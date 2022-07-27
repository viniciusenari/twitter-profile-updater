import requests

class Content():
    def __init__(self, title = None, imageURL = None):
        self.title = title
        self.imageURL = imageURL

class NASAContentExtractor():
    def __init__(self):
        pass

    def getContent(self):
        json = requests.get('https://api.nasa.gov/planetary/apod?api_key=fa1X4GIO4HhAn3r1k28nR18Kt8Yd5hU44JWM9Suc').json()
        
        title = json['title']
        imageURL = json['hdurl']

        content = Content(title, imageURL)
        return content
