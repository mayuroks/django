# from .models import SampleCount
from celery import task
from requests import get
from BeautifulSoup import BeautifulSoup
import re 
@task
def add(x, y):
	return x + y

## TAKES couchseats URL and returns (artist, title, youtube_url) 
@task
def my_info_fetcher(url_str=""):
	if url_str:
# fetch page source of cs_URL
		r = get(url_str)
		data = r.content
		soup = BeautifulSoup(data)
		page_ka_title = soup.findAll('title')
		## page_ka_title = Nine Inch Nails - Hurt Live | CouchSeats.com
		title = str(page_ka_title[0].string).split("|")[0]
		## title = Nine Inch Nails - Hurt Live		
		artist = title.split("-")[0].strip(' ')
		## artist = Nine Inch Nails
		youtube_url = str(soup.findAll('iframe')[0]['src']).split("?&")[0]
		## youtube_url = 'http://www.youtube.com/embed/fb4qyuR7_cc'
		print "TITLE = %s , ARTIST = %s, URL = %s" % (title,artist,youtube_url)
		# CALL api/q?=artist= group0 & title = group1 & youtube_url = group2
			# to directly fill the form and populate










