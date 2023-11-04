# Speedtest

## Install 
* `scp -pr speedtest/*.py pi@statspi:/home/pi/speedtest`

## Pip installs needed
`pip3 install bs4`
`pip3 install requests`
`pip3 install configparser`

## Set up db
* from datapi, run `influx`
* CREATE DATABASE internetspeed

## check it
* `influx`
* `use internetspeed`
* `select * from internet_speed`