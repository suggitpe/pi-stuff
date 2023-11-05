# Statistics gathering Pi

Short explain on how i created the statistics Pi

## Creation
* Create from Pi full O/S
* extend file system
* Auto login to `pi`
* enable vnc
* GPU memory to 256
* Full upgrade and update
* update .bashrc

## Set up local installs
* set up speed test as per here: https://pimylifeup.com/raspberry-pi-internet-speed-monitor/
    * `sudo apt install apt-transport-https gnupg1 dirmngr lsb-release`
    * `curl -L https://packagecloud.io/ookla/speedtest-cli/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/speedtestcli-archive-keyring.gpg >/dev/null`
    * `echo "deb [signed-by=/usr/share/keyrings/speedtestcli-archive-keyring.gpg] https://packagecloud.io/ookla/speedtest-cli/debian/ $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/speedtest.list`
    * `sudo apt update`
    * `sudo apt install speedtest`
    * `speedtest` --> accept the asks
* set up pip as per here: https://pimylifeup.com/raspberry-pi-pip/
    * `sudo apt install python3-pip`
* `sudo apt install influxdb-client`
* `sudo pip3 install influxdb`
* from github clone `scp -pr pi/speedtest pi@statspi:/home/pi/speedtest`
* manually add data pi IP to the /etc/hosts
* add to crontab with `*/30 * * * * python3 /home/pi/speedtest/speedtest-influx.py`
