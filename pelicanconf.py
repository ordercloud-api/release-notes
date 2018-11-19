#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import pathlib


AUTHOR = 'OrderCloud'
SITENAME = 'OrderCloud API Release Notes'
SITEURL = 'localhost:8000'
TIMEZONE = "America/Chicago"
DEFAULT_LANG = 'English'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']
THEME = 'pelican-themes/pelican-bootstrap3'


# global metadata to all the contents


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('OrderCloud.io', 'https://ordercloud.io'),
    ('OrderCloud Documentation', 'https://documentation.ordercloud.io/'),
    ('OrderCloud.io Community Support Slack', 'http://community.ordercloud.io/')
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AUTHOR_SAVE_AS = 'author/{slug}.html'
