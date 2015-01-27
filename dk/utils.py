# -*- coding: utf-8 -*-

"""XXX: many of these really should go in their own modules...
"""


import re, os, datetime


def identity(x):
    """Return the argument unchanged.
       This function is often called `identity` in programming language
       and type theory (the type is t -> t, which turns out to be a
       difficult type for most classical static type systems).
    """
    return x


def srcpath(base, pth):
    """Return an absolute path based on the relative path `pth`.
       Useful in tests, where we don't know what the absolute path is,
       and we can't use relative paths since we don't know which folder
       the tests are run from.

       In a test file xxxxxxx/foo/test/test_foo.py::

          path = 'foo/test'
          fp = open(srcpath(path, 'data/testdata.txt'))
          
    """

    # XXX: this no longer works as intended!
    
    srcroot = __file__.replace('\\', '/').rsplit('/', 1)[0]

    if not base:
        base = '/'
    base = base.replace('\\', '/')
    if base[0] != '/':
        base = '/' + base
    if base[-1] != '/':
        base += '/'
    
    return srcroot + base + pth.replace('\\', '/')
        

def root():
    "Return the root of the source tree."
    return __file__.replace('\\', '/').rsplit('/', 1)[0]


def dkpath(pth=None):
    """Usage::

         dkpath() => (w:)/xxxxxxx/
                  => (/home)/xxxxxxxx/

         dkpath('app/') => ../xxxxxxxx/app/
    """
    if not pth:
        pth = ''
    if pth.startswith('/'):
        pth = pth[1:]
    return os.path.normcase(os.path.normpath(srcpath('', pth)))


def hour_minute(v):
    "Convert 7.5 (hours) to (7, 30) i.e. 7 hours and 30 minutes."
    h = int(v)
    m = int((v - h) * 60)
    return h, m


def HourMinute(v):
    "Format 7.10 as 7t 06m."
    return '%dt %02dm' % hour_minute(v)


def hm_to_float(h, m):
    "Convert 7, 30 to 7.5 hours."
    return float(h) + (float(m) / 60.0)


def single_line(txt):
    "Remove multiple spaces and newlines."
    return u' '.join(txt.split())


def lower_case(s, encoding='u8'):
    """Return a lower cased (byte-)string version of ``s`` encoded
       in ``encoding``.
    """
    s = unicode_repr(s)
    s = s.lower()
    return s.encode(encoding)


def ulower_case(val):
    "Call val.lower(). Return '' if val is None."
    if val is None:
        return u''
    assert isinstance(val, unicode)
    return val.lower()


def title_case(s, encoding='u8'):
    """Return a title cased (byte-)string version of ``s`` encoded
       in ``encoding``.
    """
    s = unicode_repr(s)
    s = s.title()
    return s.encode(encoding)


def utitle_case(val):
    "(safer) val.title() implementation."
    if val is None:
        return u''
    if not isinstance(val, unicode):
        raise ValueError(repr(val) + ' of type ' + str(type(val)))
    return val.title()

_mixedcase = re.compile(ur'[A-ZÆØÅ][a-zæøå]+[A-ZÆØÅ]')
_mcmac = re.compile(ur'(Mc)|(Mac)|(Van)|(Von)')


def title_case_lastname(s, encoding='u8'):
    """Return a title cased version of ``s`` encoded in ``encoding``.
       If it looks like ``s`` is already title cased, then leave it alone
       (in case of manual override and complex capitalization rules for
       last names).
    """
    if not s:
        return ''
    us = unicode_repr(s)
    m = _mixedcase.match(us)
    if m:
        return us.encode(encoding)
    else:
        ts = us.title()
        return ts.encode(encoding)


def utitle_case_lastname(s):
    """Return a title cased version of ``s``.
       If ``s`` contains a recognized special case, then return it unchanged.
    """
    if not s:
        return u''
    m = _mcmac.match(s)
    if m:
        return s
    else:
        return s.title()


