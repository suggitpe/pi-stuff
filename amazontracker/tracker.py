import argparse
import configparser
import random

import requests
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient

USER_AGENT_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
                   'Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.102 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']

#USER_AGENT = random.choice(USER_AGENT_LIST)
USER_AGENT = USER_AGENT_LIST[2]
print("Using agent:", USER_AGENT)
HEADERS = {'User-Agent': USER_AGENT ,'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7', 'referer': 'https://prerender.io/'}

CONFIG_FILE = None

def test_headers(session):
    heads = session.get('http://httpbin.org/headers', headers=HEADERS)
    print(heads.text)
    return

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-c", "--config", help="pass in a config file")
    args = arg_parser.parse_args()
    if args.config is None:
        raise Exception("Need a config file please")
    return args.config


def get_prices():
    db_client = create_db_client()
    with open('urls.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    for url in lines:
        store_price(url, db_client)


def store_price(url, client):
    session = requests.Session()
    test_headers(session)
    page = session.get(url, headers=HEADERS)
    if check_for_captcha(page.text):
        print("Found captcha for ", url)
        return
    data = create_data_from_page(page)
    client.write_points(data)
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
                "host": "statspi"
            },
            "fields": {
                "name": name[:50],
                "price": float(price)
            }
        }
    ]


def create_db_client():
    cfg = configuration()
    return InfluxDBClient(host=cfg.get('influxdb', 'host'),
                          port=cfg.get('influxdb', 'port'),
                          username=cfg.get('influxdb', 'user'),
                          password=cfg.get('influxdb', 'pass'),
                          database='amazonprices')


def configuration():
    print("Reading config from", CONFIG_FILE)
    config_data = configparser.ConfigParser()
    config_data.read(CONFIG_FILE)
    return config_data


if __name__ == "__main__":
    CONFIG_FILE = get_args()
    get_prices()
