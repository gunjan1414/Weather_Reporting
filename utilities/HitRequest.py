import json
import logging
import requests


class HitRequest:
    @staticmethod
    def send_post_request(context, url, data):
        try:
            HitRequest.hit_request(context, url, data, "POST")
        except Exception as e:
            logging.error("Error in getting api response ")
            logging.error(str(e))

    @staticmethod
    def hit_request(context, url, data, text):
        response = requests.post(url, data=json.dumps(data))
        return response