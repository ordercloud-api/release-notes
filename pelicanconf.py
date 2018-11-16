#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'OrderCloud'
SITENAME = 'OrderCloud API Release Notes'
SITEURL = 'localhost:8000'
TIMEZONE = "America/Chicago"
DEFAULT_LANG = 'English'

PATH = 'content'

# global metadata to all the contents
DEFAULT_METADATA = {
    'Title': 'OrderCloud API v{ApiVersion} Release Notes',
    'Category': 'API Release Notes',
    'Tags': 'OrderCloud API',
    'Date': datetime.today(),
    'Status': 'draft',
    'Authors': 'Kate Reeher'}

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

THEME = 'bootstrap'
