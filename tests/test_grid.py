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


def test_nsquared_grid():
    "Test basic assignment"
    g = grid()
    for i in range(5):
        for j in range(5):
            g[i, j] = i + j

    print "G:"
    print dedent(str(g))
    expected = '''\
        0 1 2 3 4
        1 2 3 4 5
        2 3 4 5 6
        3 4 5 6 7
        4 5 6 7 8'''

    assert dedent(str(g)) == dedent(expected)


def test_isomorphic_assign():
    "Test that you can assign areas of the same size to each other."
    g = grid()
    for i in range(5):
        for j in range(5):
            g[i, j] = i + j

    print g
    
    print "G select:"
    print g[1:3, :5]

    print
    print
    print 'h'
    h = grid()
    h[5, 5] = 1
    print h
    print
    assert dedent(str(h)) == dedent('''\
       None None None None None None
       None None None None None None
       None None None None None None
       None None None None None None
       None None None None None None
       None None None None None    1''')
    
    h[2:4, :5] = g[1:3, :5]  # assignment to same shaped area
    print h
    print
    assert dedent(str(h)) == dedent('''\
       None None None None None None
       None None None None None None
          1    2    3    4    5 None
          2    3    4    5    6 None
       None None None None None None
       None None None None None    1''')

    # assign 4 and 2 to rows 1..3 in the last column
    h[1:3, -1] = [4, 2]
    print h
    print
    assert dedent(str(h)) == dedent('''\
       None None None None None None
       None None None None None    4
          1    2    3    4    5    2
          2    3    4    5    6 None
       None None None None None None
       None None None None None    1''')

    # assign range(5) to all rows in the next-to-last column
    h[:, -2] = range(5)
    print h
    print
    assert dedent(str(h)) == dedent('''\
       None None None None    0 None
       None None None None    1    4
          1    2    3    4    2    2
          2    3    4    5    3 None
       None None None None    4 None
       None None None None None    1''')

    # assign the last row of g to the third-to-last *column* of h.
    print "GRange:", g[-1, :]
    h[1:, -3] = g[-1, :]
    print "H (same shape):"
    print h
    assert dedent(str(h)) == dedent('''\
       None None None None    0 None
       None None None    4    1    4
          1    2    3    5    2    2
          2    3    4    6    3 None
       None None None    7    4 None
       None None None    8 None    1''')
