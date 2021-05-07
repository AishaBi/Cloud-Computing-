import boto3
import json
from multiprocessing import Process
import ast
import time as clock

#triggers the lambdafunction - this waits for response however we need this program to do more than just this simultaneously so we use multiprocessing
def trigger(lambdafunction):
	
	#name of the aws function which we will get the tweet information from
	lambda_function_name = "getTweets"
	#aws credentials
	AWS_ACCESS_KEY="ASIAS4XF3HVO6DFOWH4Z"
	AWS_SECRET_ACCESS_KEY="LhAJkf01J27kCP1dxx1y0FM1E50DlLuLjs/ydzbj"
	AWS_REGION="us-east-1"
	AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEL3//////////wEaCXVzLXdlc3QtMiJIMEYCIQCxhHnhyBLxRKA+1RUx50YGqcaC/hVPEgrhEOZbZ0fK/AIhAK3QW7zbglrizH2KWsMkaD8MCTNr+XLqEb563XShEcRDKrQCCEYQABoMMTk5MTI0MjcwNDI5Igw+jGk3dC7ZXqlmZRoqkQL9bls4oVHFEYgeQ/nQVlQnPnU6dUyH3hfR0VrSGYJThrreNHlXHJIcKVl+eO9+vaDba1+lPeYEYaykCgt4zlhbkxBDGqDA8CYGlKN3owoWp02XlSP3jaBKK+ZBAiv323ufcyK3ghHi9h+8o4jsFUAX8sSJtwnCg9OOjp0D92NlGsOlUuZjKF/RIPKoaM546xOgnxZi6sDsEVxZtoROCpvRZUxW7+f/bNlzdGMy5twmvSSANnAmjPqarmCSqKK1N9kSrucvqDA9jhB+yxQ7nUdhcQbsG0t/Xq7V+SfIyMsKjdK5/AXKHeFzAtvzp6EA5ooyP+mNv1sMaCINL1UK+jEwj/IIJf8dXU0HcpveGhib1aIwnvPUhAY6nAEGszE9QchbwTDT+aFEbhXROdjKmrW7CW5zEcIYtqOsHb4qSiN5gCvHDKqhTGU/0QxHpYHGgrfFLTFW0X5p52KmUzyGSPPSWoqUVOIkUY9a6EzcJ3IK5co3EGOaB69/qmhXV204020vBuJvOpx5FjWPHoK0lMpmRf0Fnjcybl7Y0RRvFD8raNXn+YE71O0aIeXvn/JtcIx2+uLG09M="
	#create client to connect to lambda function
	client = boto3.client('lambda',
							region_name=AWS_REGION,
							aws_access_key_id= AWS_ACCESS_KEY,
							aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
							aws_session_token= AWS_SESSION_TOKEN)


	result = client.invoke(FunctionName="arn:aws:lambda:us-east-1:199124270429:function:getTweets",
	InvocationType='RequestResponse',
	Payload=json.dumps(lambdafunction))
	#print(result)
	
if __name__ == '__main__':

