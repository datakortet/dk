import os

import pytest

from dk import dkimport
DIRNAME = os.path.dirname(__file__)


def test_dkimport():
    item = dkimport.dkimport('dk.dkimport.dkimport')
    assert item.__name__ == 'dkimport'

    with pytest.raises(ValueError):
        dkimport.dkimport('/foo')


def test_defined_symbols():
    symbol_names = [m.__name__ for m in dkimport.defined_symbols(dkimport)]
    assert 'defined_symbols' in symbol_names
    assert 'dkimport' in symbol_names


def test_load_files_from():
    items = [f for f in dkimport.load_files_from(
        os.path.join(os.path.dirname(DIRNAME), 'dk'),
        'dk',
        filefilter=lambda fname: fname == 'dkimport.py'
    )]
    assert items == [dkimport]


def test_dkimport_star():
    symbols = dkimport.dkimport_star('dk.collections')
    assert 1   #


def test_dkimport_functions():
    fns = dkimport.dkimport_functions('dk.collections')
    assert fns == []
