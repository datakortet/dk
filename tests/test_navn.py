# -*- coding: utf-8 -*-

"""datakortet.tag
"""

import unittest

from dk.identifiers import navn


class NameTest(unittest.TestCase):
    "datakortet.tag.navn"

    def setUp(self):
        self.fname = 'Bjorn Steinar'
        self.lname = 'Fjeld Pettersen'
        self.fnameu = u'Bjørn Øystein'
        self.lnameu = u'Ødal Pættersen'

    def test_ascii(self):
        "Basic ascii tests."
        n = navn.forkort_navn(25, self.fname, self.lname)
        self.assertEqual(n, u'Bjorn S Fjeld Pettersen')
        n = navn.forkort_navn(22, self.fname, self.lname)
        self.assertEqual(n, u'Bjorn S F Pettersen')
        try:
            n = navn.forkort_navn(18, self.fname, self.lname)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_unicode(self):
        "Basic unicode tests."
        n = navn.forkort_navn(25, self.fnameu, self.lnameu)
        self.assertEqual(n, u'Bjørn Ø Ødal Pættersen')
        n = navn.forkort_navn(21, self.fnameu, self.lnameu)
        self.assertEqual(n, u'Bjørn Ø Ø Pættersen')
        n = navn.forkort_navn(21, self.fnameu, self.lnameu)
        self.assertEqual(n, u'Bjørn Ø Ø Pættersen')

    def test_normalize_u8(self):
        "Normalization tests."
        b = u'Bjørn'.encode('u8')
        self.assertEqual(b, navn.normalize2u8(u'Bjørn'))
        self.assertEqual(b, navn.normalize2u8(u'Bjørn'.encode('u8')))
        self.assertEqual(b, navn.normalize2u8(u'BJørn'))
        self.assertEqual(b, navn.normalize2u8(u'BJØrn'))
        self.assertEqual(b'Geir-Arne', navn.normalize2u8(u'geir-arne'))

    def test_normalize_uni(self):
        "Normalization tests."
        b = u'Bjørn'.encode('u8')
        self.assertEqual(u'Bjørn', navn.normalize2uni(b))

    def test_shorten_fname(self):
        "Shorten first name."
        self.assertEqual(u'Bjørn S', navn.shorten_fname(12, u'Bjørn Steinar'))

    def test_shorten_lname(self):
        "Shorten last name."
        self.assertEqual(u'F Pettersen', 
                         navn.shorten_lname(12, u'Fjeld Pettersen'))

    def test_forkort_navn_u8(self):
        "Forkort navn u8"
        self.assertEqual(
            navn.forkort_navn_u8(21, self.fnameu.encode('u8'),
                                     self.lnameu.encode('u8')),
            u' '.join(navn.shorten(21, self.fnameu, self.lnameu)).encode('u8'))
