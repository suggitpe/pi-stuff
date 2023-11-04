import configparser
import requests
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient

HEADERS = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

def configuration():
    config = configparser.ConfigParser()
    config.read('config.txt')
    return config

def create_db_client():
    cfg = configuration()
    return InfluxDBClient(host=cfg.get('influxdb', 'host'),
                          port=cfg.get('influxdb', 'port'),
                          username=cfg.get('influxdb', 'user'),
                          password=cfg.get('influxdb', 'pass'),
                          database='amazonprices')

def create_data(name, price):
    return [
        {
            "measurement": "amazon_price",
            "tags": {
                "host": "RaspberryPiMyLifeUp"
            },
            "fields": {
                "name": name[:50],
                "price": float(price)
            }
        }
    ]

def get_prices():
    client = create_db_client()
    with open('trackurls.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    for url in lines:
        store_price(url, client)

def store_price(url, client):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find('span', class_='a-offscreen').get_text().replace('£', '')
    print(create_data(title, price))

if __name__ == "__main__":
    get_prices()
