import schedule
import time
import os

def tweet():
	print 'Time to tweet.'
	os.system('python app/main.py')

schedule.every().day.at('08:00').do(job)

while True:
	schedule.run_pending()
	time.sleep(1)