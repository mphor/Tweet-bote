# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:23:07 2017

@author: mojod
"""


import random
import tweepy
import time

consumer_key='L3MsyCOoqgSPc4jzZV8wero0d'
consumer_secret='ZCOI3x1f8GZ9c2cJ8kPYyyBW4gRX4MJBbyHijGE1UObnAow6ka'
access_token='3789452353-dmM75KVaDGqIPz6ZtzP8b5Q6VkvzQQo9Sn34ZOZ'
access_token_secret='JvYlzlqM3AHj7IXSMMoIgS0A8auqzI1KyMjKnJeT3gn8w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

f = open("speech.txt")
while True:

    raw = api.user_timeline(user_id = 'robo_skellington', count = 1, page = 1)
    #get text from json of recent post
    for status in raw:
        format_status = status.text
    #get random quote from txt file
    sentence = f.read().split('.')
    status = random.choice(sentence) + '.'
    #make sure quote is within size for twitter post
    if len(status) > 140:
        status=random.choice(sentence)+'.'
    #make sure quote is not the same as previous post
    elif format_status == status:
        status=random.choice(sentence)+'.'
    #make status post
    else:
        api.update_status(status)
        print('New Post')
    #wait 1 hour between next post
    time.sleep(3600)
