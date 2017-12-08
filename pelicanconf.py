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
SOCIAL = (('OrderCloud.io Twitter', 'https://twitter.com/ordercloudapi'),
          ('OrderCloud.io Community Support Slack', 'http://community.ordercloud.io/'),)

DEFAULT_PAGINATION = 10
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# plugins

PLUGIN_PATHS = ['pelican-plugins', 'pelican-bootstrapify']
PLUGINS = {
					'assets',
					'sitemap',
					'touch',
          'pelican-bootstrapify',
          'neighbors',
          'post-stats'
          #yuicompressor #enable after theming

					#'filetime_from_git'
					#'ace_editor'
					}

# filetime_from_git

#GIT_HISTORY_FOLLOWS_RENAME = True

#GIT_GENERATE_PERMALINK = True

#GIT_SHA_METADATA = True

#GIT_FILETIME_FROM_GIT = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
    'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


SUMMARY_MAX_LENGTH = 50


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