#these must be kept up to data because they expire
	AWS_ACCESS_KEY="ASIAS4XF3HVO6DFOWH4Z"
	AWS_SECRET_ACCESS_KEY="LhAJkf01J27kCP1dxx1y0FM1E50DlLuLjs/ydzbj"
	AWS_REGION="us-east-1"
	AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEL3//////////wEaCXVzLXdlc3QtMiJIMEYCIQCxhHnhyBLxRKA+1RUx50YGqcaC/hVPEgrhEOZbZ0fK/AIhAK3QW7zbglrizH2KWsMkaD8MCTNr+XLqEb563XShEcRDKrQCCEYQABoMMTk5MTI0MjcwNDI5Igw+jGk3dC7ZXqlmZRoqkQL9bls4oVHFEYgeQ/nQVlQnPnU6dUyH3hfR0VrSGYJThrreNHlXHJIcKVl+eO9+vaDba1+lPeYEYaykCgt4zlhbkxBDGqDA8CYGlKN3owoWp02XlSP3jaBKK+ZBAiv323ufcyK3ghHi9h+8o4jsFUAX8sSJtwnCg9OOjp0D92NlGsOlUuZjKF/RIPKoaM546xOgnxZi6sDsEVxZtoROCpvRZUxW7+f/bNlzdGMy5twmvSSANnAmjPqarmCSqKK1N9kSrucvqDA9jhB+yxQ7nUdhcQbsG0t/Xq7V+SfIyMsKjdK5/AXKHeFzAtvzp6EA5ooyP+mNv1sMaCINL1UK+jEwj/IIJf8dXU0HcpveGhib1aIwnvPUhAY6nAEGszE9QchbwTDT+aFEbhXROdjKmrW7CW5zEcIYtqOsHb4qSiN5gCvHDKqhTGU/0QxHpYHGgrfFLTFW0X5p52KmUzyGSPPSWoqUVOIkUY9a6EzcJ3IK5co3EGOaB69/qmhXV204020vBuJvOpx5FjWPHoK0lMpmRf0Fnjcybl7Y0RRvFD8raNXn+YE71O0aIeXvn/JtcIx2+uLG09M="
	

	#Command line user interface
	print('Please select: \n 1 - Show tweets 	\n 2 - Show hashtags \n 3 - Tweet wordcloud \n 4 - Hashtag wordcloud' )
	option = input()

	if option == '1':
		lambda_type = "tweet"
		print('How many tweets would you like to see? \n Please enter: 10,50 or 100')
		number = input()
		print('Please enter the time frame of this search \n Select how many minutes: 10, 30 or 60, please wait 30 seconds for the results')
		time = input()
				  
	elif option == '2':
		lambda_type = "hashtag"
		print('How many hashtage would you like to see? \n Please enter: 10,30 or 50')
		number = input()
		print('Please enter the time frame of this search \n Select how many minutes: 10, 30 or 60')
		time = input()

	elif option == '3':
		print('Please click link below to open the tweets wordcloud: \n https://tweetsbucket0301.s3.amazonaws.com/tweets-wordcloud.png')

	elif option == '4':
		print('Please click link below to open the hashtag wordcloud: \n https://tweetsbucket0301.s3.amazonaws.com/hashcloud.png')
				  
	else:
		print('error')
		raise Exception("Error")


	#create payload - dictionary
	lambdafunction = {
	"type": lambda_type,
	"no": number,
	"time": time
	}
	

	#multithreading, starting the process, runs another process at the same time triggering lambda function
	p = Process(target=trigger,args=(lambdafunction,))
	p.start()

	#need program to read the json file with the tweet info on the s3 bucket
	if lambda_type == "tweet":
		clock.sleep(30)

		BUCKET_NAME = "tweetsbucket0301"
		FILE_NAME = "tweetlistsfile.txt"
		s3 = boto3.resource('s3', aws_access_key_id= AWS_ACCESS_KEY,
								aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
								aws_session_token= AWS_SESSION_TOKEN)
		bucket_object = s3.Object(BUCKET_NAME,FILE_NAME)
		bucket_content = bucket_object.get()['Body'].read().decode('utf-8')

		dic_content = ast.literal_eval(bucket_content)

		for retweet, tweet in dic_content.items():
			print("Retweets: " + str(retweet))
			print("Tweet: " + tweet)
			print(" ")

	
	elif lambda_type == "hashtag":
		######################################################
		BUCKET_NAME = "tweetsbucket0301"
		FILE_NAME = "hashtaglist.txt"
		s3 = boto3.resource('s3', aws_access_key_id= AWS_ACCESS_KEY,
								aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
								aws_session_token= AWS_SESSION_TOKEN)
		bucket_object = s3.Object(BUCKET_NAME,FILE_NAME)
		bucket_content = bucket_object.get()['Body'].read().decode('utf-8')

		dic_content = ast.literal_eval(bucket_content)

		for trends in dic_content:
			print("Trend: " + str(trends))
			print(" ")

			#############

	




