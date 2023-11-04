import requests
import configparser
from bs4 import BeautifulSoup

HEADERS = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

config = configparser.ConfigParser()
config.read('config.txt')

# print(config.get('influxdb', 'port'))

def get_prices():
    with open('trackurls.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    for url in lines:
        get_price(url)

def get_price(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find('span', class_ = 'a-offscreen').get_text().replace('£', '')
    print(price, title)

if __name__ == "__main__":
    get_prices()

