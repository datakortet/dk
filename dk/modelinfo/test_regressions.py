
"""modelmetainfo regressiontests.
"""

from datakortet.core import modelinfo

# testing models
from datakortet.bfp.models import BFRegister
from datakortet.tag.models import TagJob


def test_html():
    m = modelinfo.info(BFRegister)
    print m.field_info['kid']


if __name__ == "__main__":
    test_html()
