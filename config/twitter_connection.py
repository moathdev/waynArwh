import twitter
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

api = twitter.Api(consumer_key=config('TWITTER_CONSUMER_KEY'),
                  consumer_secret=config('TWITTER_CONSUMER_SECRET'),
                  access_token_key=config('TWITTER_ACCESS_TOKEN_KEY'),
                  access_token_secret=config('TWITTER_ACCESS_TOKEN_SECRET'))
