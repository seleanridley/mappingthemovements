from . import NewsAPI
from . import redditAPI
from . import TwitterAPI
import json
from datetime import date, datetime

'''
	Contributors: Chris Lau and Cameron Bates
'''
class SearchParam(object):
	def __init__(self, start_date, end_date, keyword, twitter, reddit):
		self.startDate = datetime.strptime(start_date, '%d/%m/%Y')
		self.endDate = datetime.strptime(start_date, '%d/%m/%Y')
		self.keyword = keyword
		if twitter and not reddit:
			self.platform = 'Twitter'
		elif reddit and not twitter:
			self.platform = 'Reddit'
		else:
			self.platform = None #throw an error!

	def runSearch(self):
		startDate_str = search_param.startDate.strftime('%Y-%m-%d')
		endDate_str = search_param.endDate.strftime('%Y-%m-%d')

		##News API
		news_api = NewsAPI()
		news_api.search(search_param.keyword, startDate_str, endDate_str)
		news_api.parse_results()

		##Social Media API
		##if search_param.platform = 'Twitter' run twitter search
		twitter_api = TwitterAPI()
		twitter_api.search(search_param.keyword, startDate_str, endDate_str)
		twitter_api.parse_results()


		##elif search_param.platform = 'Reddit' run reddit search
		reddit_api = RedditAPI()
		reddit_api.search(search_param.keyword, search_param.startDate, search_param.endDate)
		reddit_api.parse_results()
