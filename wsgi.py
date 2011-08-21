#!/usr/bin/env python

"""
DotCloud Django Docs:  http://olddocs.dotcloud.com/tutorials/django/

In order for the application to run on DotCloud, it must have a
`wsgi.py` file.
"""

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
