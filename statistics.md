# Statistics gathering Pi

Short explain on how i created the statistics Pi

## Creation
* Create from Pi lite O/S
* extend file system
* Auto login to `pi`
* Full upgrade and update

## Set up local installs
* set up speed test as per here: https://pimylifeup.com/raspberry-pi-internet-speed-monitor/
* set up pip as per here: https://pimylifeup.com/raspberry-pi-pip/
* `sudo apt install influxdb-client`
* `sudo pip3 install influxdb`
* from github clone `scp -pr pi/speedtest pi@statspi:/home/pi/speedtest`
* manually add data pi IP to the /etc/hosts
* add to crontab with `*/30 * * * * python3 /home/pi/speedtest/speedtest-influx.py`
