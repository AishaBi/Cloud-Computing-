import datetime
import tweepy
import time
from collections import OrderedDict
import boto3
import json
from twitterwordcloud import plot_cloud

def getTweets(amount, api,tweettime):
    tweet_list = []
    retweet_list= []
    counter=1
    
    for _ in range(tweettime*2):
        tweetsearch = api.search(q="lockdown", count=amount, lang="en")
        for tweet in tweetsearch:
            tweet_list.append(tweet.text)
            retweet_list.append(tweet.retweet_count)
        tweet_list_sorted = sort_tweets(tweet_list, retweet_list, amount)
        save_to_bucket(tweet_list_sorted)
        time.sleep(30)
    return tweets_list_sorted

def sort_tweets(tweet_list, retweet_list, amount):
    #sorting algorithm - zip them togther to sort the tweet volume
    retweet_list,tweet_list = (list(t) for t in zip(*sorted(zip(retweet_list, tweet_list), reverse=True)))
    #trim the list to get the correct amount of tweets
    retweet_list = retweet_list[0:amount]
    tweet_list = tweet_list[0:amount]
    tweetcloud(tweet_list)
    tweets_by_date = dict(zip(retweet_list,tweet_list))
    return tweets_by_date

def tweetcloud(list_tweets):
    tweetstring = ""
    for tweet in list_tweets:
        tweetstring += " "+str(tweet)
    plot_cloud(tweetstring, 'tweets-wordcloud.png')
                
def save_to_bucket(tweets_to_save):
    BUCKET_NAME = "tweetsbucket0301"
    s3_bucket = boto3.client('s3')
    with open('/tmp/tweetlistsfile.txt', 'w') as f:
        print(tweets_to_save, file=f)
    s3_bucket.upload_file('/tmp/tweetlistsfile.txt', BUCKET_NAME, 'tweetlistsfile.txt')    
