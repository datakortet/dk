

def tagtester(htmlmod):
    assert str(unicode(htmlmod.a('a', b='c'))) == '<a b="c">a</a>'
    assert str(unicode(htmlmod.abbr('a', b='c'))) == '<abbr b="c">a</abbr>'
    assert str(unicode(htmlmod.acronym('a', b='c'))) == '<acronym b="c">a</acronym>'
    assert str(unicode(htmlmod.address('a', b='c'))) == '<address b="c">a</address>'
    assert str(unicode(htmlmod.applet('a', b='c'))) == '<applet b="c">a</applet>'
    assert str(unicode(htmlmod.area('a', b='c'))) == '<area b="c">a</area>'
    assert str(unicode(htmlmod.b('a', b='c'))) == '<b b="c">a</b>'
    assert str(unicode(htmlmod.base('a', b='c'))) == '<base b="c">a</base>'
    assert str(unicode(htmlmod.bsefont('a', b='c'))) == '<bsefont b="c">a</bsefont>'
    assert str(unicode(htmlmod.bdo('a', b='c'))) == '<bdo b="c">a</bdo>'
    assert str(unicode(htmlmod.big('a', b='c'))) == '<big b="c">a</big>'
    assert str(unicode(htmlmod.blockquote('a', b='c'))) == '<blockquote b="c">a</blockquote>\n'
    assert str(unicode(htmlmod.body('a', b='c'))) == '<body b="c">a</body>\n'
    assert str(unicode(htmlmod.button('a', b='c'))) == '<button b="c">a</button>'
    assert str(unicode(htmlmod.center('a', b='c'))) == '<center b="c">a</center>\n'
    assert str(unicode(htmlmod.cite('a', b='c'))) == '<cite b="c">a</cite>'
    assert str(unicode(htmlmod.code('a', b='c'))) == '<code b="c">a</code>'
    assert str(unicode(htmlmod.colgroup('a', b='c'))) == '<colgroup b="c">a</colgroup>\n'
    assert str(unicode(htmlmod.dd('a', b='c'))) == '<dd b="c">a</dd>'
    assert str(unicode(htmlmod.dfn('a', b='c'))) == '<dfn b="c">a</dfn>'
    assert str(unicode(htmlmod.div('a', b='c'))) == '<div b="c">a</div>\n'
    assert str(unicode(htmlmod.dl('a', b='c'))) == '<dl b="c">a</dl>\n'
    assert str(unicode(htmlmod.dt('a', b='c'))) == '<dt b="c">a</dt>\n'
    assert str(unicode(htmlmod.em('a', b='c'))) == '<em b="c">a</em>'
    assert str(unicode(htmlmod.fieldset('a', b='c'))) == '<fieldset b="c">a</fieldset>\n'
    assert str(unicode(htmlmod.font('a', b='c'))) == '<font b="c">a</font>'
    assert str(unicode(htmlmod.form('a', b='c'))) == '<form b="c">a</form>\n'
    assert str(unicode(htmlmod.frame('a', b='c'))) == '<frame b="c">a</frame>\n'
    assert str(unicode(htmlmod.frameset('a', b='c'))) == '<frameset b="c">a</frameset>'
    assert str(unicode(htmlmod.h1('a', b='c'))) == '<h1 b="c">a</h1>\n'
    assert str(unicode(htmlmod.h2('a', b='c'))) == '<h2 b="c">a</h2>\n'
    assert str(unicode(htmlmod.h3('a', b='c'))) == '<h3 b="c">a</h3>\n'
    assert str(unicode(htmlmod.h4('a', b='c'))) == '<h4 b="c">a</h4>\n'
    assert str(unicode(htmlmod.h5('a', b='c'))) == '<h5 b="c">a</h5>\n'
    assert str(unicode(htmlmod.h6('a', b='c'))) == '<h6 b="c">a</h6>\n'
    assert str(unicode(htmlmod.head('a', b='c'))) == '<head b="c">a</head>\n'
    assert str(unicode(htmlmod.html('a', b='c'))) == '<html b="c">a</html>\n'
    assert str(unicode(htmlmod.i('a', b='c'))) == '<i b="c">a</i>'
    assert str(unicode(htmlmod.iframe('a', b='c'))) == '<iframe b="c">a</iframe>\n'
    assert str(unicode(htmlmod.ins('a', b='c'))) == '<ins b="c">a</ins>'
    assert str(unicode(htmlmod.kbd('a', b='c'))) == '<kbd b="c">a</kbd>'
    assert str(unicode(htmlmod.label('a', b='c'))) == '<label b="c">a</label>'
    assert str(unicode(htmlmod.li('a', b='c'))) == '<li b="c">a</li>\n'
    assert str(unicode(htmlmod.map('a', b='c'))) == '<map b="c">a</map>'
    assert str(unicode(htmlmod.menu('a', b='c'))) == '<menu b="c">a</menu>'
    assert str(unicode(htmlmod.nobr('a', b='c'))) == '<nobr b="c">a</nobr>'
    assert str(unicode(htmlmod.noframes('a', b='c'))) == '<noframes b="c">a</noframes>'
    assert str(unicode(htmlmod.noscript('a', b='c'))) == '<noscript b="c">a</noscript>'
    assert str(unicode(htmlmod.ol('a', b='c'))) == '<ol b="c">a</ol>\n'
    assert str(unicode(htmlmod.optgroup('a', b='c'))) == '<optgroup b="c">a</optgroup>'
    assert str(unicode(htmlmod.option('a', b='c'))) == '<option b="c">a</option>\n'
    assert str(unicode(htmlmod.p('a', b='c'))) == '<p b="c">a</p>\n'
    assert str(unicode(htmlmod.param('a', b='c'))) == '<param b="c">a</param>'
    assert str(unicode(htmlmod.pre('a', b='c'))) == '<pre b="c">a</pre>\n'
    assert str(unicode(htmlmod.q('a', b='c'))) == '<q b="c">a</q>'
    assert str(unicode(htmlmod.s('a', b='c'))) == '<s b="c">a</s>'
    assert str(unicode(htmlmod.samp('a', b='c'))) == '<samp b="c">a</samp>'
    assert str(unicode(htmlmod.small('a', b='c'))) == '<small b="c">a</small>'
    assert str(unicode(htmlmod.span('a', b='c'))) == '<span b="c">a</span>'
    assert str(unicode(htmlmod.strike('a', b='c'))) == '<strike b="c">a</strike>'
    assert str(unicode(htmlmod.strong('a', b='c'))) == '<strong b="c">a</strong>'
    assert str(unicode(htmlmod.sub('a', b='c'))) == '<sub b="c">a</sub>'
    assert str(unicode(htmlmod.sup('a', b='c'))) == '<sup b="c">a</sup>'
    assert str(unicode(htmlmod.table('a', b='c'))) == '<table b="c">a</table>\n'
    assert str(unicode(htmlmod.tbody('a', b='c'))) == '<tbody b="c">a</tbody>\n'
    assert str(unicode(htmlmod.td('a', b='c'))) == '<td b="c">a</td>'
    assert str(unicode(htmlmod.textarea('a', b='c'))) == '<textarea b="c">a</textarea>'
    assert str(unicode(htmlmod.tfoot('a', b='c'))) == '<tfoot b="c">a</tfoot>'
    assert str(unicode(htmlmod.th('a', b='c'))) == '<th b="c">a</th>'
    assert str(unicode(htmlmod.thead('a', b='c'))) == '<thead b="c">a</thead>'
    assert str(unicode(htmlmod.title('a', b='c'))) == '<title b="c">a</title>\n'
    assert str(unicode(htmlmod.tr('a', b='c'))) == '<tr b="c">a</tr>\n'
    assert str(unicode(htmlmod.tt('a', b='c'))) == '<tt b="c">a</tt>'
    assert str(unicode(htmlmod.u('a', b='c'))) == '<u b="c">a</u>'
    assert str(unicode(htmlmod.ul('a', b='c'))) == '<ul b="c">a</ul>\n'
    assert str(unicode(htmlmod.var('a', b='c'))) == '<var b="c">a</var>'

    for t in htmlmod.tags:
        nl = '\\n' if t in htmlmod._nlafter else ''
        #print """    assert str(unicode(htmlmod.%s('a', b='c'))) == '<%s b=\"c\">a</%s>%s'""" % (t,t,t, nl)


def test_html():
    from . import html
    return tagtester(html)


def test_uhtml():
    from . import uhtml
    return tagtester(uhtml)


if __name__ == "__main__":
    test_html()
    test_uhtml()
