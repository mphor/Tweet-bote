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
print ('start')

def post_func():
    #get text from json of recent post
    raw = api.user_timeline(user_id = 'robo_skellington', count = 1, page = 1)
    ######
    for status in raw:
        format_status = status.text
    ######
    #get random quote from txt file
    sentence = f.read().split('.')
    status = random.choice(sentence) + '.'
    #make strings comparable
    set_sentence=set(map(lambda word: word.lower(), status.split(' ')))
    set_status=set(map(lambda word: word.lower(), format_status.split(' ')))
    #make sure quote is within size AND not equal to previous post
    while len(status) > 139 or len(status) < 6 or set_status == set_sentence:
        ######
        status=random.choice(sentence)+'.'
        ######
        set_sentence=set(map(lambda word: word.lower(), status.split(' ')))
        ######
        print('Error! Trying again')
        ######
    #make status post
    #api.update_status(status)
    print('New Post')

var = 1
while var == 1 :
    post_func()
    time.sleep(1800)
