import re
import subprocess
import configparser
from influxdb import InfluxDBClient
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-c", "--config", help="pass in a config file")
args = argParser.parse_args()

if args.config is None:
    raise Exception("Need a config file please")

cfg = configparser.ConfigParser()
cfg.read(args.config)

response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('Latency:.*?jitter:\s+(.*?)ms', response, re.MULTILINE)

ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)

speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": "statspi"
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping),
            "jitter": float(jitter)
        }
    }
]

client = InfluxDBClient(host=cfg.get('influxdb', 'host'),
                        port=cfg.get('influxdb', 'port'),
                        username=cfg.get('influxdb', 'user'),
                        password=cfg.get('influxdb', 'pass'),
                        database='internetspeed')
client.write_points(speed_data)