# users: list = [
# #     {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3, 'coord': [52.23, 21.0], 'img_url': ""},
# #     {'name': 'Asia', 'location': 'Kraków', 'posts': 5, 'coord': [50.0, 19.9], 'img_url': ""},
# #     {'name': 'Bsia', 'location': 'Wrocław', 'posts': 7, 'coord': [51.0, 17.0], 'img_url': ""},
# ]

import requests
from bs4 import BeautifulSoup

class User:
    def __init__(self, name: str, location: str, posts: int, img_url: str):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_coordinates()
        self.marker = None

    def get_coordinates(self):
        url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/123.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, "html.parser")
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        return [latitude, longitude]
