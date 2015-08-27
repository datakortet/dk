# -*- coding: utf-8 -*-
from datetime import timedelta
from unittest import TestCase
from dk import ttcal


class TestDuration(TestCase):
    """Unit tests for the ttcal.Duration class.
    """

    def setUp(self):
        """SetUp initial data used by all tests in this case.
        """
        self.duration1 = ttcal.Duration(days=1, hours=3, minutes=14, seconds=20)
        self.duration2 = ttcal.Duration(days=0, hours=1, minutes=10, seconds=0)
        self.duration3 = ttcal.Duration(days=0, hours=0, minutes=70, seconds=0)
        self.duration4 = ttcal.Duration(timedelta(minutes=70))

    def test_duration_tuple(self):
        """Test of the duration_tuple method.
        """
        self.assertEqual(self.duration1.duration_tuple(),
                         tuple(('', 27, 14, 20)))

    def test_str_(self):
        """Test of the __str__ method.
        """
        self.assertEqual(str(self.duration2), '1:10:00')
        self.assertEqual(str(self.duration3), '1:10:00')

    def test_parse(self):
        """Test of the parse method.
        """
        self.assertEqual(self.duration1.parse('01:10:00'), self.duration2)

    def test_add_(self):
        """Test of the __add__ method.
        """
        self.assertEqual(self.duration2 + self.duration3,
                         ttcal.Duration(hours=2, minutes=20))

    def test_sub_(self):
        """Test of the __sub__ method.
        """
        self.assertEqual(self.duration1 - self.duration2,
                         ttcal.Duration(days=1, hours=2, minutes=4, seconds=20))

    def test_mul_(self):
        """Test of the __mul__ method.
        """
        self.assertEqual(self.duration2 * 3,
                         ttcal.Duration(hours=3, minutes=30))

    def test_div_(self):
        """Test of the __div__ method.
        """
        self.assertEqual(self.duration2 / 2,
                         ttcal.Duration(minutes=35))

        # Unable to catch the error.
        # self.assertRaises(ZeroDivisionError, self.duration2 / 0)


def test_duration_rmeth():
    class Foo(object):
        def __req__(self, other):
            return 42

    assert (ttcal.Duration(years=2) == Foo()) == 42
