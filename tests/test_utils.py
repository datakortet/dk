# -*- coding: utf-8 -*-
import pytest

from dk.utils import *


def test_identity():
    assert  identity(identity(42)) == 42

# def test_srcpath():
#     assert srcpath(base=None, pth='foo/bar/things.py')[-28:] == '/lib/dk/dk/foo/bar/things.py'
#     assert srcpath(base='foo', pth='bar/things.py')[-28:] == '/lib/dk/dk/foo/bar/things.py'
#     assert srcpath(base='foo\\bar', pth='things.py')[-28:] == '/lib/dk/dk/foo/bar/things.py'


# def test_root():
#     assert root()[-11:] == '/datakortet'


# def test_dkpath():
#     win = dkpath('foo')[-14:] == '\\lib\\dk\\dk\\foo'
#     unix = dkpath('foo')[-14:] == '/lib/dk/dk/foo'
#     assert win or unix


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
    assert lower_case('This is JUST a test!!') == b'this is just a test!!'
    assert lower_case('Gåsa flyr over Høybukta') == u'gåsa flyr over høybukta'.encode('u8')
    assert lower_case('Gåsa flyr over Høybukta', 'l1') == u'gåsa flyr over høybukta'.encode('l1')


def test_ulower_case():
    assert ulower_case(None) == u''
    assert ulower_case(u'Tømmer og biller') == u'tømmer og biller'


def test_title_case():
    assert title_case('høna verper egg') == u'Høna Verper Egg'.encode('u8')


def test_utitle_case():
    assert utitle_case(None) == u''
    with pytest.raises(ValueError):
        utitle_case(42)
    assert utitle_case(u'hanen stend på stabburshella') == u'Hanen Stend På Stabburshella'


def test_title_case_lastname():
    assert title_case_lastname(None) == b''
    assert title_case_lastname(u'OlSen') == b'OlSen'
    assert title_case_lastname('ole olsen') == b'Ole Olsen'
    assert title_case_lastname(u'jan jönson') == b'Jan J\xc3\xb6nson'
    assert title_case_lastname(u'jan jönson', 'l1') == b'Jan J\xf6nson'


def test_utitle_case_lastname():
    assert utitle_case_lastname(None) == ''
    assert utitle_case_lastname(u"McDonald") == 'McDonald'
    assert utitle_case_lastname('ole olsen') == 'Ole Olsen'
    assert utitle_case_lastname(u'jan jönson') == u'Jan Jönson'


def test_unicode_repr():
    assert unicode_repr('Laksen springer i håven') == u'Laksen springer i håven'
    assert unicode_repr(object())[:17] == '<object object at'
    assert unicode_repr(u'Bjørn'.encode('iso-8859-1')) == u'Bjørn'


def test_normalize():
    assert normalize(42) == b'42'
    assert normalize(None) == b''
    assert normalize(u'bjørn') == u'bjørn'.encode('u8')


def test_nlat():
    assert nlat(42) == b'42'
    assert nlat(None) == b''
    assert nlat(u'bjørn') == u'bjørn'.encode('l1')


def test_utf8():
    assert utf8(42) == b'42'


def test_latin1():
    assert latin1(42) == b'42'


def test_unhtml():
    assert unhtml(42) == 42
    string = u'&nbsp;&Aring;&AElig;&Oslash;&aring;&aelig;&oslash;&eacute;'
    result = u' ÅÆØåæøé'
    assert unhtml(string) == result
    assert unhtml(string.encode('u8')) == result


def test_html2u8():
    string = u'&nbsp;&Aring;&AElig;&Oslash;&aring;&aelig;&oslash;&eacute;'
    result = u' ÅÆØåæøé'.encode('u8')
    assert html2u8(string) == result


def test_kronestring():
    assert kronestring(0) == '0'
    assert kronestring(1054) == '1 054'
    assert kronestring(-1054) == '-1 054'


def test_orestring():
    assert orestring(0) == '-'
    assert orestring(2) == '02'
    assert orestring(42) == '42'


def test_kr_ore():
    assert kr_ore(1054) == '10,54'
