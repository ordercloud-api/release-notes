#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'OrderCloud'
SITENAME = 'OrderCloud API Release Notes'
SITEURL = 'localhost:8000'

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

DISPLAY_PAGES_ON_MENU = True
DISPLAY_LINKS_ON_MENU = False
DISPLAY_SOCIAL_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

LINKS = (
	       ('OrderCloud.io', 'https://ordercloud.io'),
         ('OrderCloud Documentation', 'https://documentation.ordercloud.io/'),
                  ('OrderCloud.io Community Support Slack', 'http://community.ordercloud.io/')
         )


# Social widget
TWITTER = ('OrderCloud.io Twitter', 'https://twitter.com/ordercloudapi')
RSS_FEED = ('Release Notes RSS', 'https://ordercloud-api.github.io/release-notes/feeds/all.atom.xml')


SOCIAL = (
          TWITTER,
          RSS_FEED
         )




# plugins

PLUGIN_PATHS = ['pelican-plugins', 'pelican-bootstrapify']
PLUGINS = {
					'assets',
					'sitemap',
					'touch',
          'pelican-bootstrapify',
          'neighbors',
          #'post-stats',
          'yuicompressor' #enable after theming

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


SUMMARY_MAX_LENGTH = 100


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# themes

THEME = "pelican-themes/foundation-default-colours"

FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = True
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a>. Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
FOUNDATION_PYGMENT_THEME = 'monokai'

DEFAULT_PAGINATION = 5
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
