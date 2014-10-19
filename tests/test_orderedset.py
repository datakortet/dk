# -*- coding: utf-8 -*-

"core.adt.OrderedSet"
from dk.collections import OrderedSet


def test_add():
    oset = OrderedSet.oset(range(5)[::-1])
    oset.add(20)
    assert len(oset) == 6


def test_iter_():
    "Test of the __iter__ method."
    oset = OrderedSet.oset(range(5)[::-1])
    i = 0
    for element in iter(oset):
        i = i + 1
    assert i == 5

