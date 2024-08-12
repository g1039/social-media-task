import threading
import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SocialMediaUtil:
    def __init__(self, *args, **kwargs):
        self.results = {}

    def social_media_count(self, url, platform) -> None:
        res = requests.get(url)

        try:
            response = res.json()
            if isinstance(response, list):
                x = len(response)
                self.results[platform] = x
        except Exception as e:
            logger.error(e)
            self.results[platform] = 0

    def social_media_thread(self):

        twitter = threading.Thread(target=self.social_media_count, args=("https://takehome.io/twitter", "twitter"))
        facebook = threading.Thread(target=self.social_media_count, args=("https://takehome.io/facebook","facebook"))
        instagram = threading.Thread(target=self.social_media_count, args=("https://takehome.io/instagram", "instagram"))

        twitter.start()
        facebook.start()
        instagram.start()

        twitter.join()
        facebook.join()
        instagram.join()
        
        return self.results
