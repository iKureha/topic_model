# coding: utf-8


# import _mysql
import tweepy

# Authentication
consumer_key = 'hEfV2WmbpuRZNXdFVNLVP4RAS'
consumer_secret = 'QjHFBvKMycHe1SVXo1LH5WdbXAHlAidFcyZCJ2Kjnyl9HxxYEz'
access_token = '3931387452-uyJ9RD57ixib61QB4Fj1OJEjqxJKTsQ0tmn8Kqa'
access_token_secret = '7q0bhNRJjMNrjvhEoJiEYwfxUbhwXus8HAHV8ECCNokyY'

# Connect to DB
# db = _mysql.connect(host='localhost', user='root', passwd='wangyu123', db='TwitterTest')


def linkToTwitter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api



 
 
