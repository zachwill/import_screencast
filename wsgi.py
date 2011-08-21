#!/usr/bin/env python

"""
DotCloud Django Docs:  http://olddocs.dotcloud.com/tutorials/django/

In order for the application to run on DotCloud, it must have a
`wsgi.py` file.
"""

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'import_screencast.settings'

import django.core.handlers.wsgi
django_app = django.core.handlers.wsgi.WSGIHandler()


def application(environ, start_response):
    """
    The DotCloud `wsgi.py` file must have an application variable or
    executable.
    """
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return django_app(environ, start_response)
