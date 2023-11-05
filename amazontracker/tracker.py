import configparser
import requests
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient

HEADERS = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
# HEADERS = {    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'}
# HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}

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



def get_prices():
    client = create_db_client()
    with open('trackurls.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    for url in lines:
        store_price(url, client)

def store_price(url, client):
    page = requests.get(url, headers=HEADERS)
    if check_for_captcha(page.text):
        print("Found captcha for ", url)
        return
    data = create_data_from_page(page)
#     client.write_points(data)
    print(data)

def check_for_captcha(page_text):
    return page_text.find('Type the characters you see in this image') > 1

def create_data_from_page(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find('span', class_='a-offscreen').get_text().replace('£', '')
    return create_data(title, price)

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



if __name__ == "__main__":
    get_prices()
