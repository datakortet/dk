"""This module is dedicated to creating javascript snippets that can be
   consumed elsewhere.
   (uses MochiKit and seems to be imported in way too many places...)
"""
import warnings
# this is way old code, from before Python had ''.format()...
from string import Template as _T  # pylint:disable=W0402


def _subst(txt, args):
    return _T(txt).substitute(args)


def javascript(txt, **args):
    "Compress javascript into a single line, for in-situ on___ handlers."
    warnings.warn("Use of javascript is deprecated", DeprecationWarning)
    txt = txt.strip()
    lines = txt.split('\n')
    txt = ';'.join(line.strip() for line in lines)
    return _subst(txt, args)


def setpnumber_function(postnrid, poststedid):
    "Event handler to load poststed from postnr, through an ajax call."
    warnings.warn("Use of setpnumber_function is deprecated", DeprecationWarning)
    return """
        var setpnumber = function () {
          var jdoc = loadJSONDoc('http://cache.norsktest.no/ajax/poststed/' + $('%s').value + '/');
          jdoc.addCallback(function (result) {
             if (result != "")
                $('%s').value = result;
          });
        }""" % (postnrid, poststedid)


def setpnumber_connect(postnrid):
    "Add onblur handler that connects the above event handler."
    return f"connect($('{postnrid}'), 'onblur', setpnumber);"


def focus(item):
    "Output javascript to focus on item."
    warnings.warn("Use of focus is deprecated", DeprecationWarning)
    return javascript("""
        $$('#$item').focus()
    """, item=item)


def submit_form(formname):
    """JS sniplet that will submit the named form when being the target
       of an event-handler.
    """
    warnings.warn("Use of submit_form is deprecated", DeprecationWarning)
    return javascript('''
        getElementById('$formname').submit()
        ''', formname=formname)


def link(url):
    """Same as a html.a element"""
    warnings.warn("Use of link is deprecated", DeprecationWarning)
    return javascript("""
        window.location = '$url'
    """, url=url)


def set_datefield(name, year, month, day):  # pylint:disable=W0613
    """The year/month/day values need to be calculated as in the SetDateButton
       in widgets.
    """
    warnings.warn("Use of set_datefield is deprecated", DeprecationWarning)
    return javascript("""
        getElementById('id_${name}_year').selectedIndex = $year
        getElementById('id_${name}_month').selectedIndex = $month
        getElementById('id_${name}_day').selectedIndex = $day
    """, **locals())
