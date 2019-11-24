#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Base info
AUTHOR = 'Brendan King'
SITENAME = 'Brendan King'
# SITEURL = 'https://kingb12.github.io'
THEME = '/Users/bking/pelican/pelican-themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['/Users/bking/pelican/pelican-plugins']
PLUGINS = ['i18n_subsites']

# Page content configuration
PATH = 'content'
STATIC_PATHS = [
    'pdf',
    'images'
]
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Styling parameters
BOOTSTRAP_THEME = "flatly"
DISPLAY_CATEGORIES_ON_MENU = False
BOOTSTRAP_NAVBAR_INVERSE = False
HIDE_SITENAME = False
SIDEBAR_ON_LEFT = True
HIDE_SIDEBAR = True
DISABLE_SIDEBAR_TITLE_ICONS = True
DEFAULT_PAGINATION = 10

# About Me
AVATAR = "images/prof-circle.png"
ABOUT_ME = "Software Engineer<br />Prospective Ph.D. Student<br />Novice Mountaineer <br /><br /><b>This site is " \
           "under construction!</b> I'll be collecting projects, publications, and more here."

# Blogroll
SOCIAL = (('GitHub', 'http://github.com/kingb12'),
          ('LinkedIn', 'http://www.linkedin.com/in/kingb12'))

SIDEBAR_IMAGES_HEADER = "<b> can I just put HTML here?</b>"
SIDEBAR_IMAGES = []
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
