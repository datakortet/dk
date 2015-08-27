# -*- coding: utf-8 -*-
from datetime import timedelta
from unittest import TestCase
from dk import ttcal
import pytest


@pytest.fixture
def dd():
    return [
        ttcal.Duration(days=1, hours=3, minutes=14, seconds=20),
        ttcal.Duration(days=0, hours=1, minutes=10, seconds=0),
        ttcal.Duration(days=0, hours=0, minutes=70, seconds=0),
        ttcal.Duration(timedelta(minutes=70)),
    ]


def test_duration_tuple(dd):
    assert dd[0].duration_tuple() == ('', 27, 14, 20)


def test_str(dd):
    assert str(dd[1]) == '1:10:00'
    assert str(dd[2]) == '1:10:00'
    assert "%s" % dd[3] == '1:10:00'


def test_parse(dd):
    assert dd[1].parse('01:10:00') == dd[2]


def test_add(dd):
    assert dd[2] + dd[3] == ttcal.Duration(hours=2, minutes=20)


def test_sub(dd):
    tmp = ttcal.Duration(days=1, hours=2, minutes=4, seconds=20)
    assert dd[0] - dd[1] == tmp


def test_mul(dd):
    assert dd[2] * 3 == ttcal.Duration(hours=3, minutes=30)


def test_div(dd):
    assert dd[2] / 2 == ttcal.Duration(minutes=35)


def test_duration_rmeth():
    class Foo(object):
        def __req__(self, other):
            return 42

    assert (ttcal.Duration(years=2) == Foo()) == 42
