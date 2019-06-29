# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:14:23 2019

@author: DeveshKataria
"""

import tweepy
from textblob import TextBlob
import pandas as pd

Banks = ['Yes Bank', 'HDFC Bank', 'ICICI Bank', 'Indusind Bank']
Sentiments = []

consumer_key = 'IHJadx4KIYYZIBpbYSZ9MZrmC'
consumer_secret = '1l4UEZDycwf4JtS5fwtCEvDT3eUYVGF8VR5uy7PF90Y2QqX3lR'
access_token = '1144925802351353857-0Yv32NFulkZ9ZF2XG2yQRw57dovwKA'
access_token_secret = '6JHlaOdRBcasDohaAAjbNIom9eatQPVnVdleLvyuznLHI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for bank in Banks:
	public_tweets = api.search(bank)
	sents = []
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		sents.append(analysis.sentiment[0])
	Sentiments.append(sum(sents) / len(sents))
	

print(Sentiments)
df = pd.DataFrame({'Bank Name': Banks, 'Trend': Sentiments})
df.to_csv(r'C:\Users\DeveshKataria\Desktop\trend.csv', index = False)

