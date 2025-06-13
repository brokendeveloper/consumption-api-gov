import requests
from config import BASE_URL, HEADERS

class APIClient:
    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()