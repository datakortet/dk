from dk.collections import invdict


def test_invdict():
    assert -invdict({'key': 'val'}) == {'val': 'key'}
