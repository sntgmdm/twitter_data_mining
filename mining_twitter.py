import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json
import config

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

class MyListener (StreamListener):
    def on_status(self, status):
        print(status.text)
'''
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseExcepetion as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error (self, status):
        print (status)
        return True
'''
twitter_stream = Stream(auth, MyListener())

'''
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
'''
