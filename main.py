import tweepy
import os
from dotenv import load_dotenv

load_dotenv()


api_key=os.getenv("API")
api_key_secret=os.getenv("API_SECRET")
access_token=os.getenv("ACCESS")
access_token_secret=os.getenv("ACCESS_SECRET")

def get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret) -> tweepy.API:
    """Get twitter conn 1.1"""

    auth = tweepy.OAuth1UserHandler(api_key, api_secret)
    auth.set_access_token(
        access_token,
        access_token_secret,
    )
    return tweepy.API(auth)

def get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret) -> tweepy.Client:
    """Get twitter conn 2.0"""

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client

def get_media

client_v1 = get_twitter_conn_v1(api_key, api_key_secret, access_token, access_token_secret)
client_v2 = get_twitter_conn_v2(api_key, api_key_secret, access_token, access_token_secret)

media_path = "myimage.jpg"
media = client_v1.media_upload(filename=media_path)
media_id = media.media_id

client_v2.create_tweet(text="", media_ids=[media_id])
