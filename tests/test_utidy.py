# -*- coding: utf-8 -*-
from __future__ import print_function
from dk.utidy import Utidy


def test_dunder():
    s = u'<br>'
    u = Utidy(s)
    v = Utidy(s, debug=True)
    assert str(u) == repr(u)
    assert not v == 42


def test_basic():
    assert Utidy("<p>a</p>") == """
    <p>
        a
    </p>
    """


def test_self_closing():
    assert Utidy("<p><br></p>") == """
    <p>
        <br>
    </p>
    """


def test_attributes():
    assert Utidy("<p class='foo' style='color:red' foo=bar>a</p>") == """
    <p class="foo" foo="bar" style="color:red;">
        a
    </p>"""


def test_utidy_spacing_ordering():
    assert Utidy('<tag z="3" a="1" b="2"></tag>') == Utidy('''
        <tag a='1' z='3' b='2'>
        </tag>
    ''')
    assert Utidy('<div style="height :50px;width :30px"></div>') == Utidy('''
        <div style="width: 30px; height: 50px;"></div>
    ''')


def test_simplify():
    ua = Utidy("<h1>a</h1>", simplify=True, debug=True)
    assert ua == "<h1>a</h1>"


def test_regr1():
    assert Utidy('''
        <select class="form-control" tabindex="5">
        <option value="dag"> dag </option>
    <option value="1"> 1 </option><option value="2"> 2 </option><option value="3"> 3 </option><option value="4"> 4 </option><option value="5"> 5 </option><option value="6"> 6 </option><option value="7"> 7 </option><option value="8"> 8 </option><option value="9"> 9 </option><option value="10"> 10 </option><option value="11"> 11 </option><option value="12"> 12 </option><option value="13"> 13 </option><option value="14"> 14 </option><option value="15"> 15 </option><option value="16"> 16 </option><option value="17"> 17 </option><option value="18"> 18 </option><option value="19"> 19 </option><option selected="selected" value="20"> 20 </option><option value="21"> 21 </option><option value="22"> 22 </option><option value="23"> 23 </option><option value="24"> 24 </option><option value="25"> 25 </option><option value="26"> 26 </option><option value="27"> 27 </option><option value="28"> 28 </option><option value="29"> 29 </option><option value="30"> 30 </option><option value="31"> 31 </option></select>
    &nbsp;/&nbsp;
    <selectclass="form-control" tabindex="5">
        <option> mnd </option>
    <option selected="selected" value="1"> 1-jan </option>
<option value="2"> 2-feb </option>
<option value="3"> 3-mar </option>
<option value="4"> 4-apr </option>
<option value="5"> 5-mai </option>
<option value="6"> 6-jun </option>
<option value="7"> 7-jul </option>
<option value="8"> 8-aug </option>
<option value="9"> 9-sep </option>
<option value="10"> 10-okt </option>
<option value="11"> 11-nov </option>
<option value="12"> 12-des </option>
</select>
''') == ""
