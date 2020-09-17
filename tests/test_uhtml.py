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


def test_tag_attributes():
    assert tag('A', checked=True) == '<A checked></A>'
    assert tag('A', checked=False) == '<A></A>'
    assert tag('A', xchecked=False) == '<A xchecked="False"></A>'
    assert tag('A', style=css(height=50)) == '<A style="height:50"></A>'
    assert tag('A', foo=EmptyString) == '<A foo=""></A>'


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
    assert htmlval == u'<a href="url">bjørn</a>'
    # check that str is "sensible" on both pythons
    if sys.version_info.major < 3:
        assert str(htmlval) == u'<a href="url">bjørn</a>'.encode('u8')
    else:
        assert str(htmlval) == '<a href="url">bjørn</a>'
    assert to_html(htmlval) == u'<a href="url">bjørn</a>'


def test_tags():
    assert uhtml.abbr('a', b='c') == '<abbr b="c">a</abbr>'
    assert uhtml.acronym('a', b='c') == '<acronym b="c">a</acronym>'
    assert uhtml.address('a', b='c') == '<address b="c">a</address>'
    assert uhtml.applet('a', b='c') == '<applet b="c">a</applet>'
    assert uhtml.area('a', b='c') == '<area b="c">a</area>'
    assert uhtml.b('a', b='c') == '<b b="c">a</b>'
    assert uhtml.base('a', b='c') == '<base b="c">a</base>'
    assert uhtml.bsefont('a', b='c') == '<bsefont b="c">a</bsefont>'
    assert uhtml.bdo('a', b='c') == '<bdo b="c">a</bdo>'
    assert uhtml.big('a', b='c') == '<big b="c">a</big>'
    assert uhtml.blockquote('a', b='c') == '<blockquote b="c">a</blockquote>\n'
    assert uhtml.body('a', b='c') == '<body b="c">a</body>\n'
    assert uhtml.button('a', b='c') == '<button b="c">a</button>'
    assert uhtml.center('a', b='c') == '<center b="c">a</center>\n'
    assert uhtml.cite('a', b='c') == '<cite b="c">a</cite>'
    assert uhtml.code('a', b='c') == '<code b="c">a</code>'
    assert uhtml.colgroup('a', b='c') == '<colgroup b="c">a</colgroup>\n'
    assert uhtml.dd('a', b='c') == '<dd b="c">a</dd>'
    assert uhtml.dfn('a', b='c') == '<dfn b="c">a</dfn>'
    assert uhtml.div('a', b='c') == '<div b="c">a</div>\n'
    assert uhtml.dl('a', b='c') == '<dl b="c">a</dl>\n'
    assert uhtml.dt('a', b='c') == '<dt b="c">a</dt>\n'
    assert uhtml.em('a', b='c') == '<em b="c">a</em>'
    assert uhtml.fieldset('a', b='c') == '<fieldset b="c">a</fieldset>\n'
    assert uhtml.font('a', b='c') == '<font b="c">a</font>'
    assert uhtml.form('a', b='c') == '<form b="c">a</form>\n'
    assert uhtml.frame('a', b='c') == '<frame b="c">a</frame>\n'
    assert uhtml.frameset('a', b='c') == '<frameset b="c">a</frameset>'
    assert uhtml.h1('a', b='c') == '<h1 b="c">a</h1>\n'
    assert uhtml.h2('a', b='c') == '<h2 b="c">a</h2>\n'
    assert uhtml.h3('a', b='c') == '<h3 b="c">a</h3>\n'
    assert uhtml.h4('a', b='c') == '<h4 b="c">a</h4>\n'
    assert uhtml.h5('a', b='c') == '<h5 b="c">a</h5>\n'
    assert uhtml.h6('a', b='c') == '<h6 b="c">a</h6>\n'
    assert uhtml.head('a', b='c') == '<head b="c">a</head>\n'
    assert uhtml.html('a', b='c') == '<html b="c">a</html>\n'
    assert uhtml.i('a', b='c') == '<i b="c">a</i>'
    assert uhtml.iframe('a', b='c') == '<iframe b="c">a</iframe>\n'
    assert uhtml.ins('a', b='c') == '<ins b="c">a</ins>'
    assert uhtml.kbd('a', b='c') == '<kbd b="c">a</kbd>'
    assert uhtml.label('a', b='c') == '<label b="c">a</label>'
    assert uhtml.li('a', b='c') == '<li b="c">a</li>\n'
    assert uhtml.map('a', b='c') == '<map b="c">a</map>'
    assert uhtml.menu('a', b='c') == '<menu b="c">a</menu>'
    assert uhtml.nobr('a', b='c') == '<nobr b="c">a</nobr>'
    assert uhtml.noframes('a', b='c') == '<noframes b="c">a</noframes>'
    assert uhtml.noscript('a', b='c') == '<noscript b="c">a</noscript>'
    assert uhtml.ol('a', b='c') == '<ol b="c">a</ol>\n'
    assert uhtml.optgroup('a', b='c') == '<optgroup b="c">a</optgroup>'
    assert uhtml.option('a', b='c') == '<option b="c">a</option>\n'
    assert uhtml.p('a', b='c') == '<p b="c">a</p>\n'
    assert uhtml.param('a', b='c') == '<param b="c">a</param>'
    assert uhtml.pre('a', b='c') == '<pre b="c">a</pre>\n'
    assert uhtml.q('a', b='c') == '<q b="c">a</q>'
    assert uhtml.s('a', b='c') == '<s b="c">a</s>'
    assert uhtml.samp('a', b='c') == '<samp b="c">a</samp>'
    assert uhtml.small('a', b='c') == '<small b="c">a</small>'
    assert uhtml.span('a', b='c') == '<span b="c">a</span>'
    assert uhtml.strike('a', b='c') == '<strike b="c">a</strike>'
    assert uhtml.strong('a', b='c') == '<strong b="c">a</strong>'
    assert uhtml.sub('a', b='c') == '<sub b="c">a</sub>'
    assert uhtml.sup('a', b='c') == '<sup b="c">a</sup>'
    assert uhtml.table('a', b='c') == '<table b="c">a</table>\n'
    assert uhtml.tbody('a', b='c') == '<tbody b="c">a</tbody>\n'
    assert uhtml.td('a', b='c') == '<td b="c">a</td>'
    assert uhtml.textarea('a', b='c') == '<textarea b="c">a</textarea>'
    assert uhtml.tfoot('a', b='c') == '<tfoot b="c">a</tfoot>'
    assert uhtml.th('a', b='c') == '<th b="c">a</th>'
    assert uhtml.thead('a', b='c') == '<thead b="c">a</thead>'
    assert uhtml.title('a', b='c') == '<title b="c">a</title>\n'
    assert uhtml.tr('a', b='c') == '<tr b="c">a</tr>\n'
    assert uhtml.tt('a', b='c') == '<tt b="c">a</tt>'
    assert uhtml.u('a', b='c') == '<u b="c">a</u>'
    assert uhtml.ul('a', b='c') == '<ul b="c">a</ul>\n'
    assert uhtml.var('a', b='c') == '<var b="c">a</var>'


