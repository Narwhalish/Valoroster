import requests


class APICaller:
    BASE_URL = "https://liquipedia.net/valorant/api.php"
    BASE_PARAMS = {"action": "parse", "format": "json"}

    def __init__(self):
        self.response = requests.get(self.BASE_URL, params=self.BASE_PARAMS)

        if self.response.status_code != 200:
            raise Exception("API call failed")

    def get_page(self, page_name):
        self.response = requests.get(
            self.BASE_URL, params=self.BASE_PARAMS | {"page": page_name}
        )

    def get_json(self):
        return self.response.json()
