import argparse
import configparser
import random
import os
import time

import requests
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient

USER_AGENT_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.102 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15']

ARGS = None
CFG = None
LOCAL_STORE = '~/amazon-prices.csv'


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-c", "--config", help="pass in a config file")
    arg_parser.add_argument("-i", "--influx", action="store_true", help="persist results to influxdb")
    arg_parser.add_argument("-v", "--csv", action="store_true", help="persist results to local csv")
    arg_parser.add_argument("-d", "--debug", action="store_true", help="add debug details (eg headers)")
    args = arg_parser.parse_args()
    if args.config is None:
        raise Exception("Need a config file please")
    return args


def get_prices():
    session = requests.Session()
    with open('urls.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    for url_cfg in lines:
        cfg=url_cfg.split("|")
        store_price(session, cfg[0], cfg[1])


def store_price(session, friendly_name, url):
    show_headers(session)
    page = session.get(url, headers=build_headers())
    if check_for_captcha(page.text):
        print("Found captcha for ", url)
        return
    data = create_data_from_page(friendly_name, page)
    persist_data(data)
    print(data)


def build_headers():
    user_agent = random.choice(USER_AGENT_LIST)
    if ARGS.debug:
        print("Using agent:", user_agent)
    return {'User-Agent': user_agent,
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
    'referer': 'https://prerender.io/'}


def persist_data(data):
    if ARGS.influx:
        print("Writing data to influxdb")
        db_client = create_db_client()
        db_client.write_points(data)
    if ARGS.csv:
        print("Wring data to CSV file")
        f = open(LOCAL_STORE, 'a+')
        if os.stat(LOCAL_STORE).st_size == 0:
            f.write('Date,Time,Ping (ms),Jitter (ms),Download (Mbps),Upload (Mbps)\r\n')


def check_for_captcha(page_text):
    return page_text.find('Type the characters you see in this image') > 1


def create_data_from_page(friendly_name, page):
    soup = BeautifulSoup(page.content, 'html.parser')
    page_title = soup.find(id='productTitle').get_text().strip()
    price = soup.find('span', class_='a-offscreen').get_text().replace('£', '')
    return create_data(friendly_name, page_title, price)


def create_data(friendly_name, page_title, price):
    return [
        {
            "measurement": "amazon_price",
            "tags": {
                "host": "statspi"
            },
            "fields": {
                "datetime":time.strftime('%d-%m-%Y %H:%M'),
                "friendly_name": friendly_name,
                "name": page_title[:50],
                "price": float(price)
            }
        }
    ]


def show_headers(session):
    if ARGS.debug:
        print(session.get('http://httpbin.org/headers', headers=build_headers()).text)


def create_db_client():
    return InfluxDBClient(host=CFG.get('influxdb', 'host'),
                          port=CFG.get('influxdb', 'port'),
                          username=CFG.get('influxdb', 'user'),
                          password=CFG.get('influxdb', 'pass'),
                          database='amazonprices')


def read_configuration():
    if ARGS.debug:
        print("Reading config from", ARGS.config)
    config_data = configparser.ConfigParser()
    config_data.read(ARGS.config)
    return config_data


if __name__ == "__main__":
    ARGS = get_args()
    CFG = read_configuration()
    get_prices()