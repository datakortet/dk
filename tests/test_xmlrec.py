import datetime
from decimal import Decimal

from dk.collections.xmlrec import Boolean, NOK, Datetime, Date


def test_Boolean():
    assert Boolean('true')
    assert not Boolean('false')
    assert Boolean(42)


def test_NOK():
    assert NOK('123,45') == Decimal('123.45')


def test_Datetime():
    assert Datetime('2020-06-04 15:47') == datetime.datetime(2020, 6, 4, 15, 47)
    assert Datetime('hello world') is None


def test_Date():
    assert Date('2020-06-04') == datetime.datetime(2020, 6, 4)
    assert Date('hello world') is None
