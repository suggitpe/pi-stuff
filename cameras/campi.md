# Cameras Pi (no OmxPlayer)

----

## Initial
* Install raspian bullseye
* Open raspi-config
  * System Options -> Auto login to pi
  * GPU memory -> 256
  * Enable SSH
  * Advanced -> expand filesystem
* System update and upgrade
* `sudo apt-get update && sudo apt-get update`
* `sudo apt-get install -y git vim wget`
* `sudo apt-get install -y libcamera-apps-lite libfreetype6 libcamera0`

----
## Install
* from https://github.com/bluenviron/mediamtx/releases
* `wget https://github.com/bluenviron/mediamtx/releases/download/v1.4.0/mediamtx_v1.4.0_linux_armv7.tar.gz`
* `tar -xzvf mediamtx_v1.2.1_linux_armv7.tar.gz`
