import markovify
import tweepy

def markov_maker():
 	with open('') as f: # Load your .txt corpus
		text = f.read()
	text_model = markovify.Text(text)	# Create a Markov model
	tweet_maker(text_model)	# Send model to sentence-maker

def tweet_maker(text_model):
	content = text_model.make_short_sentence(150) # Change to adjust length. 150 was fine for tweets with my corpus
	if any(char.isdigit() for char in content) is True: # Make sure we didn't get page numbers, and run again if we did
		tweet_maker(text_model)
	else:
		print content	# Comment this out and uncomment below to send actual tweets
# 		send_tweet(content) # Run it again if there were numbers
				
def send_tweet(content):
	CONSUMER_KEY = '' # Fill in with your details from twitter
	CONSUMER_SECRET = '' # Fill in with your details from twitter
	ACCESS_KEY = '' # Fill in with your details from twitter
	ACCESS_SECRET = '' # Fill in with your details from twitter
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) # Access stuff for the API
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	try:
		api.update_status(status=content) # Send the tweet
	except tweepy.error.TweepError:	
		api.update_status(status=content[:139]) # If the tweet is too long, cut it so it fits
		
if __name__ == '__main__':
	markov_maker()
	
