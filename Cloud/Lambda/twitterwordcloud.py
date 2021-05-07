from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import boto3

def plot_cloud(wordstring,filename):
    BUCKET_NAME = "tweetsbucket0301"
    s3_bucket = boto3.client('s3')
  # Generate word cloud
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon',
    colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(wordstring)
    wordcloud.to_file('/tmp/'+ filename )
    s3_bucket.upload_file('/tmp/'+filename, BUCKET_NAME, filename)
    


