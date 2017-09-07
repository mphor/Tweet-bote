import markovify
import tweepy
import time

consumer_key='L3MsyCOoqgSPc4jzZV8wero0d'
consumer_secret='ZCOI3x1f8GZ9c2cJ8kPYyyBW4gRX4MJBbyHijGE1UObnAow6ka'
access_token='3789452353-dmM75KVaDGqIPz6ZtzP8b5Q6VkvzQQo9Sn34ZOZ'
access_token_secret='JvYlzlqM3AHj7IXSMMoIgS0A8auqzI1KyMjKnJeT3gn8w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_sent():
    f = open("speech.txt")
    f = f.read()
    text_model = markovify.Text(f, retain_original=True)
    get_sent.sent = text_model.make_short_sentence(140)
    get_sent.hash = ' #' + get_sent.sent
    print(get_sent.hash)


while True:
    get_sent()
    #api.update_status(get_sent.hash)
    time.sleep(1)
