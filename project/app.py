import tweepy
from dotenv import load_dotenv
import os
load_dotenv()

class App():
    def __init__(self, api = None, content_extractor = None, image_downloader = None):
        self.api = api
        self.content_extractor = content_extractor
        self.image_downloader = image_downloader

    def create_api_instance(self):
        api_key = os.getenv("TWITTER_API_KEY")
        api_key_secret = os.getenv("TWITTER_API_KEY_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def update_profile(self):
        content = self.content_extractor.get_content()
        if not content: return
        self.image_downloader.download_image(content.imageURL)

        text = f'Banner photo: {content.title}\nCopyright: {content.copyright}\nfrom: https://apod.nasa.gov/apod/astropix.html'
        self.api.update_profile_banner(filename = 'tmp/banner.jpg')
        self.api.update_profile(description = text)