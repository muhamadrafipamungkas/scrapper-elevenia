import requests
from bs4 import BeautifulSoup, Tag

class ScrapperElevenia:
    url = None
    price = None

    def __init__(self, url):
        self.url = url
    def getPrice(self):
        try:
            s = requests.Session()
            page = s.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
            self.price = soup.find(attrs={'price notranslate'}).get_text()
            print(self.price)

        except:
            print("Gagal")