from . import NewsAPI
from . import redditAPI
from . import TwitterAPI
import json
from datetime import date, datetime
import time

'''
	Contributors: Chris Lau and Cameron Bates
'''
class SearchParam(object):
	def __init__(self, start_date, end_date, keyword, twitter, reddit):
		self.startDate = datetime.strptime(start_date, '%m/%d/%Y').date()
		self.endDate = datetime.strptime(end_date, '%m/%d/%Y').date()
		self.keyword = keyword
		if twitter and not reddit:
			self.platform = 'Twitter'
		elif reddit and not twitter:
			self.platform = 'Reddit'
		else:
			self.platform = None #throw an error!

	def runSearch(self):
		startDate_str = self.startDate.strftime('%Y-%m-%d')
		endDate_str = self.endDate.strftime('%Y-%m-%d')

		##News API
		news_api = NewsAPI.NewsAPI()
		news_api.search(self.keyword, startDate_str, endDate_str)
		news_api.parse_results()

		##Social Media API
		if self.platform == 'Twitter': ##run twitter search
			twitter_api = TwitterAPI.TwitterAPI()
			twitter_api.search(self.keyword, startDate_str, endDate_str)
			twitter_api.parse_results()


		elif self.platform == 'Reddit': ##run reddit search
			reddit_api = redditAPI.RedditAPI()
			reddit_api.search(self.keyword, self.startDate, self.endDate)
			reddit_api.parse_results()
