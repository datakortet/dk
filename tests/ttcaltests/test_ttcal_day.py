# -*- coding: utf-8 -*-
from datetime import date
from unittest import TestCase
import six
from dk import ttcal


class TestDay(TestCase):
    """Unit tests for the ttcal.Day class.
    """

    def setUp(self):
        """SetUp default data for the tests.
        """
        self.day1 = ttcal.Day(date(2012, 4, 10))
        self.day2 = ttcal.Day(2012, 4, 8)
        self.day3 = ttcal.Day()
        self.today = ttcal.Today()

    def test_get_day_name(self):
        """Test of the get_day_name method.
        """
        self.assertEqual(self.day1.get_day_name(2), 'onsdag')
        self.assertEqual(self.day2.get_day_name(2, 3), 'ons')

    def test_hash_(self):
        """Test of the __hash__ method.
        """
        # hash(x) truncates the returned value from __hash__ in Python 3..
        #self.assertEqual(hash(self.day1), hash(hash(self.day1)))
        self.assertEqual(hash(self.day1), hash(self.day1))

    def test_unicode_(self):
        """Test of the __unicode__ method.
        """
        self.assertEqual(six.text_type(self.day2), six.u('2012-04-08'))

    def test_datetuple(self):
        """Test of the datetuple method.
        """
        self.assertEqual(self.day2.datetuple(), tuple((2012, 4, 8)))

    def test_add_(self):
        """Test of the __add__ method.
        """
        self.assertEqual(self.day2 + 3, ttcal.Day(2012, 4, 11))

    def test_sub_(self):
        """Test of the __sub__ method.
        """
        self.assertEqual(self.day1 - 5, ttcal.Day(2012, 4, 5))

    def test_day_name(self):
        """Test of the day_name property.
        """
        self.assertEqual(self.day1.dayname, 'tirsdag')
        self.assertEqual(self.day2.dayname, u'søndag')

    def test_code(self):
        """Test of the code property.
        """
        self.assertEqual(self.day1.code, 'U')

    def test_weeknum(self):
        """Test of the weeknum property.
        """
        self.assertEqual(self.day1.weeknum, 15)

    def test_isoyear(self):
        """Test of the isoyear property.
        """
        self.assertEqual(self.day1.isoyear, 2012)

    def test_week(self):
        """Test of the week property.
        """
        week = ttcal.Week.weeknum(15, 2012)
        self.assertEqual(self.day1.week, week)

    def test_Month(self):
        """Test of the Month property.
        """
        month = ttcal.Month(2012, 4)
        self.assertEqual(self.day1.Month, month)

    def test_Year(self):
        """Test of the Year property.
        """
        year = ttcal.Year(2012)
        self.assertEqual(self.day1.Year, year)

    def test_display(self):
        """Test of the display property.
        """
        #self.assertEqual(self.day3.display, 'today month')
        self.assertTrue('today' in self.day3.display)
        self.assertTrue('month' in self.day3.display)

    def test_idtag(self):
        """Test of the idtag property.
        """
        self.assertEqual(self.day1.idtag, 'd2012041004')

    def test_today(self):
        """Test of the today property.
        """
        self.assertTrue(self.day3.today)
        self.assertEqual(self.day1.today, False)

    def test_weekday(self):
        """Test of the weekday property.
        """
        self.assertTrue(self.day1.weekday)
        self.assertNotEqual(self.day2.weekday, True)  # Does not return False

    def test_weekend(self):
        """Test of the weekend property.
        """
        self.assertTrue(self.day2.weekend)
        self.assertNotEqual(self.day1.weekend, True)  # Does not return False

    def test_in_month(self):
        """Test of the in_month property.
        """
        self.assertTrue(self.day3.in_month)

    def test_compare(self):
        """Test the compare method.
        """
        self.assertEqual(self.day1.compare(self.day2), 'month')

    def test_compare_specific(self):
        """Test the methods in the CompareMixin class.
        """
        self.assertTrue(self.day1 > self.day2)
        self.assertFalse(self.day1 < self.day2)
        self.assertFalse(self.day1 <= self.day2)
        self.assertTrue(self.day1 >= self.day2)
        self.assertFalse(self.day1 == self.day2)
        self.assertTrue(self.day1 != self.day2)

    def test_format(self):
        """Test the format method.
        """
        self.assertEqual(self.day1.format('y-m-d'), '12-04-10')
        self.assertEqual(self.day1.format('Y-W'), '2012-15')
        self.assertEqual(self.day1.format('b'), 'apr')
        self.assertEqual(self.day1.format('w'), '1')
        self.assertEqual(self.day1.format('D-n'), 'tir-4')
        self.assertEqual(self.day1.format('z'), '100')
        self.assertEqual(self.day1.format(), u'Apr 10, 2012')

    def test_from_idtag(self):
        """Test the from_idtag method.
        """
        self.assertEqual(ttcal.Day.from_idtag('d2012041004'), self.day1)

    def test_parse(self):
        """Test the parse method.
        """
        self.assertEqual(self.day1.parse('04/08/2011'), ttcal.Day(2011, 8, 4))
        self.assertEqual(self.day1.parse('2012-04-06'), ttcal.Day(2012, 4, 6))
        self.assertEqual(self.day1.parse('2012-4-6'), ttcal.Day(2012, 4, 6))
        self.assertEqual(self.day1.parse('20130619'), ttcal.Day(2013, 6, 19))
        self.assertEqual(self.day1.parse('12.11.2013'), ttcal.Day(2013, 11, 12))
        self.assertEqual(self.day1.parse('12.10.13'), ttcal.Day(2013, 10, 12))

        self.assertRaises(ValueError, self.day1.parse, '12.10.11')
        self.assertRaises(ValueError, self.day1.parse, '21/13/2011')


class TestDays(TestCase):
    """Unit tests for the ttcal.Days class.
    """

    def setUp(self):
        """SetUp default data for the tests.
        """
        self.days = ttcal.Days(date(2012, 1, 1), date(2012, 1, 10))

    def test_first(self):
        """Test the first property.
        """
        first = self.days.first
        self.assertEqual([first.year, first.month, first.day], [2012, 1, 1])

    def test_middle(self):
        """Test the middle property.
        """
        middle = self.days.middle
        self.assertEqual([middle.year, middle.month, middle.day], [2012, 1, 5])

    def test_last(self):
        """Test the last property.
        """
        last = self.days.last
        self.assertEqual([last.year, last.month, last.day], [2012, 1, 10])

    def test_range(self):
        """The the range method defined in the RangeMixin class.
        """
        res = [ttcal.Day(2012, 1, 1), ttcal.Day(2012, 1, 2),
               ttcal.Day(2012, 1, 3), ttcal.Day(2012, 1, 4),
               ttcal.Day(2012, 1, 5), ttcal.Day(2012, 1, 6),
               ttcal.Day(2012, 1, 7), ttcal.Day(2012, 1, 8),
               ttcal.Day(2012, 1, 9), ttcal.Day(2012, 1, 10)]
        self.assertEqual(self.days.range(), res)
