# -*- coding: utf-8 -*-

"""Test that all modules are importable.
"""

import dk
import dk.age
import dk.asciify
import dk.collections
import dk.collections.OrderedSet
import dk.collections.invdict
import dk.collections.mmap
import dk.collections.pset
import dk.collections.sdict
import dk.collections.xmlrec
import dk.dkimport
import dk.dklogger
import dk.fstr
import dk.gchart
import dk.grid
import dk.html
import dk.html.css
import dk.html.html
import dk.html.theme
import dk.html.uhtml
import dk.iplist
import dk.js
import dk.js.js
import dk.proxy
import dk.text
import dk.utidy
import dk.utils


def test_import_dk():
    """Test that all modules are importable.
    """
    
    assert dk
    assert dk.age
    assert dk.asciify
    assert dk.collections
    assert dk.collections.OrderedSet
    assert dk.collections.invdict
    assert dk.collections.mmap
    assert dk.collections.pset
    assert dk.collections.sdict
    assert dk.collections.xmlrec
    assert dk.dkimport
    assert dk.dklogger
    assert dk.fstr
    assert dk.gchart
    assert dk.grid
    assert dk.html
    assert dk.html.css
    assert dk.html.html
    assert dk.html.theme
    assert dk.html.uhtml
    assert dk.iplist
    assert dk.js
    assert dk.js.js
    assert dk.proxy
    assert dk.text
    assert dk.utidy
    assert dk.utils
