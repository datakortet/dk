# -*- coding: utf-8 -*-
from dk.html.html import *
from dk.html import html


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
    # assert tag('A', xchecked=False) == '<A xchecked="False"></A>'
    assert tag('A', style=css(height=50)) == '<A style="height:50"></A>'
    assert tag('A', foo=EmptyString) == '<A foo=""></A>'


def test_caption():
    assert html.figure(
        html.img(),
        html.figcaption('hello')
    ) == "<figure><img><figcaption>hello</figcaption></figure>\n"


def test_empty_caption():
    assert html.figure(
        html.img(),
        html.figcaption()
    ) == "<figure><img></figure>\n"


def test_flatten():
    a = tag('A')
    b = tag('B', a)
    t = tag('T', a, b, ['e', 'f'], c="d")
    assert t == str(t)


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
    htmlval = html.a(u'bjørn', href=u'url')
    assert str(htmlval) == '<a href="url">bjørn</a>'
    assert htmlval == '<a href="url">bjørn</a>'


# try:
#     unicode
# except NameError:
#     unicode = str

def test_tags():
    assert html.a('a', b='c') == '<a b="c">a</a>'
    assert html.abbr('a', b='c') == '<abbr b="c">a</abbr>'
    assert html.acronym('a', b='c') == '<acronym b="c">a</acronym>'
    assert html.address('a', b='c') == '<address b="c">a</address>'
    assert html.applet('a', b='c') == '<applet b="c">a</applet>'
    assert html.area('a', b='c') == '<area b="c">a</area>'
    assert html.b('a', b='c') == '<b b="c">a</b>'
    assert html.base('a', b='c') == '<base b="c">a</base>'
    assert html.bsefont('a', b='c') == '<bsefont b="c">a</bsefont>'
    assert html.bdo('a', b='c') == '<bdo b="c">a</bdo>'
    assert html.big('a', b='c') == '<big b="c">a</big>'
    assert html.blockquote('a', b='c') == '<blockquote b="c">a</blockquote>\n'
    assert html.body('a', b='c') == '<body b="c">a</body>\n'
    assert html.button('a', b='c') == '<button b="c">a</button>'
    assert html.center('a', b='c') == '<center b="c">a</center>\n'
    assert html.cite('a', b='c') == '<cite b="c">a</cite>'
    assert html.code('a', b='c') == '<code b="c">a</code>'
    assert html.colgroup('a', b='c') == '<colgroup b="c">a</colgroup>\n'
    assert html.dd('a', b='c') == '<dd b="c">a</dd>'
    assert html.dfn('a', b='c') == '<dfn b="c">a</dfn>'
    assert html.div('a', b='c') == '<div b="c">a</div>\n'
    assert html.dl('a', b='c') == '<dl b="c">a</dl>\n'
    assert html.dt('a', b='c') == '<dt b="c">a</dt>\n'
    assert html.em('a', b='c') == '<em b="c">a</em>'
    assert html.fieldset('a', b='c') == '<fieldset b="c">a</fieldset>\n'
    assert html.font('a', b='c') == '<font b="c">a</font>'
    assert html.form('a', b='c') == '<form b="c">a</form>\n'
    assert html.frame('a', b='c') == '<frame b="c">a</frame>\n'
    assert html.frameset('a', b='c') == '<frameset b="c">a</frameset>'
    assert html.h1('a', b='c') == '<h1 b="c">a</h1>\n'
    assert html.h2('a', b='c') == '<h2 b="c">a</h2>\n'
    assert html.h3('a', b='c') == '<h3 b="c">a</h3>\n'
    assert html.h4('a', b='c') == '<h4 b="c">a</h4>\n'
    assert html.h5('a', b='c') == '<h5 b="c">a</h5>\n'
    assert html.h6('a', b='c') == '<h6 b="c">a</h6>\n'
    assert html.head('a', b='c') == '<head b="c">a</head>\n'
    assert html.html('a', b='c') == '<html b="c">a</html>\n'
    assert html.i('a', b='c') == '<i b="c">a</i>'
    assert html.iframe('a', b='c') == '<iframe b="c">a</iframe>\n'
    assert html.ins('a', b='c') == '<ins b="c">a</ins>'
    assert html.kbd('a', b='c') == '<kbd b="c">a</kbd>'
    assert html.label('a', b='c') == '<label b="c">a</label>'
    assert html.li('a', b='c') == '<li b="c">a</li>\n'
    assert html.map('a', b='c') == '<map b="c">a</map>'
    assert html.menu('a', b='c') == '<menu b="c">a</menu>'
    assert html.nobr('a', b='c') == '<nobr b="c">a</nobr>'
    assert html.noframes('a', b='c') == '<noframes b="c">a</noframes>'
    assert html.noscript('a', b='c') == '<noscript b="c">a</noscript>'
    assert html.ol('a', b='c') == '<ol b="c">a</ol>\n'
    assert html.optgroup('a', b='c') == '<optgroup b="c">a</optgroup>'
    assert html.option('a', b='c') == '<option b="c">a</option>\n'
    assert html.p('a', b='c') == '<p b="c">a</p>\n'
    assert html.param('a', b='c') == '<param b="c">a</param>'
    assert html.pre('a', b='c') == '<pre b="c">a</pre>\n'
    assert html.q('a', b='c') == '<q b="c">a</q>'
    assert html.s('a', b='c') == '<s b="c">a</s>'
    assert html.samp('a', b='c') == '<samp b="c">a</samp>'
    assert html.small('a', b='c') == '<small b="c">a</small>'
    assert html.span('a', b='c') == '<span b="c">a</span>'
    assert html.strike('a', b='c') == '<strike b="c">a</strike>'
    assert html.strong('a', b='c') == '<strong b="c">a</strong>'
    assert html.sub('a', b='c') == '<sub b="c">a</sub>'
    assert html.sup('a', b='c') == '<sup b="c">a</sup>'
    assert html.table('a', b='c') == '<table b="c">a</table>\n'
    assert html.tbody('a', b='c') == '<tbody b="c">a</tbody>\n'
    assert html.td('a', b='c') == '<td b="c">a</td>'
    assert html.textarea('a', b='c') == '<textarea b="c">a</textarea>'
    assert html.tfoot('a', b='c') == '<tfoot b="c">a</tfoot>'
    assert html.th('a', b='c') == '<th b="c">a</th>'
    assert html.thead('a', b='c') == '<thead b="c">a</thead>'
    assert html.title('a', b='c') == '<title b="c">a</title>\n'
    assert html.tr('a', b='c') == '<tr b="c">a</tr>\n'
    assert html.tt('a', b='c') == '<tt b="c">a</tt>'
    assert html.u('a', b='c') == '<u b="c">a</u>'
    assert html.ul('a', b='c') == '<ul b="c">a</ul>\n'
    assert html.var('a', b='c') == '<var b="c">a</var>'


def test_escape_char():
    from dk.html.html import escape_char, escaped_array, escape

    assert escape_char(u'&oslash;') == '&oslash;'
    assert escape_char(u'ø') == '&oslash;'
    assert escaped_array(u'hi') == ['h', 'i']
    assert escape(u'bjørn') == 'bj&oslash;rn'


def test_attribute_functions():
    from dk.html.html import plain_attribute, quote_xhtml, quote_smart, quote_if_needed

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
    assert make_unicode(EmptyString) == EmptyString
    assert make_unicode(u'') == u''
    assert make_unicode('') == u''
    assert make_unicode(b'') == u''
    assert make_unicode(42) == u'42'


def test_old_doctest():
    assert str(html.br()) == '<br>'
    assert str(html.div('hello', html.b('world'))) == '<div>hello<b>world</b></div>\n'
    print(select(options=[u'a', u'b'], name='foo'))
    assert str(select(options=[u'a', u'b'], name='foo')) == (
        '<select id="id_foo" name="foo">'
        '<option value="a">a</option>\n'
        '<option value="b">b</option>\n'
        '</select>'
    )


def test_lines():
    assert lines('a', 'b') == 'a<br>b'


# def test_text_grouping():
#     assert text_grouping('a', 'b') == 'ab'
