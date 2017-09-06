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

print ('start')

def get_sentence():
    print('get sentence')
    f = open("speech.txt")
    sentence = f.read().split('.')
    get_sentence.status = random.choice(sentence) + '.'
    print('got sentence')

def get_previous_post():
    raw = api.user_timeline(user_id = 'robo_skellington', count = 1, page = 1)
    for status in raw:
        get_previous_post.post = status.text

def format_post(new_post, old_post):
    format_post.set_new=set(map(lambda word: word.lower(), new_post.split(' ')))
    format_post.set_old=set(map(lambda word: word.lower(), old_post.split(' ')))
    format_post.new_post_string=str(new_post.split(' '))


while True:
    get_sentence()
    get_previous_post()
    format_post(get_sentence.status, get_previous_post.post)
    while format_post.set_old == format_post.set_new:
            print('Post is same, Now changing')
            get_sentence()
            get_previous_post()
            format_post(get_sentence.status, get_previous_post.post)
            time.sleep(1)
    print('Sentence is new')

    while len(format_post.new_post_string) >= 140:
        print('Post is large, changing now')
        get_sentence()
        get_previous_post()
        format_post(get_sentence.status, get_previous_post.post)
        time.sleep(1)
    print('success')
    print(get_sentence.status)
    api.update_status(get_sentence.status)
    time.sleep(7200)
