# -*- coding: utf-8 -*-

"""Run the doctests manually, so we don't have to invoke py.test with special
   flags.
"""

from pset import test_pset
from sdict import test_sdict


def test_all():
    "Run all tests."
    test_pset()
    test_sdict()

if __name__ == "__main__":
    test_all()
