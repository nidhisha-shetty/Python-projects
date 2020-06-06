

								###using twython post tweets on twitter
from twython import Twython
APP_KEY="r84tfRQsecYZO7XIvfJFlR8Fn"
APP_SECRET="zCTENpUJXqzB8eG3gQcySKd2g6CsG3CPn0bRMFwvBdJyJIk8qK"
OAUTH_TOKEN="927454279585087489-1XINu6ol8fjWbx9xcIWq2gXQzwC6P2n"
OAUTH_TOKEN_SECRET="LoR6KMYJCNQCtvTWtdxKCrnareeqZ2sYRYWcZb6qwJgQI"
twi = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twi.update_status(status='Twython status test')



								###using tweepy post tweets on twitter
# importing the module 
import tweepy 

# personal details 
consumer_key ="r84tfRQsecYZO7XIvfJFlR8Fn"
consumer_secret ="zCTENpUJXqzB8eG3gQcySKd2g6CsG3CPn0bRMFwvBdJyJIk8qK"
access_token ="927454279585087489-1XINu6ol8fjWbx9xcIWq2gXQzwC6P2n"
access_token_secret ="LoR6KMYJCNQCtvTWtdxKCrnareeqZ2sYRYWcZb6qwJgQI"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

# update the status 
api.update_status(status ="Hello Everyone !") 
