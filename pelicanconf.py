#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matt Layman'
SITENAME = "Matt's Portfolio"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'Flex'

SITETITLE = AUTHOR
SITESUBTITLE = 'Python Frederick organizer'
SITEDESCRIPTION = 'Demo site for Python Frederick March 2018'
SITELOGO = 'https://avatars1.githubusercontent.com/u/636865?s=460&v=4'

MAIN_MENU = True
MENUITEMS = (
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

DISABLE_URL_HASH = True
SOCIAL = (
    ('twitter', 'https://twitter.com/mblayman'),
    ('github', 'https://github.com/mblayman'),
)

COPYRIGHT_NAME = 'Matt Layman'
COPYRIGHT_YEAR = 2018
