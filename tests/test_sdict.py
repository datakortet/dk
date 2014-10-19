from dk.collections import sdict


def test_sdict():
    x = sdict()
    x['a'] = 43
    x['b'] = 'foo'

    assert x.keys() == ['a', 'b']
    assert x.values() == [43, 'foo']
    assert list(x) == [('a', 43), ('b', 'foo')]
