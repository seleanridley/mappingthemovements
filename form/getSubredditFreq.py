import praw
import json

subList = {}
subList = []

totalSubmissions = {}
totalSubmissions = []

worldnewsTotal = 0
politicsTotal = 0
totalSubs = 0

with open('../json/redditData.json') as jsonFile:
    data = json.load(jsonFile)
    for i in data['submissions']:
        if i['subreddit'] == 'worldnews':
            worldnewsTotal += 1
            totalSubs += 1
        if i['subreddit'] == 'politics':
            politicsTotal += 1
            totalSubs += 1
            
subList.append({
    'subreddit': 'worldnews',
    'frequency': worldnewsTotal
    })

subList.append({
    'subreddit': 'politics',
    'frequency': politicsTotal
    })

totalSubmissions.append({
    'totalSubs': totalSubs
    })

with open('../json/subredditFreq.json', 'w') as outfile:
    json.dump(subList, outfile)
    
with open('../json/totalSubmissions.json', 'w') as outfile:
    json.dump(totalSubmissions, outfile)