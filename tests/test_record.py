
from unittest import TestCase
import datetime
from dk import collections as adt


class TestRecord(TestCase):
    "Unit tests of the record class."

    def setUp(self):
        self.ff = adt.record(id=1, band='Foo Fighters', genre='Rock')
        self.ni = adt.record(id=2, band='Nirvana', genre='Grunge')
        self.me = adt.record(id=3, band='Metallica', genre='Metal')

    def test_fields(self):
        "Test the fields property."
        assert set(self.ff.fields) == {'Genre', 'Band', 'Id'}

    def test_strvals(self):
        "Test the strvals method."
        self.me.datetime = datetime.datetime(2012, 5, 17, 13, 44, 22)
        assert set(self.me.strvals()) == {'Metal', 'Metallica', '3', '2012-05-17 13:44:22'}

    def test_trans(self):
        "Test the trans method."
        t = self.ni.trans()
        assert set(t.keys()) == {b'id', b'band', b'genre'}
        assert t[b'id'] == 2
        assert t[b'band'] == b'Nirvana'
        assert t[b'genre'] == b'Grunge'

    def test_commit(self):
        "Test the commit method."
        assert self.ff.commit() == self.ff

    def test_changed(self):
        "Test the changed and rollback methods."
        self.ff.commit()
        self.ff.genre = 'Indie-rock'
        assert self.ff.changed() == ['genre']
        self.ff.rollback()
        assert self.ff == adt.record(id=1, band='Foo Fighters', genre='Rock')
