import textwrap
from dk.grid import grid


def _s(g):
    return textwrap.dedent(str(g)).strip()


def test_grid1():
    t = grid(emptyval=0)
    t[1, 1] = 42
    assert _s(t) == _s('''
        0  0
        0 42
    ''')
    t[0, :] = 1
    assert _s(t) == _s('''
        1  1
        0 42
    ''')
    t[:, -1] = 'x'
    assert _s(t) == _s('''
        1 x
        0 x
    ''')


def test_copy():
    t = grid(emptyval=0)
    t[1, 1] = 42
    t2 = grid.copy(t, lambda orig, (y, x): orig[y, x] / 2)
    assert _s(t2) == _s('''
        0  0
        0 21
    ''')


def test_repr():
    t = grid(emptyval=0)
    t[1, 1] = 42
    assert _s(repr(t)) == _s('''
        0  0
        0 42
    ''')


def test_insert_row():
    t = grid(emptyval=0)
    t[1, 1] = 42
    t.insert_row(1)
    assert _s(t) == _s('''
        0  0
        0  0
        0 42
    ''')


def test_remove_row():
    t = grid(emptyval=0)
    t[2, 2] = 42
    assert _s(t) == _s('''
        0 0  0
        0 0  0
        0 0 42
    ''')
    t.remove_row(1)
    assert _s(t) == _s('''
        0 0  0
        0 0 42
    ''')


def test_insert_col():
    t = grid(emptyval=0)
    t[1, 1] = 42
    t.insert_col(1)
    assert _s(t) == _s('''
        0 0  0
        0 0 42
    ''')


def test_remove_col():
    t = grid(emptyval=0)
    t[2, 2] = 42
    assert _s(t) == _s('''
        0 0  0
        0 0  0
        0 0 42
    ''')
    t.remove_col(1)
    assert _s(t) == _s('''
        0  0
        0  0
        0 42
    ''')


def test_purge():
    t = grid(emptyval=0)
    t[2, 2] = 42
    assert _s(t) == _s('''
        0 0  0
        0 0  0
        0 0 42
    ''')
    t.purge()
    assert _s(t) == _s('''
         0
        42
    ''')


def test_sum():
    t = grid(emptyval=0)
    for i in range(3):
        for j in range(3):
            t[i, j] = i + j
    assert _s(t) == _s('''
        0 1 2
        1 2 3
        2 3 4
    ''')
    assert sum(t[:, :]) == 18
