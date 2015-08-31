# -*- coding: utf-8 -*-

"core.dklogger"

# pylint:disable=R0904
# R0904: Too many public methods

from dk import dklogger
from logging import DEBUG, INFO


def test_dklogger():
    "Test of dklogger"
    assert dklogger.dklogger(
        __name__,
        debug=1,
        info=1
    ).name == 'tests.test_dklogger'
    assert dklogger.dklogger(__name__, debug=1, info=0).level == DEBUG
    assert dklogger.dklogger(__name__, debug=0, info=1).level == INFO
