# Dependencies
import pandas as pd
import tweepy
import time
import json
import random

# Twitter API Keys
consumer_key = "NB1KzKcTYMPR8sZGFnzMIoD18"
consumer_secret = "NsMmuCXATKwZpbsmLsDi96WO8PtEgX5njh5JpwhvK0vPPLkOgp"
access_token = "710461777650257921-SbIP6gQLT9kUVQrVX4Kp4C78E2DsFPO"
access_token_secret = "2MKRCLFHh82iv0gJGmVyritpvdH3NpkEx0ZQEwoxlngsE"

# Quotes to Tweet
happy_quotes = [
    'If you want to achieve greatness stop asking for permission. ~Anonymous',
	'Things work out best for those who make the best of how things work out. ~John Wooden',
	'To live a creative life, we must lose our fear of being wrong. ~Anonymous',
	'If you are not willing to risk the usual you will have to settle for the ordinary. ~Jim Rohn',
	'Trust because you are willing to accept the risk, not because it’s safe or certain. ~Anonymous',
	'The function of leadership is to produce more leaders, not more followers. ~Ralph Nader',
	'Success is liking yourself, liking what you do, and liking how you do it. ~Maya Angelou',
	'As we look ahead into the next century, leaders will be those who empower others. ~Bill Gates',
	'A real entrepreneur is somebody who has no safety net underneath them. ~Henry Kravis',
	'Take up one idea. Make that one idea your life - think of it, dream of it, live on that idea. Let the brain, muscles, nerves, every part of your body, be full of that idea, and just leave every other idea alone. This is the way to success. ~Swami Vivekananda',
	'All our dreams can come true if we have the courage to pursue them. ~Walt Disney'
	# 'Good things come to people who wait, but better things come to those who go out and get them. ~Anonymous',
	# 'If you do what you always did, you will get what you always got. ~Anonymous'
	]

# Create function for tweeting

# Create a function that tweets
def TweetOut(tweet):
	try:
		# Twitter credentials
		# Setup Tweepy API Authentication
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

		# tweet = random.choice(tweets)
		api.update_status(tweet)   

		# Print success message
		print("I twitted: %s" % tweet)

	except:
		print("Duplicate")


# Tweet a random quote

for quote in happy_quotes:
	TweetOut(quote)

# Set timer to run every minute
	time.sleep(60)
