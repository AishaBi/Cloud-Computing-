import boto3
import json
from twitterwordcloud import plot_cloud
import matplotlib.pyplot as plt

def getTopics(amount, api):
        data = api.trends_place(23424975)
        trends = []
        for trend in data[0]['trends']:
                trends.append((trend['name'], trend['tweet_volume']))
        trends = trends[0:amount]
        print("count:" + str(len(trends)))
        print(trends)
        hashcloud(trends)
        save_to_bucket(trends)
        return trends
        
def hashcloud(trendcloud):
    # wordcloud
    wordstring = ""
    for trend in trendcloud:
            wordstring += " "+str(trend[0])
    plot_cloud(wordstring, 'hashcloud.png')
    
def save_to_bucket(trends_to_save):
    BUCKET_NAME = "tweetsbucket0301"
    s3_bucket = boto3.client('s3')
    with open('/tmp/hashtaglist.txt', 'w') as f:
        print(trends_to_save, file=f)
    s3_bucket.upload_file('/tmp/hashtaglist.txt', BUCKET_NAME, 'hashtaglist.txt') 
    
    