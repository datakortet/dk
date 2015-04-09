# -*- coding: utf-8 -*-

"""Module for finding all models in a given app.
"""

import inspect
from django.db import models


def findmodels(appname):
    """Appname should be just the name of the app folder.
       yields the actual model classes (the name can be retrieved
       from .__name__).
    """
    importpath = 'datakortet.%s.models' % appname
    modelsmodule = __import__(importpath, globals(), locals(), ['*'], -1)
    for name in dir(modelsmodule):
        module_item = getattr(modelsmodule, name)
        if not inspect.isclass(module_item):
            continue
        if issubclass(module_item, models.Model):
            yield module_item
