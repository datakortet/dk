from dk.proxy import proxy


def test_int_proxy():
    v = 42
    p = proxy(v)
    assert p.bit_length() == v.bit_length()
    assert repr(p) == 'proxy(%s)' % v
    assert hex(p) == hex(v)
    assert oct(p) == oct(v)
    assert hash(p) == hash(v)
    assert p < 43
    assert p <= 42
    assert p == 42
    assert p != 43
    assert p > 41
    assert p >= 42
    assert p + 1 == 43
    assert type(p + 1) == int
    assert 1 + p == 43
    assert type(1 + p) == int
    assert abs(p) == abs(v)
    assert 84 / p == 2
    assert p / 2 == 21
    assert p // 2 == 21
    # assert 84 // p == 2
    assert p - 1 == 41
    assert 43 - p == 1
    assert p % 10 == v % 10
    assert -p == -v
    assert +p == +v
    assert p ** 2 == v ** 2
    assert 2 ** p == 2 ** v


def test_imeth():
    p = proxy(42)
    p += 1
    assert p == 43
    p -= 1
    assert p == 42
    p *= 2
    assert p == 84
    p /= 2
    assert p == 42


def test_binary_proxy():
    v = 2
    p = proxy(v)
    # assert (~p) == (~v)
    assert p << 3 == v << 3
    assert 3 << p == 3 << v
    assert p >> 1 == v >> 1
    # assert 16 >> p == 16 >> v
    # assert p | 1 == 0
    assert p ^ 2 == v ^ 2
    assert p & 2 == v & 2


def test_bool_proxy():
    v = True
    p = proxy(v)

    assert (not p) == (not v)
    assert (p and True) == True
    assert (p and False) == False


def test_list_proxy():
    v = [1, 2, 3]
    p = proxy(v)

    assert len(v) == len(p)
    assert list(iter(v)) == list(iter(p))
    assert (2 in p) == (2 in v)
    assert p[1] == v[1]

    t = proxy([1, 2, 3])
    del t[1]
    assert t == [1, 3]
    t[1] = 42
    assert t == [1, 42]


def test_str_proxy():
    v = 'hello'
    p = proxy(v)
    assert p * 3 == v * 3
    assert 'x' * proxy(3) == 'xxx'
    assert str(p) == 'hello'


def test_obj_proxy():
    class T(object):
        a = 'a'

    t = T()
    assert t.a == 'a'
    p = proxy(t)
    assert p.a == 'a'
    p.a = 42
    assert p.a == 42
    assert t.a == 42


def test_fn_proxy():
    def v(x):
        return x

    p = proxy(v)

    assert p(42) == v(42)
