# -*- coding: utf-8 -*-
from datetime import date
from unittest import TestCase
from dk import ttcal


class TestMonth(TestCase):
    """Unit tests for the ttcal.Month class.
    """

    def setUp(self):
        """SetUp initial data used by all tests in this case.
        """
        self.month1 = ttcal.Month(2012, 4)
        self.month2 = ttcal.Month(year=2012, month=10)
        self.month3 = ttcal.Month(date=date(2012, 7, 10))
        # Cannot only specify month, must have year as well.
        self.assertRaises(AssertionError, ttcal.Month, month=10)

    def test_parse(self):
        """ttcal.Month.parse(txt)
        """
        assert ttcal.Month.parse('2012-04') == self.month1
        assert ttcal.Month.parse('2012-4') == self.month1
        assert ttcal.Month.parse('2012-09') == ttcal.Month(2012, 9)

    def test_from_idtag(self):
        """Test the from_idtag method.
        """
        self.assertEqual(ttcal.Month.from_idtag('m201204'), self.month1)

    def test_from_date(self):
        """Test the from_date method.
        """
        self.assertEqual(ttcal.Month.from_date(date(2012, 7, 10)), self.month3)
        self.assertEqual(ttcal.Month.from_date(date(2012, 10, 20)), self.month2)

    def test_Year(self):
        """Test the Year method.
        """
        self.assertEqual(self.month1.Year, ttcal.Year(2012))

    def test_eq_(self):
        """Test the __eq__ method.
        """
        self.assertTrue(self.month1 == date(2012, 4, 5))
        self.assertFalse(self.month2 == self.month1)

    def test_len(self):
        """Test the __len__ method.
        """
        self.assertEqual(len(self.month1), 30)

    def test_numdays(self):
        """Test the numdays method.
        """
        self.assertEqual(self.month2.numdays(), 31)

    def test_add_(self):
        """Test the __add__ method.
        """
        self.assertEqual(self.month1 + 3, ttcal.Month(2012, 7))

    def test_sub_(self):
        """Test the __sub__ method.
        """
        self.assertEqual(self.month1 - 3, ttcal.Month(2012, 1))

    def test_dayiter(self):
        """Test the dayiter method.
        """
        res = [ttcal.Day(2012, 6, 25), ttcal.Day(2012, 6, 26),
               ttcal.Day(2012, 6, 27)]
        days = []
        for i, day in enumerate(self.month3.dayiter()):
            days.append(day)
            if i == 2:
                break
        self.assertEqual(days, res)

    def test_days(self):
        """Test the days method.
        """
        res = [ttcal.Day(2012, 7, 1), ttcal.Day(2012, 7, 2),
               ttcal.Day(2012, 7, 3)]
        self.assertEqual(self.month3.days()[:3], res)

    def test_idtag(self):
        """Test the idtag method.
        """
        self.assertEqual(self.month3.idtag(), 'm20127')

    def test_daycount(self):
        """Test the daycount property.
        """
        self.assertEqual(self.month3.daycount, 31)

    def test_marked_days(self):
        """Test the mark method.
        """
        res = [ttcal.Day(2012, 10, 3), ttcal.Day(2012, 10, 10)]
        self.month2.mark(ttcal.Day(2012, 10, 10))
        self.month2.mark(ttcal.Day(2012, 10, 3))
        days = []
        for day in self.month2.marked_days():
            days.append(day)
        self.assertEqual(days, res)

    def test_format(self):
        """Test the format method.
        """
        self.assertEqual(self.month1.format(), 'April, 2012')
        self.assertEqual(self.month1.format('F-Y'), 'April-2012')
        self.assertEqual(self.month1.format('n y'), '4 12')
        self.assertEqual(self.month1.format('m'), '04')
        self.assertEqual(self.month1.format('b'), 'apr')
        self.assertEqual(self.month1.format('M'), 'Apr')
