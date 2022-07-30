import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('NASA_API_KEY')

class Content():
    def __init__(self, title = None, copyright = None, imageURL = None):
        self.title = title
        self.copyright = copyright
        self.imageURL = imageURL

class NASAContentExtractor():
    def __init__(self):
        pass

    def get_content(self):
        json = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').json()
        if json['media_type'] != 'image':
            return None

        title = json['title']
        copyright = json['copyright']
        imageURL = json['hdurl']
        content = Content(title, copyright, imageURL)
        return content
