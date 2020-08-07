# -*- coding: utf-8 -*-
import sys
from builtins import str as text
from dk.html.uhtml import *
from dk.html import uhtml


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


def test_attribute_functions():
    assert plain_attribute('foo')
    assert not plain_attribute('&')
    assert quote_xhtml('hello') == '"hello"'
    assert quote_xhtml('"hi"') == '"&quot;hi&quot;"'
    assert quote_smart('"hi"') == """'"hi"'"""
    # s = ""
    # s += '"'
    # s += "'"
    # assert quote_smart(s) == "&quot;'"

    assert quote_if_needed('v') == "v"
    assert quote_if_needed('&1') == '"&1"'


def test_make_unicode():
    assert 1
    assert make_unicode(EmptyString) == EmptyString
    assert make_unicode(u'') == u''
    assert make_unicode('') == u''
    assert (make_unicode(b'')) == u''


def test_caption():
    assert text(uhtml.figure(
        uhtml.img(),
        uhtml.figcaption('hello')
    )) == "<figure><img><figcaption>hello</figcaption></figure>\n"

    # XXX figcaption should disappear here...
    assert text(uhtml.figure(
        uhtml.img(),
        uhtml.figcaption()
    )) == "<figure><img><figcaption></figcaption></figure>\n"


def test_tags():
    assert text(uhtml.a('a', b='c')) == u'<a b="c">a</a>'
    assert text(uhtml.abbr('a', b='c')) == u'<abbr b="c">a</abbr>'
    assert text(uhtml.acronym('a', b='c')) == u'<acronym b="c">a</acronym>'
    assert text(uhtml.address('a', b='c')) == u'<address b="c">a</address>'
    assert text(uhtml.applet('a', b='c')) == u'<applet b="c">a</applet>'
    assert text(uhtml.area('a', b='c')) == u'<area b="c">a</area>'
    assert text(uhtml.b('a', b='c')) == u'<b b="c">a</b>'
    assert text(uhtml.base('a', b='c')) == u'<base b="c">a</base>'
    assert text(uhtml.bsefont('a', b='c')) == u'<bsefont b="c">a</bsefont>'
    assert text(uhtml.bdo('a', b='c')) == u'<bdo b="c">a</bdo>'
    assert text(uhtml.big('a', b='c')) == u'<big b="c">a</big>'
    assert text(uhtml.blockquote('a', b='c')) == u'<blockquote b="c">a</blockquote>\n'
    assert text(uhtml.body('a', b='c')) == u'<body b="c">a</body>\n'
    assert text(uhtml.button('a', b='c')) == u'<button b="c">a</button>'
    assert text(uhtml.center('a', b='c')) == u'<center b="c">a</center>\n'
    assert text(uhtml.cite('a', b='c')) == u'<cite b="c">a</cite>'
    assert text(uhtml.code('a', b='c')) == u'<code b="c">a</code>'
    assert text(uhtml.colgroup('a', b='c')) == u'<colgroup b="c">a</colgroup>\n'
    assert text(uhtml.dd('a', b='c')) == u'<dd b="c">a</dd>'
    assert text(uhtml.dfn('a', b='c')) == u'<dfn b="c">a</dfn>'
    assert text(uhtml.div('a', b='c')) == u'<div b="c">a</div>\n'
    assert text(uhtml.dl('a', b='c')) == u'<dl b="c">a</dl>\n'
    assert text(uhtml.dt('a', b='c')) == u'<dt b="c">a</dt>\n'
    assert text(uhtml.em('a', b='c')) == u'<em b="c">a</em>'
    assert text(uhtml.fieldset('a', b='c')) == u'<fieldset b="c">a</fieldset>\n'
    assert text(uhtml.font('a', b='c')) == u'<font b="c">a</font>'
    assert text(uhtml.form('a', b='c')) == u'<form b="c">a</form>\n'
    assert text(uhtml.frame('a', b='c')) == u'<frame b="c">a</frame>\n'
    assert text(uhtml.frameset('a', b='c')) == u'<frameset b="c">a</frameset>'
    assert text(uhtml.h1('a', b='c')) == u'<h1 b="c">a</h1>\n'
    assert text(uhtml.h2('a', b='c')) == u'<h2 b="c">a</h2>\n'
    assert text(uhtml.h3('a', b='c')) == u'<h3 b="c">a</h3>\n'
    assert text(uhtml.h4('a', b='c')) == u'<h4 b="c">a</h4>\n'
    assert text(uhtml.h5('a', b='c')) == u'<h5 b="c">a</h5>\n'
    assert text(uhtml.h6('a', b='c')) == u'<h6 b="c">a</h6>\n'
    assert text(uhtml.head('a', b='c')) == u'<head b="c">a</head>\n'
    assert text(uhtml.html('a', b='c')) == u'<html b="c">a</html>\n'
    assert text(uhtml.i('a', b='c')) == u'<i b="c">a</i>'
    assert text(uhtml.iframe('a', b='c')) == u'<iframe b="c">a</iframe>\n'
    assert text(uhtml.ins('a', b='c')) == u'<ins b="c">a</ins>'
    assert text(uhtml.kbd('a', b='c')) == u'<kbd b="c">a</kbd>'
    assert text(uhtml.label('a', b='c')) == u'<label b="c">a</label>'
    assert text(uhtml.li('a', b='c')) == u'<li b="c">a</li>\n'
    assert text(uhtml.map('a', b='c')) == u'<map b="c">a</map>'
    assert text(uhtml.menu('a', b='c')) == u'<menu b="c">a</menu>'
    assert text(uhtml.nobr('a', b='c')) == u'<nobr b="c">a</nobr>'
    assert text(uhtml.noframes('a', b='c')) == u'<noframes b="c">a</noframes>'
    assert text(uhtml.noscript('a', b='c')) == u'<noscript b="c">a</noscript>'
    assert text(uhtml.ol('a', b='c')) == u'<ol b="c">a</ol>\n'
    assert text(uhtml.optgroup('a', b='c')) == u'<optgroup b="c">a</optgroup>'
    assert text(uhtml.option('a', b='c')) == u'<option b="c">a</option>\n'
    assert text(uhtml.p('a', b='c')) == u'<p b="c">a</p>\n'
    assert text(uhtml.param('a', b='c')) == u'<param b="c">a</param>'
    assert text(uhtml.pre('a', b='c')) == u'<pre b="c">a</pre>\n'
    assert text(uhtml.q('a', b='c')) == u'<q b="c">a</q>'
    assert text(uhtml.s('a', b='c')) == u'<s b="c">a</s>'
    assert text(uhtml.samp('a', b='c')) == u'<samp b="c">a</samp>'
    assert text(uhtml.small('a', b='c')) == u'<small b="c">a</small>'
    assert text(uhtml.span('a', b='c')) == u'<span b="c">a</span>'
    assert text(uhtml.strike('a', b='c')) == u'<strike b="c">a</strike>'
    assert text(uhtml.strong('a', b='c')) == u'<strong b="c">a</strong>'
    assert text(uhtml.sub('a', b='c')) == u'<sub b="c">a</sub>'
    assert text(uhtml.sup('a', b='c')) == u'<sup b="c">a</sup>'
    assert text(uhtml.table('a', b='c')) == u'<table b="c">a</table>\n'
    assert text(uhtml.tbody('a', b='c')) == u'<tbody b="c">a</tbody>\n'
    assert text(uhtml.td('a', b='c')) == u'<td b="c">a</td>'
    assert text(uhtml.textarea('a', b='c')) == u'<textarea b="c">a</textarea>'
    assert text(uhtml.tfoot('a', b='c')) == u'<tfoot b="c">a</tfoot>'
    assert text(uhtml.th('a', b='c')) == u'<th b="c">a</th>'
    assert text(uhtml.thead('a', b='c')) == u'<thead b="c">a</thead>'
    assert text(uhtml.title('a', b='c')) == u'<title b="c">a</title>\n'
    assert text(uhtml.tr('a', b='c')) == u'<tr b="c">a</tr>\n'
    assert text(uhtml.tt('a', b='c')) == u'<tt b="c">a</tt>'
    assert text(uhtml.u('a', b='c')) == u'<u b="c">a</u>'
    assert text(uhtml.ul('a', b='c')) == u'<ul b="c">a</ul>\n'
    assert text(uhtml.var('a', b='c')) == u'<var b="c">a</var>'


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

