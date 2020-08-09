# -*- coding: utf-8 -*-
import sys

import pytest
from builtins import str as text
from dk.html.uhtml import *
from dk.html import uhtml


def test_to_html():
    assert to_html(42) == u'42'
    assert to_html(b'hi') == u'hi'


def test_escape_char():
    assert escape_char(u'&oslash;') == u'&oslash;'
    assert escape_char(u'ø') == u'&oslash;'
    if sys.version_info.major >= 3:
        assert escape_char(u'👍') == u''
    assert escaped_array(u'hi') == [u'h', u'i']
    assert escape(u'bjørn') == u'bj&oslash;rn'
    assert escape(u'bjørn'.encode('u8'), 'u8') == u'bj&oslash;rn'
    assert escape(None) == u''
    assert u8escape(u'bjørn'.encode('u8')) == u'bj&oslash;rn'
    assert unescape(u'bj&oslash;rn') == u'bjørn'
    assert unescape(b'bj&oslash;rn') == u'bjørn'


def test_normalize():
    assert normalize(u'Bjørn') == u'Bjørn'
    assert normalize(u'Bjørn'.encode('u8')) == u'Bjørn'
    assert normalize(u'Bjørn'.encode('iso-8859-1')) == u'Bjørn'
    assert normalize(u'€'.encode('iso-8859-15')) != u'€'
    assert normalize(b'\0') == u'\x00'


def test_attribute_functions():
    assert plain_attribute('foo')
    assert not plain_attribute('&')
    assert quote_xhtml('hello') == '"hello"'
    assert quote_xhtml('"hi"') == '"&quot;hi&quot;"'
    assert quote_smart('"hi"') == """'"hi"'"""
    assert quote_smart('''
    "it's"
    '''.strip()) == "'&quot;it's&quot;'"
    assert norm_attr_name('foo') == 'foo'
    assert norm_attr_name('foo_') == 'foo'
    assert norm_attr_name('foo_bar') == 'foo-bar'
    assert quote_if_needed('v') == "v"
    assert quote_if_needed('&1') == '"&1"'


def test_make_unicode():
    assert make_unicode(EmptyString) == EmptyString
    assert make_unicode(u'') == u''
    assert make_unicode('') == u''
    assert make_unicode(b'') == u''
    assert make_unicode(42) == u'42'


def test_eq():
    assert tag('T') == '<T></T>'
    assert tag('T') != 42


def test_tag_methods():
    t = tag('T')
    t.foo = 'bar'
    assert t.foo == 'bar'
    assert t == '<T foo="bar"></T>'
    assert stag('B') == '<B>'


def test_caption():
    assert uhtml.figure(
        uhtml.img(),
        uhtml.figcaption('hello')
    ) == "<figure><img><figcaption>hello</figcaption></figure>\n"


def test_empty_caption():
    assert uhtml.figure(
        uhtml.img(),
        uhtml.figcaption()
    ) == "<figure><img></figure>\n"


def test_flatten():
    a = tag('A')
    b = tag('B', a)
    t = tag('T', a, b, ['e', 'f'], c="d")
    # print("str?:", t)
    # print("_unicode:", t._as_unicode())
    # print("__html__:", t.__html__())
    assert t == to_html(t)


def test_flatten_d():
    a = dtag('A')
    b = tag('B', a)
    assert b == "<B></B>"
    assert a == ""


def test_dtag():
    a = dtag("A", 'a')
    assert a == "<A>a</A>"
    b = dtag("B")
    assert b == ""


def test_simple_tag():
    htmlval = uhtml.a(u'bjørn', href=u'url')
    assert htmlval == '<a href="url">bjørn</a>'
    assert str(htmlval) == '<a href="url">bjørn</a>'


