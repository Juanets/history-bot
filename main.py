import time
from api import TwitterAPI, Events

e = Events()
twitter = TwitterAPI()
events = e.get_events()

for event in events:
	time.sleep(10)
	try:
		twitter.compose(event)
		print 'ok'
	except Exception as e:
		print e.message