def unicode_repr(obj):
    """Return obj as a unicode string. If obj is a (non-)unicode string, then
       first try to decode it as utf-8, then as iso-8859-1.
    """
    if isinstance(obj, unicode):
        return obj

    if isinstance(obj, str):
        try:
            return obj.decode('u8')
        except:
            return obj.decode('l1')

    return unicode(obj)

u = unicode_repr


def utf8(obj):
    "Return a utf-8 representation of ``obj``."
    return unicode_repr(obj).encode('u8')


def latin1(obj):
    "Return a latin-1 representation of ``obj``."
    return unicode_repr(obj).encode('l1')

u8 = utf8


def unhtml(s, toencoding=None):
    "Convert charrefs for Norwegian vowels to their unicode counterparts."
    
    if type(s) not in (str, unicode):
        return s
    if type(s) is str:
        s = unicode(s)
        
    tr = {
        u'&nbsp;': u' ',
        u'&Aring;': u'Å',
        u'&AElig;': u'Æ',
        u'&Oslash;': u'Ø',
        u'&aring;': u'å',
        u'&aelig;': u'æ',
        u'&oslash;': u'ø',
        u'&eacute;': u'é',
    }

    for k, v in tr.items():
        s = s.replace(k, v)

    if toencoding is None:
        return s
    else:
        return s.encode(toencoding)


def html2u8(s):
    "Convert charrefs for Norwegian vowels to their utf-8 counterparts."    
    return unhtml(s, 'u8')


def normalize(v):
    """Return a string version of v such that
    
         normalize(u) == normalize(v) iff **not** (u != v)

       e.g.:

         normalize(None) == normalize('') == normalize(u'')
         
    """
    if type(v) == unicode:
        return v.encode('u8')
    if v in (None, ''):
        return ''
    return str(v)


def nlat(v):
    "Normalize and recover from utf-8 stored in varchar columns."
    return normalize(v).decode('u8').encode('l1')


def kronestring(kr):
    """Return a string version of the integer value ``kr``, with
       space as the thousand-separator.
    """
    if kr == 0:
        return '0'
    res = ''
    if kr < 0:
        sign = '-'
        kr = -kr
    else:
        sign = ''
        
    while kr:
        kr, tusen = divmod(kr, 1000)
        res = ' '.join(['%03d' % tusen, res])
        
    return sign + res.rstrip(' ').lstrip('0')


def orestring(n):
    u"""Return a string version of the integer ``øre`` value. Either a two-digit
       string or a dash (as in 5,-).
    """
    if n == 0:
        return '-'
    return '%02d' % n


def kr_ore(n):
    u"Convert the øre-value ``n`` to a proper NOK string value."
    kr, ore = divmod(n, 100)
    return kronestring(kr) + ',' + orestring(ore)


def mk_post(model):
    """Encode ``model`` (a dict-like object) into a dict where:

        - all values are strings
        - None values are removed
        - date values are expanded into year/month/day parts

       Note:: this function is superceeded by maint.client._encode_date
              which does this transparently for unit tests.
              
    """
    res = {}
    for key, val in model.items():
        if isinstance(val, datetime.date):
            res[key + '_year'] = str(val.year)
            res[key + '_month'] = str(val.month)
            res[key + '_day'] = str(val.day)
        elif val is None:
            pass  # do nothing
        else:
            res[key] = str(val)
    return res


class Ordered(dict):
    """
    Mapping that maintains insertion order.
    (Should be removed and the adt versions should be used).
    """
    def __init__(self):
        super(Ordered, self).__init__()
        self._ordered = []
        
    def __setitem__(self, key, val):
        super(Ordered, self).__setitem__(key, val)
        self._ordered.append(key)

    def __getitem__(self, key):
        if key not in self._ordered:
            return ''
        return super(Ordered, self).__getitem__(key)

    def keys(self):
        return self._ordered

    def values(self):
        for key in self._ordered:
            yield self[key]

    def items(self):
        for key in self._ordered:
            yield (key, self[key])
