# -*- coding: utf-8 -*-
from datetime import date
from unittest import TestCase
from dk import ttcal


class TestYear(TestCase):
    """Unit tests for the ttcal.Year class.
    """

    def setUp(self):
        """SetUp initial data used by all tests in this case.
        """
        self.year1 = ttcal.Year(2005)
        self.year2 = ttcal.Year()
        self.year3 = ttcal.Year(2025)

    def test_from_idtag(self):
        """Test of the from_idtag method.
        """
        self.assertEqual(self.year1.from_idtag('y2005'), self.year1)

    def test_idtag(self):
        """Test of the idtag method.
        """
        self.assertEqual(self.year3.idtag(), 'y2025')

    def test_add_(self):
        """Test of the __add__ method.
        """
        self.assertEqual(self.year1 + 5, ttcal.Year(2010))

    def test_sub_(self):
        """Test of the __sub__ method.
        """
        self.assertEqual(self.year1 - 3, ttcal.Year(2002))

    def test_prev(self):
        """Test of the prev method.
        """
        self.assertEqual(self.year1.prev(), ttcal.Year(2004))

    def test_next(self):
        """Test of the next method.
        """
        self.assertEqual(self.year1.next(), ttcal.Year(2006))

    def test_periods(self):
        """Test of periods using misc methods and properties.
        """
        first_half = [ttcal.Month(2005, 1), ttcal.Month(2005, 2),
                      ttcal.Month(2005, 3), ttcal.Month(2005, 4),
                      ttcal.Month(2005, 5), ttcal.Month(2005, 6)]
        Q3 = [ttcal.Month(2005, 7), ttcal.Month(2005, 8), ttcal.Month(2005, 9)]
        self.assertEqual(self.year1.H1, first_half)
        self.assertEqual(self.year1.Q3, Q3)

        self.assert_(self.year1.halves())
        self.assert_(self.year1.quarters())
        self.assert_(self.year1.january)
        self.assert_(self.year1.february)
        self.assert_(self.year1.march)
        self.assert_(self.year1.april)
        self.assert_(self.year1.may)
        self.assert_(self.year1.june)
        self.assert_(self.year1.july)
        self.assert_(self.year1.august)
        self.assert_(self.year1.september)
        self.assert_(self.year1.october)
        self.assert_(self.year1.november)
        self.assert_(self.year1.december)

    def test_mark_period(self):
        """Test the mark_period method.
        """
        res = [ttcal.Day(2025, 3, 1), ttcal.Day(2025, 3, 2),
               ttcal.Day(2025, 3, 3)]
        self.year3.mark_period(self.year3.march)
        days = []
        for i, day in enumerate(self.year3.marked_days()):
            days.append(day)
            if i == 2:
                break
        self.assertEqual(days, res)

    def test_eq_(self):
        """Test the __eq__ method.
        """
        self.assertTrue(self.year2 == ttcal.Year(date.today().year))
        self.assertFalse(self.year1 == self.year3)
