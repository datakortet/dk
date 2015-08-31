# -*- coding: utf-8 -*-
import datetime
from itertools import islice


# def _cmp_ttuple(op):
#     rname = '__r{}__'.format(op.__name__)
#
#     def relop_meth(self, other):
#         if hasattr(other, rname):
#             return getattr(other, rname)(self)
#         try:
#             return op(self.timetuple(), other.timetuple())
#         except:
#             return False
#     return relop_meth
#
#


def chop(it, n):
    """Chop iterator into `n` size chuchks.
    """
    while 1:
        s = list(islice(it, n))
        if not s:
            break
        yield s


def isoweek(year, week):
    """Iterate over the days in isoweek `week` of `year`.
    """
    # 4th of January is always in week 1
    wk1date = datetime.date(year, 1, 4)

    # daynumber of the 4th, zero-based
    weekday = wk1date.weekday()

    # (proleptic Gregorian) ordinal of first day of week 1
    day1 = wk1date.toordinal() - weekday

    # first day in week
    start = day1 + (week - 1) * 7
    # one past last day in week
    stop = day1 + week * 7

    for n in range(start, stop):
        yield datetime.date.fromordinal(n)
