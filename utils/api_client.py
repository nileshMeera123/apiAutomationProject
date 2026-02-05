import requests
import configparser
import os

class APIClient:

    def __init__(self):
        config = configparser.ConfigParser()
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )
        config.read(config_path)

        self.base_url = config.get("API", "base_url")
        api_key = config.get("API", "api_key")
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": api_key
        }

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.headers)

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json=payload,headers=self.headers)

    def put(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, json=payload,headers=self.headers)

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url,headers=self.headers)