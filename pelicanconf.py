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

#DISPLAY_PAGES_ON_MENU = True
#DISPLAY_LINKS_ON_MENU = False
#DISPLAY_SOCIAL_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

LINKS = (
	       ('OrderCloud.io', 'https://ordercloud.io'),
         ('OrderCloud Documentation', 'https://documentation.ordercloud.io/'),
                  ('OrderCloud.io Community Support Slack', 'http://community.ordercloud.io/')
         )


# Social widget
TWITTER = ('OrderCloud.io Twitter', 'https://twitter.com/ordercloudapi')
RSS_FEED = ('Full Site RSS', SITEURL+'/release-notes/feeds/all.atom.xml')
CAT_RSS_FEED = ('Release Notes RSS', SITEURL+'/release-notes/feeds/release-notes.atom.xml')

SOCIAL = (
          TWITTER,
          RSS_FEED,
          CAT_RSS_FEED
         )




# plugins

PLUGIN_PATHS = ['pelican-plugins', 'pelican-bootstrapify', 'plugins']

PLUGINS = {
					'assets',
					'sitemap',
					'touch',
          'pelican-bootstrapify',
          'neighbors',
          'representative_image',
          'tag_cloud',
          'tipue_search',
          'i18n_subsites'
          #'post-stats',
          #'yuicompressor' #enable after theming

					#'filetime_from_git'
					#'ace_editor'
					}

DEFAULT_DATE = 'fs'

TYPOGRIFY = True

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
USE_FOLDER_AS_CATEGORY = True


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# themes

THEME = "pelican-themes/pelican-bootstrap3"

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
SHOW_ARTICLE_AUTHOR =  False
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
DISPLAY_TAGS_ON_SIDEBAR = False
PYGMENTS_STYLE = 'monokai'
#BOOTSTRAP_FLUID= True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_THEME = 'lumen'
DISPLAY_ARCHIVE_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
#FAVICON = 
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-82258138-2'




DEFAULT_PAGINATION = 5
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'


