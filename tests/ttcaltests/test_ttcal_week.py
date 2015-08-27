# -*- coding: utf-8 -*-
from datetime import date
from unittest import TestCase
from dk import ttcal


class TestWeek(TestCase):
    """Unit tests for the ttcal.Week class.
    """

    def setUp(self):
        """SetUp default data for the tests.
        """
        self.week1 = ttcal.Week.weeknum(4, 2012)
        self.week2 = ttcal.Week.weeknum(1)
        self.week3 = ttcal.Week.weeknum(52, 2012)
        self.week4 = ttcal.Week.weeknum(4, 2012)

    def test_idtag(self):
        """Test the idtag method.
        """
        currentyear = date.today().year
        self.assertEqual(self.week1.idtag(), 'w20124')
        self.assertEqual(self.week2.idtag(), 'w%s1' % currentyear)
        self.assertEqual(self.week3.idtag(), 'w201252')

    def test_datetuple(self):
        """Test the datetuple method.
        """
        self.assertEqual(self.week1.datetuple(), tuple((2012, 1, 23)))

    def test_str_(self):
        """Test the __str__ method.
        """
        self.assertEqual(str(self.week1), 'Uke 4 (2012)')
        self.assertEqual(str(self.week3), 'Uke 52 (2012)')

    def test_eq_(self):
        """Test the __eq__ method defined in Week.
        """
        self.assertFalse(self.week1 == self.week2)
        self.assertTrue(self.week1 == self.week4)

    def test_from_idtag(self):
        """Test the from_idtag method.
        """
        self.assertEqual(ttcal.Week.from_idtag('w20124'), self.week1)


class TestWeeks(TestCase):
    """Unit tests for the ttcal.Weeks class.
    """

    def setUp(self):
        """SetUp default data for the tests.
        """
        self.weeks = ttcal.Weeks(5, 10)  # 5, 6, 7, 8, 9, 10 (n=6)
        self.first = self.weeks.first
        self.last = self.weeks.last

    def test_first(self):
        """Test the first property.
        """
        self.assertEqual(self.weeks.first, self.last - 7 * 6 + 1)

    def test_last(self):
        """Test the last property.
        """
        self.assertEqual(self.weeks.last, self.first + 7 * 6 - 1)

    def test_datetuple(self):
        """Test the datetuple method.
        """
        self.assertEqual(self.weeks.datetuple(), self.first.datetuple())
