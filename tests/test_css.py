from dk.html.css import css


def test_css():
    # the str here is bytes on py2 and unicode on py3

    x = css(color='red', background='blue')
    print("X: %r" % str(x))
    assert str(x) == 'background:blue;color:red'

    x.border = 'none'
    y = css(background='blue', color='red')
    y.border = 'none'
    assert x == y

    a = css()
    a['font-weight'] = 'bold'
    print("FWB: %r" % str(a))
    assert str(a) == 'font-weight:bold'

    a.text_align = 'right'
    assert str(a) == 'font-weight:bold;text-align:right'
