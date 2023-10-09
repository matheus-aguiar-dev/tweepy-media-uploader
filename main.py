import tweepy
import os
import time
import random
import shutil
from dotenv import load_dotenv

load_dotenv()


api_key=os.getenv("API")
api_key_secret=os.getenv("API_SECRET")
access_token=os.getenv("ACCESS")
access_token_secret=os.getenv("ACCESS_SECRET")
folder_path = "/home/kriza/projetos/twitter-dowloader/twitter-media-downloader-v1.10.1-linux-386/filter/pink-filter/edited"
destination_folder_path = "kissmeshawtys"

def get_twitter_conn_v1(api_key, api_secret, access_token, access_token_secret) -> tweepy.API:

    auth = tweepy.OAuth1UserHandler(api_key, api_secret)
    auth.set_access_token(
        access_token,
        access_token_secret,
    )
    return tweepy.API(auth)

def get_twitter_conn_v2(api_key, api_secret, access_token, access_token_secret) -> tweepy.Client:

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client


client_v1 = get_twitter_conn_v1(api_key, api_key_secret, access_token, access_token_secret)
client_v2 = get_twitter_conn_v2(api_key, api_key_secret, access_token, access_token_secret)

while True:
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if files:
        random_file = random.choice(files)
        random_file_path = os.path.join(folder_path, random_file)
        media = client_v1.media_upload(filename=random_file_path)
        media_id = media.media_id
        client_v2.create_tweet(text="", media_ids=[media_id])
        time.sleep(2)
        shutil.move(random_file_path, os.path.join(destination_folder_path, random_file))
        time.sleep(10800)
    else:
        print("No files found in the folder.")



