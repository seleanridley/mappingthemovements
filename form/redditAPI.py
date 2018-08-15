'''
	Contributors: Chris Lau and Cameron Bates
'''

from datetime import date, datetime
import praw
import json
#from . import APICall

class RedditAPI():

	def __init__(self):
		self.reddit = praw.Reddit(user_agent = 'userAgent', client_id = 'Wtyt6ZzLdbI6NA', client_secret = '3BxHtc7XdjL28i-xRS_NQPMV_P4')
		self.subData = {}
		self.subData['submissions'] = []
		#self.subData['todaySubs'] = []

	def get_date(self, submission):
		time = submission.created
		return date.fromtimestamp(time)

	def get_datetime(self, submission):
		time = submission.created
		return datetime.fromtimestamp(time)

	def search(self, keyword, date_start, date_end):
		#print('in reddit search')
		for submission in self.reddit.subreddit('politics+worldnews').top(limit = None):
			#print('in for loop!')
			if keyword.lower() in str(submission.title).lower() and (self.get_date(submission) > date_start and self.get_date(submission) < date_end):
				#print('in if statement')
				self.subData['submissions'].append({
					'title': str(submission.title),
					'subreddit': str(submission.subreddit),
					'score': int(submission.score),
					'comments': int(submission.num_comments),
					'date created': str(self.get_date(submission))
				})

	def search_today(self, keyword):
		for submission in reddit.subreddit('politics+worldnews').top(time_filter = 'day', limit = None):
			if keyword.lower() in str(submission.title).lower():
				self.subData['todaySubs'].append({
					'title': str(submission.title),
					'subreddit': str(submission.subreddit),
					'score': int(submission.score),
					'comments': int(submission.num_comments),
					'time created': str(self.get_datetime(submission).time())
				})

	def parse_results(self):
		print(self.subData)
		with open('static/json/redditData.json', 'w') as outfile:
			json.dump(self.subData, outfile, indent=4)

'''
search = SearchParam()
addParams(search)

getSubmissions(search.keyword, search.startDate, search.endDate)

with open('../json/redditData.json', 'w') as outfile:
    json.dump(subData, outfile)
'''
