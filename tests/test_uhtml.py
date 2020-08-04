# -*- coding: utf-8 -*-
from dk.html import uhtml
from dk.html.uhtml import escape_char, escaped_array, escape, u8escape, unescape


# from dk.html.uhtml import plain_attribute, quote_xhtml, quote_smart, \
#     quote_if_needed, norm_attr_name
# from dk.html.uhtml import make_unicode, EmptyString


def test_escape_char():
    assert escape_char(u'&oslash;') == u'&oslash;'
    assert escape_char(u'ø') == u'&oslash;'
    assert escape_char(u'👍') == u''
    assert escaped_array(u'hi') == [u'h', u'i']
    assert escape(u'bjørn') == u'bj&oslash;rn'
    assert escape(u'bjørn'.encode('u8'), 'u8') == u'bj&oslash;rn'
    assert escape(None) == u''
    assert u8escape(u'bjørn'.encode('u8')) == u'bj&oslash;rn'
    assert unescape(u'bj&oslash;rn') == u'bjørn'
    assert unescape(b'bj&oslash;rn') == u'bjørn'

# def test_attribute_functions():
#     assert plain_attribute('foo')
#     assert not plain_attribute('&')
#     assert quote_xhtml('hello') == '"hello"'
#     assert quote_xhtml('"hi"') == '"&quot;hi&quot;"'
#     assert quote_smart('"hi"') == """'"hi"'"""
#     # s = ""
#     # s += '"'
#     # s += "'"
#     # assert quote_smart(s) == "&quot;'"
#
#     assert quote_if_needed('v') == "v"
#     assert quote_if_needed('&1') == '"&1"'
#
#
# def test_make_unicode():
#     assert make_unicode(EmptyString) == EmptyString
#     assert make_unicode(u'') == u''
#     assert make_unicode('') == u''
#     assert (make_unicode(b'')) == u''
#
#
# def test_tags():
#     assert str(unicode(uhtml.a('a', b='c'))) == '<a b="c">a</a>'
#     assert str(unicode(uhtml.abbr('a', b='c'))) == '<abbr b="c">a</abbr>'
#     assert str(
#         unicode(uhtml.acronym('a', b='c'))) == '<acronym b="c">a</acronym>'
#     assert str(
#         unicode(uhtml.address('a', b='c'))) == '<address b="c">a</address>'
#     assert str(
#         unicode(uhtml.applet('a', b='c'))) == '<applet b="c">a</applet>'
#     assert str(unicode(uhtml.area('a', b='c'))) == '<area b="c">a</area>'
#     assert str(unicode(uhtml.b('a', b='c'))) == '<b b="c">a</b>'
#     assert str(unicode(uhtml.base('a', b='c'))) == '<base b="c">a</base>'
#     assert str(
#         unicode(uhtml.bsefont('a', b='c'))) == '<bsefont b="c">a</bsefont>'
#     assert str(unicode(uhtml.bdo('a', b='c'))) == '<bdo b="c">a</bdo>'
#     assert str(unicode(uhtml.big('a', b='c'))) == '<big b="c">a</big>'
#     assert str(unicode(
#         uhtml.blockquote('a', b='c'))) == '<blockquote b="c">a</blockquote>\n'
#     assert str(unicode(uhtml.body('a', b='c'))) == '<body b="c">a</body>\n'
#     assert str(
#         unicode(uhtml.button('a', b='c'))) == '<button b="c">a</button>'
#     assert str(
#         unicode(uhtml.center('a', b='c'))) == '<center b="c">a</center>\n'
#     assert str(unicode(uhtml.cite('a', b='c'))) == '<cite b="c">a</cite>'
#     assert str(unicode(uhtml.code('a', b='c'))) == '<code b="c">a</code>'
#     assert str(unicode(
#         uhtml.colgroup('a', b='c'))) == '<colgroup b="c">a</colgroup>\n'
#     assert str(unicode(uhtml.dd('a', b='c'))) == '<dd b="c">a</dd>'
#     assert str(unicode(uhtml.dfn('a', b='c'))) == '<dfn b="c">a</dfn>'
#     assert str(unicode(uhtml.div('a', b='c'))) == '<div b="c">a</div>\n'
#     assert str(unicode(uhtml.dl('a', b='c'))) == '<dl b="c">a</dl>\n'
#     assert str(unicode(uhtml.dt('a', b='c'))) == '<dt b="c">a</dt>\n'
#     assert str(unicode(uhtml.em('a', b='c'))) == '<em b="c">a</em>'
#     assert str(unicode(
#         uhtml.fieldset('a', b='c'))) == '<fieldset b="c">a</fieldset>\n'
#     assert str(unicode(uhtml.font('a', b='c'))) == '<font b="c">a</font>'
#     assert str(unicode(uhtml.form('a', b='c'))) == '<form b="c">a</form>\n'
#     assert str(unicode(uhtml.frame('a', b='c'))) == '<frame b="c">a</frame>\n'
#     assert str(
#         unicode(uhtml.frameset('a', b='c'))) == '<frameset b="c">a</frameset>'
#     assert str(unicode(uhtml.h1('a', b='c'))) == '<h1 b="c">a</h1>\n'
#     assert str(unicode(uhtml.h2('a', b='c'))) == '<h2 b="c">a</h2>\n'
#     assert str(unicode(uhtml.h3('a', b='c'))) == '<h3 b="c">a</h3>\n'
#     assert str(unicode(uhtml.h4('a', b='c'))) == '<h4 b="c">a</h4>\n'
#     assert str(unicode(uhtml.h5('a', b='c'))) == '<h5 b="c">a</h5>\n'
#     assert str(unicode(uhtml.h6('a', b='c'))) == '<h6 b="c">a</h6>\n'
#     assert str(unicode(uhtml.head('a', b='c'))) == '<head b="c">a</head>\n'
#     assert str(unicode(uhtml.html('a', b='c'))) == '<html b="c">a</html>\n'
#     assert str(unicode(uhtml.i('a', b='c'))) == '<i b="c">a</i>'
#     assert str(
#         unicode(uhtml.iframe('a', b='c'))) == '<iframe b="c">a</iframe>\n'
#     assert str(unicode(uhtml.ins('a', b='c'))) == '<ins b="c">a</ins>'
#     assert str(unicode(uhtml.kbd('a', b='c'))) == '<kbd b="c">a</kbd>'
#     assert str(unicode(uhtml.label('a', b='c'))) == '<label b="c">a</label>'
#     assert str(unicode(uhtml.li('a', b='c'))) == '<li b="c">a</li>\n'
#     assert str(unicode(uhtml.map('a', b='c'))) == '<map b="c">a</map>'
#     assert str(unicode(uhtml.menu('a', b='c'))) == '<menu b="c">a</menu>'
#     assert str(unicode(uhtml.nobr('a', b='c'))) == '<nobr b="c">a</nobr>'
#     assert str(
#         unicode(uhtml.noframes('a', b='c'))) == '<noframes b="c">a</noframes>'
#     assert str(
#         unicode(uhtml.noscript('a', b='c'))) == '<noscript b="c">a</noscript>'
#     assert str(unicode(uhtml.ol('a', b='c'))) == '<ol b="c">a</ol>\n'
#     assert str(
#         unicode(uhtml.optgroup('a', b='c'))) == '<optgroup b="c">a</optgroup>'
#     assert str(
#         unicode(uhtml.option('a', b='c'))) == '<option b="c">a</option>\n'
#     assert str(unicode(uhtml.p('a', b='c'))) == '<p b="c">a</p>\n'
#     assert str(unicode(uhtml.param('a', b='c'))) == '<param b="c">a</param>'
#     assert str(unicode(uhtml.pre('a', b='c'))) == '<pre b="c">a</pre>\n'
#     assert str(unicode(uhtml.q('a', b='c'))) == '<q b="c">a</q>'
#     assert str(unicode(uhtml.s('a', b='c'))) == '<s b="c">a</s>'
#     assert str(unicode(uhtml.samp('a', b='c'))) == '<samp b="c">a</samp>'
#     assert str(unicode(uhtml.small('a', b='c'))) == '<small b="c">a</small>'
#     assert str(unicode(uhtml.span('a', b='c'))) == '<span b="c">a</span>'
#     assert str(
#         unicode(uhtml.strike('a', b='c'))) == '<strike b="c">a</strike>'
#     assert str(
#         unicode(uhtml.strong('a', b='c'))) == '<strong b="c">a</strong>'
#     assert str(unicode(uhtml.sub('a', b='c'))) == '<sub b="c">a</sub>'
#     assert str(unicode(uhtml.sup('a', b='c'))) == '<sup b="c">a</sup>'
#     assert str(unicode(uhtml.table('a', b='c'))) == '<table b="c">a</table>\n'
#     assert str(unicode(uhtml.tbody('a', b='c'))) == '<tbody b="c">a</tbody>\n'
#     assert str(unicode(uhtml.td('a', b='c'))) == '<td b="c">a</td>'
#     assert str(
#         unicode(uhtml.textarea('a', b='c'))) == '<textarea b="c">a</textarea>'
#     assert str(unicode(uhtml.tfoot('a', b='c'))) == '<tfoot b="c">a</tfoot>'
#     assert str(unicode(uhtml.th('a', b='c'))) == '<th b="c">a</th>'
#     assert str(unicode(uhtml.thead('a', b='c'))) == '<thead b="c">a</thead>'
#     assert str(unicode(uhtml.title('a', b='c'))) == '<title b="c">a</title>\n'
#     assert str(unicode(uhtml.tr('a', b='c'))) == '<tr b="c">a</tr>\n'
#     assert str(unicode(uhtml.tt('a', b='c'))) == '<tt b="c">a</tt>'
#     assert str(unicode(uhtml.u('a', b='c'))) == '<u b="c">a</u>'
#     assert str(unicode(uhtml.ul('a', b='c'))) == '<ul b="c">a</ul>\n'
#     assert str(unicode(uhtml.var('a', b='c'))) == '<var b="c">a</var>'
#
#     for t in uhtml.tags:
#         nl = '\\n' if t in uhtml._nlafter else ''
#         # print """    assert str(unicode(uhtml.%s('a', b='c'))) == '<%s b=\"c\">a</%s>%s'""" % (t,t,t, nl)
#
