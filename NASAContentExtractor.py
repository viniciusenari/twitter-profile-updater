import requests

class Content():
    def __init__(self, title = None, copyright = None, imageURL = None):
        self.title = title
        self.copyright = copyright
        self.imageURL = imageURL

class NASAContentExtractor():
    def __init__(self):
        pass

    def get_content(self):
        json = requests.get('https://api.nasa.gov/planetary/apod?api_key=fa1X4GIO4HhAn3r1k28nR18Kt8Yd5hU44JWM9Suc').json()
        
        title = json['title']
        copyright = json['copyright']
        imageURL = json['hdurl']

        content = Content(title, copyright, imageURL)
        return content
