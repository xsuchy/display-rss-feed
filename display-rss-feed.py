# -*- coding: utf-8 -*-
# vim: noai:ts=4:sw=4:expandtab

import feedparser
from pprint import pprint
from jinja2 import Template

# https://www.ricanyubrna.cz/api/rss/
# https://www.ricanyubrna.cz/api/rss/?type=atom

TEMPLATE = 'template.html'

feed = feedparser.parse('https://www.ricanyubrna.cz/api/rss/')
with open(TEMPLATE) as f:
    template = Template(f.read())

keys = feed.keys()
msg = template.render(entries=feed['entries'])
print(msg)
#for entry in feed['entries']:
#    print(entry['title'])
#    print(entry['summary'])
#    print(entry['link'])
#    print('*****')