def test_tags():
    assert str(uhtml.abbr('a', b='c')) == '<abbr b="c">a</abbr>'
    assert str(uhtml.acronym('a', b='c')) == '<acronym b="c">a</acronym>'
    assert str(uhtml.address('a', b='c')) == '<address b="c">a</address>'
    assert str(uhtml.applet('a', b='c')) == '<applet b="c">a</applet>'
    assert str(uhtml.area('a', b='c')) == '<area b="c">a</area>'
    assert str(uhtml.b('a', b='c')) == '<b b="c">a</b>'
    assert str(uhtml.base('a', b='c')) == '<base b="c">a</base>'
    assert str(uhtml.bsefont('a', b='c')) == '<bsefont b="c">a</bsefont>'
    assert str(uhtml.bdo('a', b='c')) == '<bdo b="c">a</bdo>'
    assert str(uhtml.big('a', b='c')) == '<big b="c">a</big>'
    assert str(uhtml.blockquote('a', b='c')) == '<blockquote b="c">a</blockquote>\n'
    assert str(uhtml.body('a', b='c')) == '<body b="c">a</body>\n'
    assert str(uhtml.button('a', b='c')) == '<button b="c">a</button>'
    assert str(uhtml.center('a', b='c')) == '<center b="c">a</center>\n'
    assert str(uhtml.cite('a', b='c')) == '<cite b="c">a</cite>'
    assert str(uhtml.code('a', b='c')) == '<code b="c">a</code>'
    assert str(uhtml.colgroup('a', b='c')) == '<colgroup b="c">a</colgroup>\n'
    assert str(uhtml.dd('a', b='c')) == '<dd b="c">a</dd>'
    assert str(uhtml.dfn('a', b='c')) == '<dfn b="c">a</dfn>'
    assert str(uhtml.div('a', b='c')) == '<div b="c">a</div>\n'
    assert str(uhtml.dl('a', b='c')) == '<dl b="c">a</dl>\n'
    assert str(uhtml.dt('a', b='c')) == '<dt b="c">a</dt>\n'
    assert str(uhtml.em('a', b='c')) == '<em b="c">a</em>'
    assert str(uhtml.fieldset('a', b='c')) == '<fieldset b="c">a</fieldset>\n'
    assert str(uhtml.font('a', b='c')) == '<font b="c">a</font>'
    assert str(uhtml.form('a', b='c')) == '<form b="c">a</form>\n'
    assert str(uhtml.frame('a', b='c')) == '<frame b="c">a</frame>\n'
    assert str(uhtml.frameset('a', b='c')) == '<frameset b="c">a</frameset>'
    assert str(uhtml.h1('a', b='c')) == '<h1 b="c">a</h1>\n'
    assert str(uhtml.h2('a', b='c')) == '<h2 b="c">a</h2>\n'
    assert str(uhtml.h3('a', b='c')) == '<h3 b="c">a</h3>\n'
    assert str(uhtml.h4('a', b='c')) == '<h4 b="c">a</h4>\n'
    assert str(uhtml.h5('a', b='c')) == '<h5 b="c">a</h5>\n'
    assert str(uhtml.h6('a', b='c')) == '<h6 b="c">a</h6>\n'
    assert str(uhtml.head('a', b='c')) == '<head b="c">a</head>\n'
    assert str(uhtml.html('a', b='c')) == '<html b="c">a</html>\n'
    assert str(uhtml.i('a', b='c')) == '<i b="c">a</i>'
    assert str(uhtml.iframe('a', b='c')) == '<iframe b="c">a</iframe>\n'
    assert str(uhtml.ins('a', b='c')) == '<ins b="c">a</ins>'
    assert str(uhtml.kbd('a', b='c')) == '<kbd b="c">a</kbd>'
    assert str(uhtml.label('a', b='c')) == '<label b="c">a</label>'
    assert str(uhtml.li('a', b='c')) == '<li b="c">a</li>\n'
    assert str(uhtml.map('a', b='c')) == '<map b="c">a</map>'
    assert str(uhtml.menu('a', b='c')) == '<menu b="c">a</menu>'
    assert str(uhtml.nobr('a', b='c')) == '<nobr b="c">a</nobr>'
    assert str(uhtml.noframes('a', b='c')) == '<noframes b="c">a</noframes>'
    assert str(uhtml.noscript('a', b='c')) == '<noscript b="c">a</noscript>'
    assert str(uhtml.ol('a', b='c')) == '<ol b="c">a</ol>\n'
    assert str(uhtml.optgroup('a', b='c')) == '<optgroup b="c">a</optgroup>'
    assert str(uhtml.option('a', b='c')) == '<option b="c">a</option>\n'
    assert str(uhtml.p('a', b='c')) == '<p b="c">a</p>\n'
    assert str(uhtml.param('a', b='c')) == '<param b="c">a</param>'
    assert str(uhtml.pre('a', b='c')) == '<pre b="c">a</pre>\n'
    assert str(uhtml.q('a', b='c')) == '<q b="c">a</q>'
    assert str(uhtml.s('a', b='c')) == '<s b="c">a</s>'
    assert str(uhtml.samp('a', b='c')) == '<samp b="c">a</samp>'
    assert str(uhtml.small('a', b='c')) == '<small b="c">a</small>'
    assert str(uhtml.span('a', b='c')) == '<span b="c">a</span>'
    assert str(uhtml.strike('a', b='c')) == '<strike b="c">a</strike>'
    assert str(uhtml.strong('a', b='c')) == '<strong b="c">a</strong>'
    assert str(uhtml.sub('a', b='c')) == '<sub b="c">a</sub>'
    assert str(uhtml.sup('a', b='c')) == '<sup b="c">a</sup>'
    assert str(uhtml.table('a', b='c')) == '<table b="c">a</table>\n'
    assert str(uhtml.tbody('a', b='c')) == '<tbody b="c">a</tbody>\n'
    assert str(uhtml.td('a', b='c')) == '<td b="c">a</td>'
    assert str(uhtml.textarea('a', b='c')) == '<textarea b="c">a</textarea>'
    assert str(uhtml.tfoot('a', b='c')) == '<tfoot b="c">a</tfoot>'
    assert str(uhtml.th('a', b='c')) == '<th b="c">a</th>'
    assert str(uhtml.thead('a', b='c')) == '<thead b="c">a</thead>'
    assert str(uhtml.title('a', b='c')) == '<title b="c">a</title>\n'
    assert str(uhtml.tr('a', b='c')) == '<tr b="c">a</tr>\n'
    assert str(uhtml.tt('a', b='c')) == '<tt b="c">a</tt>'
    assert str(uhtml.u('a', b='c')) == '<u b="c">a</u>'
    assert str(uhtml.ul('a', b='c')) == '<ul b="c">a</ul>\n'
    assert str(uhtml.var('a', b='c')) == '<var b="c">a</var>'


def test_old_doctest():
    assert str(uhtml.br()) == '<br>'
    assert str(uhtml.div('hello', uhtml.b('world'))) == '<div>hello<b>world</b></div>\n'
    print(select(options=[u'a', u'b'], name='foo'))
    assert str(select(options=[u'a', u'b'], name='foo')) == (
        '<select id="id_foo" name="foo">'
        '<option value="a">a</option>\n'
        '<option value="b">b</option>\n'
        '</select>'
    )


def test_lines():
    assert lines('a', 'b') == 'a<br>b'


def test_text_grouping():
    assert text_grouping('a', 'b') == 'ab'
