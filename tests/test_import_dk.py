# -*- coding: utf-8 -*-

"""Test that all modules are importable.
"""
import dk.collections.invdict
import dk.collections.mmap
import dk.collections.OrderedSet
import dk.collections.pset
import dk.collections.sdict
import dk.collections.xmlrec
import dk.findapps
import dk.findmodels
import dk.html.css
import dk.html.html
import dk.html.theme
import dk.html.uhtml
import dk.identifiers.kid
import dk.identifiers.persnr
import dk.js.js
import dk.dkimport
import dk.dklogger
import dk.fstr
import dk.getsettings
import dk.grid
import dk.proxy
import dk.text
import dk.utidy
import dk.utils
import dk.search


def test_import_dk():
    "Test that all modules are importable."
    assert dk.collections.invdict
    assert dk.collections.mmap
    assert dk.collections.OrderedSet
    assert dk.collections.pset
    assert dk.collections.sdict
    assert dk.collections.xmlrec
    assert dk.findapps
    assert dk.findmodels
    assert dk.html.css
    assert dk.html.html
    assert dk.html.theme
    assert dk.html.uhtml
    assert dk.identifiers.kid
    assert dk.identifiers.persnr
    assert dk.js.js
    assert dk.dkimport
    assert dk.dklogger
    assert dk.fstr
    assert dk.getsettings
    assert dk.grid
    assert dk.proxy
    assert dk.text
    assert dk.utidy
    assert dk.utils
    assert dk.search
