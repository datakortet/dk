# -*- coding: utf-8 -*-

"dk.identifiers.persnr"

# pylint:disable=R0904
# R0904 = Too many public methods
import datetime

import pytest
from dk.identifiers import persnr

    
pnr1 = '02057035768'
pnr2 = '01027373737'
pnr3 = 'xx022123xx2'
pnr4 = '07107846020'
    

def test_check_pnr():
    "Test the 'check_pnr' function"
    assert persnr.check_pnr(pnr1, datetime.date(1970, 5, 2), 'm')

    with pytest.raises(persnr.PersnrException):
        persnr.check_pnr(pnr2, datetime.date(1973, 2, 1), 'm')


def test_check_pnr_structure():
    "Test the 'check_pnr_structure' function"
    assert persnr.check_pnr_structure(pnr1)
    with pytest.raises(persnr.PersnrException):
        persnr.check_pnr_structure(pnr2)


def test_is_persnr():
    "Test the 'is_persnr' function"
    assert persnr.is_persnr(pnr1)
    assert not persnr.is_persnr(pnr2)
    assert not persnr.is_persnr(pnr3)

                     
def test_list_pnr():
    "Test the 'list_pnr' function"
    assert type(persnr.list_pnr()) == list


def test_gender():
    "Test the 'gender' function"
    assert persnr.gender(pnr1) == 'M'
    assert persnr.gender(pnr4) == 'F'


def test_is_anonymized():
    assert persnr.is_anonymized('92345678901')


def test_anonymize_persnr():
    for pnr in persnr.list_pnr(gender='F') + persnr.list_pnr(gender='M'):
        apnr = persnr.anonymize_persnr(pnr)
        assert persnr.is_anonymized(apnr)
        aparts = persnr.splitpnr(apnr)
        parts = persnr.splitpnr(pnr)
        assert parts['year'] == aparts['year']
        assert persnr.year(pnr) == persnr.year(apnr)
        assert parts['gender'] == aparts['gender']


def test_dnr():
    """Test D-nummer.
       (http://www.skatteetaten.no/no/Artikler/Hvem-kan-rekvirere-D-nummer/
    """
    dnr = '57106112373'
    assert persnr.check_pnr_structure(dnr)
    assert persnr.check_parity(dnr)
    assert persnr.year(dnr) == 1961
    assert persnr.date(dnr) == datetime.date(1961, 10, 17)
    assert persnr.gender(dnr) == 'M'
    assert persnr.check_pnr(dnr, datetime.date(1961, 10, 17), 'M')
    assert persnr.is_persnr(dnr)
