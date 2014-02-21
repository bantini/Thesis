import tweepy

public_tweets = tweepy.api.public_timeline()
opener = open("public.txt","a+")
for tweet in public_tweets:
	tweet = data.split(',"text":"')[1].split('","source')[0]
	opener.write(tweet)

opener.close()
    
