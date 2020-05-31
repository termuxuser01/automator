import os
import feedparser
import delorean
import datetime
import requests

# parse feed and check update date

rss = feedparser.parse('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')

print('showing update time...:\n', rss.channel.updated)

# set the update time in hours

update_time = delorean.parse(rss.channel.updated) - datetime.timedelta(hours=6)

# get entries of specified time

entries = [e for e in rss.entries if delorean.parse(e.published) > update_time]

print('Retrieved articles:\n', len(entries))

# return tittles of entries
for article in entries:
    print(entries.index(article) + 1, article['title'])

# get link for entries
entry_no = int(input('select the entry you wish to retrieve the link from:\n')) - 1

print('Here\'s the link:\n', entries[entry_no]['link'])

choice = input('open in browser? y/n')

if choice == 'y':
    os.system('firefox {}'.format(entries[entry_no]['link']))
else:
    print('OK!')
