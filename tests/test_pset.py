# -*- coding: utf-8 -*-

"dk.collections.pset"

import datetime
from dk.collections import pset, defset
#from datakortet.core.forms import POSTProxy


def test_add1():
    "Test the add method."
    p1 = pset(foo='bar', knights=9)
    p1._add('round', 'table')  # pylint:disable=W0212
    assert p1.round == 'table'


def test_remove():
    "Test the remove method."
    p1 = pset(foo='bar', knights=9)
    p1.remove('foo')
    assert str(p1) == 'pset(knights=9)'


def test_eq_():
    "Test the __eq__ method."
    p1 = pset(foo='bar', knights=9)
    p3 = defset(lambda:'bar')
    ps1 = pset(foo='bar', knights=9)
    ps2 = pset(foo='bar', knights=8)
    ps3 = pset(foo='bar')
    ps4 = pset(knights=9, foo='bar')
    assert p1 == ps1
    assert p1 != ps2
    assert p1 != ps3
    assert p1 == ps4
    assert getattr(p1, 'foo') == getattr(p3, 'foo')


# def test_xml_():
#     "Test the __xml__ method."
#     p1 = pset(foo='bar', knights=9)
#     p2 = defset('test')
#     assert xmlrepr(p1) == '<pset><knights>9</knights><foo>bar</foo></pset>'
#     assert xmlrepr(p2) == '<defset><foo>bar</foo><knights>9</knights></defset>'


def test_pprint():
    "Test the pprint method."
    # Method does not return a value so just make sure it
    # runs without raising an error or exception.
    p1 = pset(foo='bar', knights=9)
    p1.newset = pset(key=20, lock='standard')
    assert p1.pprint(indent=2) is None


# def test_add2():
#     "Test the __add__ and __radd__ methods."
#     p1 = pset(foo='bar')
#     p2 = defset(lambda:'bar')
#     p2.ny = 'test'
#     assert p1 + pset(ny='test') == p2
#     assert pset(ny='test') + p1 == p2

