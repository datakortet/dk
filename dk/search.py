# -*- coding: utf-8 -*-

"""Generic search algorithm.
"""
from dk.collections import pset
from dknorway import postnrcache

import re
import datetime
from dkorm import modelmeta, query as dkquery

import django.db.models


def search(cls, terms="", query=None, columns=()):
    """Search the cls for terms.

       cls is either an core.orm class or a Django model class.
       terms is the text the user typed into the search box.
       query (optional) is the query object we should limit the search to.
       columns (optional) is the columns we should search.

       If query is not passed, we search all records.
       
       If columns is not specified we use:
         Django models:  the search_fields defined in the model's Admin class.
         core.orm:       all text and possibly datetime fields.

       This function returns a query that can be furter specified. E.g. to
       only get the last 10 results::

          q = search.search(Salg, '98004988', columns=['telefon'])
          last_10 = q.order_by('-id')[:10]
       
    """
    m = modelmeta.info(cls)
    if query is None:
        query = cls.objects.all()

    if not terms:
        return query

    columns = initial_search_columns(m, columns)
        
    Q = dkquery.Q if m.is_orm else django.db.models.Q

    for _term, termtypes in TermParser(terms):
        q = Q()

        # Add Q-objects for all columns that have coltype compatible with
        # termtype.

        for termtype, typedval in termtypes:
            for column in columns:
                _, colname = column
                
                if compatible_types(termtype, typedval, column):
                    q |= Q(**{colselector(termtype, colname): typedval})

        query = query.filter(q)

    return query


def compatible_types(termtype, typedval, column):
    "Return true if we can search for typedval in colname."

    colinfo, colname = column
    # Don't limit foreign fields to str only. The foreign fields are not
    # only keys, but other fields that can be int, float and so on.
    if '__' in colname: #and termtype == 'str':  # foreign key string search
        return True

    if colinfo is None:
        raise ValueError('No colinfo: %r %r' % column)
    coltype = colinfo.internal_type
    
    if termtype == 'str':
        return (colname.lower() not in ['postnr'] and
                coltype in ['CharField', unicode, str] and
                len(typedval) <= colinfo.max_length)
    elif termtype == 'int':
        return coltype in ['PositiveIntegerField', int, long]
    elif termtype == 'date':
        return coltype in ['DateField', datetime.date, datetime.datetime]
    elif termtype == 'year':
        return coltype in ['DateField', datetime.date, datetime.datetime]
    elif termtype == 'bool':
        return coltype in ['BooleanField', bool]
    elif termtype == 'float':
        return coltype in ['FloatField', float]
    elif termtype == 'postnr':
        return (colname.lower() == 'postnr' and
                coltype in ['CharField', unicode, str])
    else:
        raise ValueError('Unknown termtype: %r' % termtype)
    

TYPECOMPAT = {
    'str': ['CharField', unicode, str],
    'int': ['PositiveIntegerField', int, long],
    'date': ['DateField', datetime.date, datetime.datetime],
    'year': ['DateField', datetime.date, datetime.datetime],
    'bool': ['BooleanField', bool],
    'float': ['FloatField', float],
    }


def colselector(termtype, colname):
    "How should we match values of termtype?"

    if termtype == 'str':
        # for string values we test with like
        return '%s__icontains' % colname
    elif termtype == 'year':
        # for year values...
        return '%s__year' % colname
    else:
        # for other values we test with equals
        return colname


def initial_search_columns(meta, columns):
    """Return list of (column_type, column_name).
       Finds searchfields defined in model if none are specified as arguments.
    """
    def _coldetails(cols):
        return [(meta.field_info[c], c)
                for c in cols]
            
    if columns:
        return _coldetails(columns)

    return _coldetails(meta.search_fields)


class TermParser(object):
    "Split the text the user entered into the search box into typed chunks."
    
    ISO_DATE_RE = re.compile(r'(?P<yr>\d{4})-(?P<mnth>\d+)-(?P<day>\d+)$')
    NO_DATE_RE = re.compile(r'(?P<day>\d+)[/\.](?P<mnth>\d+)[/\.](?P<yr>\d+)$')
    PERSNR_DATE_RE = re.compile(r'(\d{6})$')
    BOOL_TRUE = re.compile(r'(ja|J|yes|Y)$', re.I)
    BOOL_FALSE = re.compile(r'(nei|N|no)$', re.I)
    POSTNR = re.compile(r'(?P<postnr>\d{4})$')
    YEAR_RE = re.compile(r'(?P<yr>((19)|(20))\d\d)$')
    
    def __init__(self, termtxt):
        "termtxt is the text the user entered into the search box."

        self.raw_terms = termtxt.split()

        self.terms = pset()
        for term in self.raw_terms:
            self.terms[term] = [('str', term)]
            self.parse(term)

    def __iter__(self):
        return iter(self.terms)

    def parse(self, term):
        "Main parse function."
        self.parse_isodate(term)
        self.parse_nodate(term)
        self.parse_persnrdate(term)
        self.parse_int(term)
        self.parse_float(term)
        self.parse_bool(term)
        self.parse_postnr(term)
        self.parse_year(term)

    def parse_bool(self, term):
        "ja/nei/yes/no/etc."
        m = TermParser.BOOL_FALSE.match(term)
        if m:
            self.terms[term].append(('bool', False))
        m = TermParser.BOOL_TRUE.match(term)
        if m:
            self.terms[term].append(('bool', True))
        
    def parse_isodate(self, term):
        "Dates in ISO format, 1970-05-02."
        m = TermParser.ISO_DATE_RE.match(term)
        if m:
            grps = m.groupdict()
            yr = int(grps['yr'])
            mnth = int(grps['mnth'])
            day = int(grps['day'])
            
            try:
                self.terms[term].append(('date', datetime.date(yr, mnth, day)))
            except ValueError:
                pass

    def parse_nodate(self, term):
        "Norwegian date formats, 2.5.1970 or 2/5/1970."
        m = TermParser.NO_DATE_RE.match(term)
        if m:
            grps = m.groupdict()
            yr = int(grps['yr'])
            if 50 < yr < 100:
                yr += 1900
            if yr < 50:
                yr += 2000
                    
            mnth = int(grps['mnth'])
            day = int(grps['day'])

            try:
                self.terms[term].append(('date', datetime.date(yr, mnth, day)))
            except ValueError:
                pass

    def parse_persnrdate(self, term):
        "datetime format found in persnr? (020570 == 1970-05-02)"
        m = TermParser.PERSNR_DATE_RE.match(term)
        if m:
            day = int(term[:2])
            mnth = int(term[2:4])
            yr = int(term[4:])
            if 50 < yr < 100:
                yr += 1900
            if yr < 50:
                yr += 2000
            
            try:
                self.terms[term].append(('date', datetime.date(yr, mnth, day)))
            except ValueError:
                pass

    def parse_int(self, term):
        "int?"
        try:
            self.terms[term].append(('int', int(term)))
        except ValueError:
            pass

    def parse_float(self, term):
        "float?"
        try:
            #if '.' in term:
            self.terms[term].append(('float', float(term)))
        except ValueError:
            pass

    def parse_postnr(self, term):
        "postnr?"
        m = TermParser.POSTNR.match(term)
        if m:
            if int(term) in postnrcache.valid_postnrs:
                self.terms[term].append(('postnr', term))

    def parse_year(self, term):
        "Year?"
        m = TermParser.YEAR_RE.match(term)
        if m:
            self.terms[term].append(('year', term))
