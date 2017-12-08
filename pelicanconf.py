#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'OrderCloud'
SITENAME = 'OrderCloud API Release Notes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

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
         ('Pelican', 'http://getpelican.com/')
         )

# Social widget
SOCIAL = (('OrderCloud.io Twitter', '#'),
          ('OrderCloud.io Community Slack', '#'),)

DEFAULT_PAGINATION = 10
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# plugins

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
					#'assets',
					#'sitemap',
					'filetime_from_git']

# filetime_from_git

#GIT_HISTORY_FOLLOWS_RENAME = True

#GIT_GENERATE_PERMALINK = True

#GIT_SHA_METADATA = True

GIT_FILETIME_FROM_GIT = True


SUMMARY_MAX_LENGTH = 50


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