def test_old_doctest():
    assert str(uhtml.br()) == '<br>'
    assert str(uhtml.div('hello', uhtml.b('world'))) == '<div>hello<b>world</b></div>\n'
    print(select(options=[u'a', u'b'], name='foo'))


def test_select():
    s = select(options=[u'a', u'ø'], selected=u'ø', name='foo')
    assert str(s) == (
        '<select id="id_foo" name="foo">'
        '<option value="a">a</option>\n'
        '<option selected="selected" value="&oslash;">ø</option>\n'
        '</select>'
    )


def test_select_tuple_nonstring():
    assert str(select(options=[(1, 1)], name='foo')) == (
        '<select id="id_foo" name="foo"><option value="1">1</option>\n</select>'
    )


def test_select_no_options():
    assert str(select(options=[], name='foo')) == (
        '<select id="id_foo" name="foo"></select>'
    )


def xtest_select_selected():
    s = select(options=[(1, 1)], selected=1, name='foo')
    s.selected = 1
    assert s.selected == 1
    assert str(s) == (
        '<select id="id_foo" name="foo"><option selected="selected" value="1">1</option>\n</select>'
    )

def test_lines():
    assert lines('a', 'b') == 'a<br>b'


def test_text_grouping():
    assert text_grouping('a', 'b') == 'ab'
