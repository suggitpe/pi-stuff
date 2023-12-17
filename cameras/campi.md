# Cameras Pi (no OmxPlayer)

----

## Initial
* Install raspian bullseye
* Open raspi-config
  * System Options -> Auto login to pi
  * Remove splash-screen
  * GPU memory -> 512
  * Enable SSH
  * Advanced -> expand filesystem
* System update and upgrade
* `sudo apt-get update && sudo apt-get update`
* `sudo apt-get install -y git vim wget`

----
##Install RpiSurv
* Remove VLC
* Increase GPU memory to 512
* Set tmp to tmpfs in fstab
* Force set the screen resolution in /boot/config.txt to 1920 / 1080
* Clone `git clone https://github.com/SvenVD/rpisurv` --> dont do the install yet
* ``

----
## Install
* from https://github.com/bluenviron/mediamtx/releases
* `wget https://github.com/bluenviron/mediamtx/releases/download/v1.4.0/mediamtx_v1.4.0_linux_armv7.tar.gz`
* `tar -xzvf mediamtx_v1.2.1_linux_armv7.tar.gz`
