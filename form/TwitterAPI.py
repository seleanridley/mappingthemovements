'''
	Contributors: Emily Simoneau and Cameron Bates
'''
#from . import APICall
from twython import Twython
import json
##from datetime import date, datetime

class TwitterAPI():	
	def __init__(self):
		self.results = {}
		with open("twitter_credentials.json", "r") as file:  
			self.creds = json.load(file)
		

	def search(self, keyword, date_start, date_end):
		self.results = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'user_loc':[]}
		python_tweets = Twython(self.creds['CONSUMER_KEY'], self.creds['CONSUMER_SECRET'])
		##date_start_str = self.date_to_string(date_start)
		##date_end_str = self.date_to_string(date_end)
		for status in python_tweets.search(q=keyword, until=date_end, since=date_start)['statuses']:
			self.results['user'].append(status['user']['screen_name'])
			self.results['date'].append(status['created_at'])
			self.results['text'].append(status['text'])
			self.results['favorite_count'].append(status['favorite_count'])
			self.results['user_loc'].append(status['user']['location'])
	'''
	def date_to_string(self, date_obj) :
		date_string = str(date_obj.year) + '-'
		if date_obj.month < 10:
			date_string += '0'
		date_string += str(date_obj.month) + '-'
		if date_obj.day < 10:
			date_string += '0'
		date_string += str(date_obj.day)
		return date_string
	'''
	def parse_results(self):
		if self.results != {}:
			#with open('../json/twitterData.json', 'w') as outfile:
			print(self.results)
				#json.dump(self.results, outfile, indent=4)
