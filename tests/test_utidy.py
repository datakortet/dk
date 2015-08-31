# -*- coding: utf-8 -*-
from dk.utidy import utidy


def test_text():
    text = utidy('''<form name="FirmaForm" id="FirmaForm" method="POST" autocomplete="off"
        action="." class="fForm"><input type="hidden" name="__cmd"
        value="FirmaForm"></form>hello
        ''')

    result = '''<form action="." autocomplete="off" class="fForm" id="FirmaForm" method="POST" name="FirmaForm">
    <input name="__cmd" type="hidden" value="FirmaForm">
</form>
hello'''
    assert text == result
