# -*- coding: utf-8 -*-

"core.iplist"

# pylint:disable=R0904
# R0904: Too many public methods

import ipaddr
from dk.iplist import IPList
import pytest


@pytest.fixture
def iplist():
    return IPList([a1, a2, a3, a4])


@pytest.fixture
def a1():
    return ipaddr.IPv4Address('81.0.132.118')


@pytest.fixture
def a2():
    return ipaddr.IPv4Address('81.0.132.119')


@pytest.fixture
def a3():
    return ipaddr.IPv4Address('81.0.132.109')


@pytest.fixture
def a4():
    return ipaddr.IPv4Address('81.0.132.123')


@pytest.fixture
def iplist(a1, a2, a3, a4):
    return IPList([a1, a2, a3, a4])


@pytest.fixture
def iplist2():
    return IPList()


def test_pack_unpack(iplist, iplist2):
    """Test of the pack and unpack methods.
    """
    iplist2.unpack(iplist.pack())
    assert iplist == iplist2


def test_add(iplist, iplist2):
    """Test of the add method.
    """
    iplist2.unpack(iplist.pack())
    iplist2.add(ipaddr.IPv4Address('81.0.132.42'))
    assert iplist != iplist2


def test_encode(iplist):
    """Test ascii encoding of values.
    """
    pval = iplist.pack()
    assert pval == 'eJwLZGjJDWRoKQPiciCuBgAptQUq'
    assert pval.encode('ascii') == 'eJwLZGjJDWRoKQPiciCuBgAptQUq'


try:
    import json

    def test_json(iplist):
        """Test json dumps of iplist.
        """
        assert json.dumps(iplist.__json__(), indent=None) == (
            '["81.0.132.109", "81.0.132.118", "81.0.132.119", "81.0.132.123"]'
        )

except ImportError:
    pass
