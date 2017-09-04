# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:23:07 2017

@author: mojod
"""

	
import random
import tweepy

consumer_key='L3MsyCOoqgSPc4jzZV8wero0d'
consumer_secret='ZCOI3x1f8GZ9c2cJ8kPYyyBW4gRX4MJBbyHijGE1UObnAow6ka'
access_token='3789452353-dmM75KVaDGqIPz6ZtzP8b5Q6VkvzQQo9Sn34ZOZ'
access_token_secret='JvYlzlqM3AHj7IXSMMoIgS0A8auqzI1KyMjKnJeT3gn8w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

f = open("speech.txt")
sentence = f.read().split('.')
status = random.choice(sentence) + "."

print(status)

api.update_status(status)
f.close