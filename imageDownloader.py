import requests
import os

class imageDownloader():
    def __init__(self):
        pass

    def download_image(self, url):
        img_data = requests.get(url).content
        if not os.path.exists('tmp'): os.makedirs('tmp')
        with open('tmp/image_name.jpg', 'wb') as handler:
            handler.write(img_data)
        