# Amazon Tracker

## Install
* `scp -pr amazontracker/*.py pi@statspi:/home/pi/amazontracker`
* `scp -pr amazontracker/trackurls.txt pi@statspi:/home/pi/amazontracker`
* `scp -pr amazontracker/config.txt pi@statspi:/home/pi/amazontracker`

## Pip installs needed
`sudo apt install influxdb-client`
`pip3 install bs4`
`pip3 install requests`
`pip3 install configparser`
`pip3 install influxdb`

## Set up db
* from datapi, run `influx`
* CREATE DATABASE amazonprices

## Check it
* `influx`
* `use amazonprices`
* `select * from amazon_price`