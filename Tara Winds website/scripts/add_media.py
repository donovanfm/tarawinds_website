# add_media.py
#
# Use this script to add groups of photos to the TW website Media page.
#
# Requirements:
#   Python
#   BeautifulSoup library
#
# Assumes the following file structure
# /
#   images/content/media-page/{year}/{event}/
#     ...all images from event here...
#   scripts/
#     add_media.py <-- This script
#   media.html
#
# Usage:
#

from bs4 import BeautifulSoup as Soup
import sys
import os 

year = sys.argv[1]
event = sys.argv[2]
thumbnail = sys.argv[3]
group_number = sys.argv[4]

media_page = open("../media.html", "r")
html = media_page.read()
media_page.close()

soup = Soup(html)

photo_albums = soup.find_all("div", {"class": "photo-albums"})[0]

photo_dir = f'../images/content/media-page/{year}/{event}'

top = soup.new_tag('div')
top['class'] = []
top['class'].append('col-sm-6')

fig = soup.new_tag('figure')
fig['class'] = []
fig['class'].append('img-hover2')
fig['class'].append('hover-white')
  
thumbnail_anchor = soup.new_tag('a')
thumbnail_anchor['class'] = []
thumbnail_anchor['class'].append('fancybox-thumbs')
thumbnail_anchor['data-fancybox-group'] = f'thumb{group_number}'
thumbnail_anchor['href'] = f'images/content/media-page/{year}/{event}/{thumbnail}'

img = soup.new_tag('img')
img['src'] = f'images/content/media-page/{year}/{event}/{thumbnail}'
img['alt']= 'img'
thumbnail_anchor.append(img)

div = soup.new_tag('div')
div['class'] = []
div['class'].append('overlay-masked')
i = soup.new_tag('i')
i['class'] = []
i['class'].append('ion')
i['class'].append('ion-eye')
div.append(i)
thumbnail_anchor.append(div)

fig.append(thumbnail_anchor)

for photo in os.listdir(photo_dir):
  photo_anchor = soup.new_tag('a')
  photo_anchor['href'] = f'images/content/media-page/{year}/{event}/{photo}'
  photo_anchor['class'] = []
  photo_anchor['class'].append('fancybox-thumbs')
  photo_anchor['class'].append('hidden')
  photo_anchor['data-fancybox-group'] = f'thumb{group_number}'

  photo_img = soup.new_tag('img')
  photo_img['src'] = f'images/content/media-page/{year}/{event}/{photo}'
  photo_img['alt'] = 'img'

  photo_anchor.append(photo_img)
  fig.append(photo_anchor)

top.append(fig)
photo_albums.insert(0, top)

media_page = open("../media.html", "w")
media_page.write(soup.prettify())
media_page.close()
