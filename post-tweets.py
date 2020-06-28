

								###using twython post tweets on twitter
from twython import Twython
APP_KEY="consumer_key"
APP_SECRET="consumer_secret_key"
OAUTH_TOKEN="authentication_token"
OAUTH_TOKEN_SECRET="authentication_secret_token"
twi = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twi.update_status(status='Twython status test')



								###using tweepy post tweets on twitter
# importing the module 
import tweepy 

# personal details 
consumer_key ="consumer_key"
consumer_secret ="consumer_secret_key"
access_token ="authentication_token"
access_token_secret ="authentication_secret_token"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

# update the status 
api.update_status(status ="Hello Everyone !") 
