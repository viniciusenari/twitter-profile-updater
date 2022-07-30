from project import App, imageDownloader, NASAContentExtractor

if __name__ == "__main__":
    content_extractor = NASAContentExtractor()
    image_downloader = imageDownloader()

    app = App(content_extractor=content_extractor, image_downloader=image_downloader)
    app.create_api_instance()
    app.update_profile()