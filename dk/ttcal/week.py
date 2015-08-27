# -*- coding: utf-8 -*-
import datetime
from .day import Day, Days
from .calfns import isoweek


class Week(object):
    def range(self):
        """Return an iterator for the range of `self`.
        """
        if hasattr(self, 'dayiter'):
            return self.dayiter()
        return Days(self.first, self.last)

    def between_tuple(period):  # pylint:disable=E0213
        """Return a tuple of datetimes that is convenient for sql
           `between` queries.
        """
        return (period.first.datetime(),
                (period.last + 1).datetime() - datetime.timedelta(seconds=1))

    @property
    def middle(self):
        """Return the day that splits the date range in half.
        """
        middle = (self.first.toordinal() + self.last.toordinal()) // 2
        return Day.fromordinal(middle)

    def timetuple(self):
        """Create timetuple from datetuple.
           (to interact with datetime objects).
        """
        d = datetime.date(*self.datetuple())
        t = datetime.time()
        return datetime.datetime.combine(d, t)

    @classmethod
    def from_idtag(cls, tag):
        # w20081
        y = int(tag[1:5])
        w = int(tag[5:])
        return cls.weeknum(w, y)

    @classmethod
    def weeknum(cls, n, year=None):
        if year is None:
            year = datetime.date.today().year
        days = list(isoweek(year, n))
        month = days[0].month  # quite arbitrary
        return cls(days, month)

    def __init__(self, days, month):
        super(Week, self).__init__()
        # thursday is always in the correct iso-year per definition
        t = days[3].isocalendar()
        self.year = t[0]
        self.num = t[1]
        self.days = [Day(d, membermonth=month) for d in days]
        self.month = month

    @property
    def current(self):
        """True if today is in week.
        """
        return any(d.today for d in self.days)

    def idtag(self):
        return 'w%d%d' % (self.year, self.num)

    @property
    def first(self):
        """1st day of week.
        """
        return self.days[0]

    @property
    def last(self):
        """Last day of week.
        """
        return self.days[-1]

    def datetuple(self):
        """First day of this week.
        """
        return self.year, self.month, self.first.day

    def __str__(self):
        return 'Uke %d (%d)' % (self.num, self.year)

    def __repr__(self):
        return 'Week(%d, month=%d, year=%d)' % (self.num, self.month, self.year)

    def __iter__(self):
        return iter(self.days)

    def until_today(self):
        for d in self.days:
            if d.today:
                break
            yield d

    def __hash__(self):
        return self.year * 100 + self.num

    def __eq__(self, other):
        return self.year == other.year and self.num == other.num

    def __getitem__(self, n):
        return self.days[n]

    def __contains__(self, date):
        return date in self.days


class Weeks(list):
    def __init__(self, start, end):
        super(Weeks, self).__init__()
        assert start <= end
        for i in range(start, end + 1):
            self.append(Week.weeknum(i))

    def range(self):
        """Return an iterator for the range of `self`.
        """
        if hasattr(self, 'dayiter'):
            return self.dayiter()
        return Days(self.first, self.last)

    def between_tuple(period):  # pylint:disable=E0213
        """Return a tuple of datetimes that is convenient for sql
           `between` queries.
        """
        return (period.first.datetime(),
                (period.last + 1).datetime() - datetime.timedelta(seconds=1))

    @property
    def middle(self):
        """Return the day that splits the date range in half.
        """
        middle = (self.first.toordinal() + self.last.toordinal()) // 2
        return Day.fromordinal(middle)

    def timetuple(self):
        """Create timetuple from datetuple.
           (to interact with datetime objects).
        """
        d = datetime.date(*self.datetuple())
        t = datetime.time()
        return datetime.datetime.combine(d, t)

    @property
    def first(self):
        """First day in first week.
        """
        return self[0][0]

    @property
    def last(self):
        """Last day in last week.
        """
        return self[-1][-1]

    def datetuple(self):
        """First day of first week.
        """
        return self.first.datetuple()

    def dayiter(self):
        """Iterate over all days in all the weeks.
        """
        for wk in self:
            for day in wk:
                yield day

    def __repr__(self):
        return '[' + ', '.join(map(str, iter(self))) + ']'


def _Week(self):
    """Return a Week object representing the week `self` belongs to.
    """
    return Week.weeknum(self.weeknum, self.isoyear)
Day.week = property(_Week)
