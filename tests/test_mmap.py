from dk.collections import mmap


def test_mmap():
    x = mmap(a=1, b=2)
    assert list(x['a']) == [1]
    x['a'] = 42
    assert list(x['a']) == [1, 42]
