# -*- coding: utf-8 -*-

from dk import asciify as an


def test_asciify():
    assert an.asciify(u'a    b') == 'a    b'
    assert an.asciify(u'a    b', spaces='-') == 'a-b'
    assert an.asciify(u'Hårek') == 'Harek'
    

def test_ascii_name():
    """Test of ascii_name function that converts a unicode string to an
       ascii-string that can be used in a filename.
    """
    assert an.ascii_name(u'Hårek den 1 hærlîge') == 'harek-den-haerlige'
    assert an.ascii_name(u'Bàmsetê brüsk') == 'bamsete-brusk'
    assert an.ascii_name(u'krÜséndó krÿg') == u'krusendo-kryg'


def test_slug():
    """Test of slug function that converts a unicode string to an
       ascii-string that can be used in an URI.
    """
    assert an.slug(u'Hårek den 1 hærlîge') == 'harek-den-1-haerlige'
