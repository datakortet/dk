# -*- coding: utf-8 -*-

"core.iplist"

# pylint:disable=R0904
# R0904: Too many public methods

import ipaddr
from dktest import TestCase
from dk.iplist import IPList
from dkjs import jason


class TestIPList(TestCase):
    "Unit test for the IPList module"
    
    def setUp(self):        
        a1 = ipaddr.IPv4Address('81.0.132.118')
        a2 = ipaddr.IPv4Address('81.0.132.119')
        a3 = ipaddr.IPv4Address('81.0.132.109')
        a4 = ipaddr.IPv4Address('81.0.132.123')        
        self.iplist = IPList([a1, a2, a3, a4])
        self.iplist2 = IPList()
    
    def test_pack_unpack(self):
        "Test of the pack and unpack methods"        
        self.iplist2.unpack(self.iplist.pack())
        self.assertEqual(self.iplist, self.iplist2)
    
    def test_add(self):
        "Test of the add method"
        self.iplist2.unpack(self.iplist.pack())
        self.iplist2.add(ipaddr.IPv4Address('81.0.132.42'))
        self.assertNotEqual(self.iplist, self.iplist2)

    def test_encode(self):
        "Test ascii encoding of values"
        pval = self.iplist.pack()
        self.assertEqual(pval, 'eJwLZGjJDWRoKQPiciCuBgAptQUq')
        self.assertEqual(pval.encode('ascii'), 'eJwLZGjJDWRoKQPiciCuBgAptQUq')
                
    def test_json(self):
        "Test json dumps of iplist"
        self.assertEqual(jason.dumps(self.iplist, indent=None),
                         ('["81.0.132.109", "81.0.132.118",'
                          ' "81.0.132.119", "81.0.132.123"]'))
