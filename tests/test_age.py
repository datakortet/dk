# -*- coding: utf-8 -*-

"""age
"""

# pylint:disable=R0903, R0904
# R0903 = Too few public methods
# R0904 = Too many public methods

from dk import age
from datetime import date
# import pytest


class AgePlaceholder:
    """Placeholder used to compare the age returned by core.age.
    """
    years = 0
    months = 0
    days = 0

    def __init__(self, years, months, days):
        self.years = years
        self.months = months
        self.days = days
        
    def __repr__(self):
        return '(%d, %d, %d)' % (self.years, self.months, self.days)


def test_age():
    """Test initialization of the age-class and make sure it produces
       correct ages.
    """
    age1 = age.age(date(1975, 9, 21), date(2012, 3, 2))
    age2 = age.age(date(1990, 1, 1), date(2016, 1, 1))
    age3 = age.age(date(2012, 5, 5), date(2012, 5, 2))
    age4 = age.age(date(2011, 12, 31), date(2012, 1, 1))
    age5 = age.age(date(2000, 4, 1), date(2012, 3, 2))

    age1 == AgePlaceholder(36, 5, 10)
    age2 == AgePlaceholder(26, 0, 0)
    age3 == AgePlaceholder(-1, 11, 27)
    age4 == AgePlaceholder(0, 0, 1)
    age5 == AgePlaceholder(11, 11, 1)


def test_next_birthday():
    """Test 'next_birthday' -method.
    """
    assert age.next_birthday(date(1975, 9, 21), date(2012, 3, 2)) == date(2012, 9, 21)
    assert age.next_birthday(date(1975, 9, 21), date(2012, 9, 21)) == date(2012, 9, 21)
    assert age.next_birthday(date(1975, 9, 21), date(2012, 9, 22)) == date(2013, 9, 21)

    d = date(2013, 9, 21)
    assert age.next_birthday(d, d) == d


def test_prev_birthday():
    """age.previous_birthday()
    """
    d = date(1975, 9, 21)
    today = date(2013, 4, 9)
    assert age.previous_birthday(d, today) == date(2012, 9, 21)
    assert age.previous_birthday(today, today) == date(2012, 4, 9)


def test_birthday_this_year():
    d = date(1975, 9, 21)
    today = date(2013, 4, 9)
    assert age.birthday_this_year(d, today) == date(2013, 9, 21)


def test_years_ago():
    """Test 'years_ago' -method."""
    assert age.years_ago(4, date(2012, 3, 2)) == date(2008, 3, 2)
    assert age.years_ago(-4, date(2012, 3, 2)) == date(2016, 3, 2)
    assert age.years_ago(0) == date.today()


def test_days_ago():
    """Test 'days_ago' -method.
    """
    assert age.days_ago(10, date(2012, 1, 5)) == date(2011, 12, 26)
    assert age.days_ago(-10, date(2012, 1, 5)) == date(2012, 1, 15)
    assert age.days_ago(0) == date.today()


def test_weeks_ago():
    """Test 'weeks_ago' -method.
    """
    assert age.weeks_ago(2, date(2012, 3, 2)) == date(2012, 2, 17)
    assert age.weeks_ago(-2, date(2012, 3, 2)) == date(2012, 3, 16)
    assert age.weeks_ago(0) == date.today()
