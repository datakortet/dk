# -*- coding: utf-8 -*-
from __future__ import print_function
import textwrap

from dk import utidy


def hcmp(a, b):
    ua = utidy.utidy(a)
    print("UA:", ua)
    ub = textwrap.dedent(b).strip()
    print("UB:", ub)
    return ua == ub


def test_basic():
    assert hcmp("<p>a</p>", """
    <p>
        a
    </p>
    """)


def test_self_closing():
    assert hcmp("<p><br></p>", """
    <p>
        <br>
    </p>
    """)


def test_attributes():
    assert hcmp("<p class='foo' style='color:red' foo=bar>a</p>", """
    <p class="foo" foo="bar" style="color:red;">
        a
    </p>""")


def test_simplify():
    ua = utidy.utidy("<h1>a</h1>", simplify=True)
    assert ua == "<h1>a</h1>"
