# coding=utf-8
import tweepy
import requests
from secrets import *
from bs4 import BeautifulSoup

class TwitterAPI():
	def __init__(self):
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)		
		self.api = tweepy.API(auth)

	def compose(self, tweet):
		self.api.update_status(tweet)


class Events():
	def __init__(self):
		r = requests.get('http://www.onthisday.com/')
		self.soup = BeautifulSoup(r.content, 'html.parser')

	def get_events(self):		
		events = []
		events_html = self.soup.find('div', class_='section no-padding-top').find(
							   'ul', class_='event-list event-list--with-advert'
							   ).find_all('li')				

		for e in events_html:
			f_event = self.format(e.text)
			if len(f_event) < 140: 
				events.append(f_event) 

		return events
	
	def format(self, text):
		return '#Today in ' + text[:4] + ',' + text[4:]