# Flight Radar

## Set up Pi
* install full latest image
* `sudo apt-get update`
* `sudo apt-get upgrade`

## Install FR software
* `sudo bash -c "$(wget -O - http://repo.feed.flightradar24.com/install_fr24_rpi.sh)"`
* `sudo fr24feed --signup`
* `sudo systemctl start fr24feed`

## To see status
* `fr24feed-status`

## Links
* [https://pimylifeup.com/raspberry-pi-flightradar24/]
* [https://www.flightradar24.com/build-your-own]
