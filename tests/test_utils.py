# -*- coding: utf-8 -*-
from dk.utils import *


def test_srcpath():
    assert srcpath(base=None, pth='foo/bar/things.py')[-23:] == 'dk/dk/foo/bar/things.py'
    assert srcpath(base='foo', pth='bar/things.py')[-23:] == 'dk/dk/foo/bar/things.py'
    assert srcpath(base='foo\\bar', pth='things.py')[-23:] == 'dk/dk/foo/bar/things.py'


def test_root():
    assert root()[-6:] == '/dk/dk'


def test_dkpath():
    win = dkpath('foo')[-9:] == 'dk\\dk\\foo'
    unix = dkpath('foo')[-9:] == 'dk/dk/foo'
    assert win or unix


def test_hour_minute():
    assert hour_minute(7.5) == (7, 30)
    assert hour_minute(2.25) == (2, 15)
    assert hour_minute(3.75) == (3, 45)


def test_HourMinute():
    assert HourMinute(7.10) == '7t 05m'
    assert HourMinute(2.25) == '2t 15m'
    assert HourMinute(3.75) == '3t 45m'


def test_hm_to_float():
    assert hm_to_float(7, 30) == 7.5
    assert hm_to_float(2, 15) == 2.25


def test_single_line():
    string = '''This text is totally
    foobar.
    And on that note, we   have  left the
    building.
    '''
    result = 'This text is totally foobar. And on that note, we have left the building.'
    assert single_line(string) == result


def test_lower_case():
    lower_case('This is JUST a test!!') == 'this is just a test!!'
    lower_case('Gåsa flyr over Høybukta') == 'gåsa flyr over høybukta'
    lower_case('Gåsa flyr over Høybukta', 'l1') == 'gåsa flyr over høybukta'


def test_ulower_case():
    assert ulower_case(None) == u''
    assert lower_case('Tømmer og biller') == 'tømmer og biller'


def test_title_case():
    assert title_case('høna verper egg') == 'Høna Verper Egg'


def test_utitle_case():
    assert utitle_case(u'hanen stend på stabburshella') == u'Hanen Stend På Stabburshella'


def test_title_case_lastname():
    assert title_case_lastname('ole olsen') == 'Ole Olsen'
    assert title_case_lastname(u'jan jönson') == 'Jan J\xc3\xb6nson'
    assert title_case_lastname(u'jan jönson', 'l1') == 'Jan J\xf6nson'


def test_utitle_case_lastname():
    assert utitle_case_lastname('ole olsen') == 'Ole Olsen'
    assert utitle_case_lastname(u'jan jönson') == u'Jan Jönson'


def test_unicode_repr():
    assert unicode_repr('Laksen springer i håven') == u'Laksen springer i håven'
    assert unicode_repr(object())[:17] == '<object object at'


def test_unhtml():
    string = u'&nbsp;&Aring;&AElig;&Oslash;&aring;&aelig;&oslash;&eacute;'
    result = u' ÅÆØåæøé'
    assert unhtml(string) == result


def test_html2u8():
    string = u'&nbsp;&Aring;&AElig;&Oslash;&aring;&aelig;&oslash;&eacute;'
    result = ' ÅÆØåæøé'
    assert html2u8(string) == result


def test_kronestring():
    assert kronestring(1054) == '1 054'
