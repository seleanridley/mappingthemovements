'''
	Contributors: Emily Simoneau and Cameron Bates
'''
#from . import APICall
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
##from datetime import date, datetime

class TwitterAPI():
	def __init__(self):
		#APICall.__init__(self)
		self.creds = {"ACCESS_TOKEN": "80730868-mdZXRx2An0GpP5U2hVGQltqjpyTEeKSUG9wITCbSL", "ACCESS_SECRET": "gjIdGLRVc3H0CSHztY8ZYcU9gReUA9FSWIBRMZXB1MvEe", "CONSUMER_SECRET": "zAf2cvPkAr3hy527OBmVopkpRwJpGKN0viy8GZSzVxyFW8ksch", "CONSUMER_KEY": "duuKptCTsD3rt7ZvGlyUg95KQ"}


	def search(self, keyword, date_start, date_end):
		self.results = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'user_loc':[], 'retweet_count':[]}
		self.eg_results = {"results" : []};
		self.wc_results = {'count' : {}};
		self.lc_results = {'count' : {}};
		oauth = OAuth(self.creds['ACCESS_TOKEN'], self.creds['ACCESS_SECRET'], self.creds['CONSUMER_KEY'], self.creds['CONSUMER_SECRET'])
		twitter = Twitter(auth=oauth)
		##date_start_str = self.date_to_string(date_start)
		##date_end_str = self.date_to_string(date_end)
		for status in twitter.search.tweets(q=keyword, until=date_end, since=date_start, result_type='popular', count=100)['statuses']:
			self.results['user'].append(status['user']['screen_name'])
			print('Please be here')
			self.results['date'].append(status['created_at'])
			self.results['text'].append(status['text'])
			self.results['favorite_count'].append(status['favorite_count'])
			self.results['user_loc'].append(status['user']['location'])
			self.results['retweet_count'].append(status['retweet_count'])
			self.eg_results["results"].append({"date": status['created_at'], "engagement": status['favorite_count'] + status['retweet_count']});
		self.format_data()

	def format_data(self) :
		words = []
		locs = []
		freq = []
		locs_freq = []
		tweets = self.results["text"]
		locations = self.results["user_loc"]
		for tweet in tweets:
			split_content = tweet.split(" ")
			for word in split_content:
				if word in words:
					freq[words.index(word)] = freq[words.index(word)] + 1
				else:
					freq.append(1)
					words.append(word)
		for location in locations:
			if location in locs:
				locs_freq[locs.index(location)] = locs_freq[locs.index(location)] + 1
			else:
					locs_freq.append(1)
					locs.append(location)
		max_value = max(freq)
		max_loc = max(locs_freq)
		index = 0
		for entry in freq:
			self.wc_results['count'][words[index]] = entry
			index = index + 1
		index = 0
		for entry in locs_freq:
			self.lc_results['count'][locations[index]] = entry
			index = index + 1

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
			with open('static/json/twitterData.json', 'w') as outfile:
				json.dump(self.results, outfile, indent = 4)
		if self.wc_results != {}:
			with open('static/json/twitterWCData.json', 'w') as outfile:
				json.dump(self.wc_results, outfile, indent = 4)
		if self.lc_results != {}:
			with open('static/json/twitterLCData.json', 'w') as outfile:
				json.dump(self.lc_results, outfile, indent = 4)
		if self.eg_results != {}:
			with open('static/json/twitterEGData.json', 'w') as outfile:
				json.dump(self.eg_results, outfile, indent = 4);
