import json
import os
import tweepy

from hashtags import getTopics
from tweets import getTweets

def lambda_handler(event, context):
        functiontype = event['type']
        tweet_number = event ['no']
        time = event['time']
    
        api_key = os.environ['APIKEY']
        api_secret = os.environ['APISECRET']
        api_bearer_token = os.environ['APIBEARER']
        api_access_token = os.environ['APIACCESSTOKEN']
        api_secret_access_token = os.environ['APISECRETACCESSTOKEN']
        
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(api_access_token, api_secret_access_token)

        api = tweepy.API(auth)
        
        if functiontype == "tweet":
                tweets = getTweets(tweet_number, api,time)
        elif functiontype == "hashtag":
                trends = getTopics(tweet_number, api)
        
    

