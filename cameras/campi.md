# Cameras Pi (no OmxPlayer)

----

## Initial
* Install raspian buster
* Open raspi-config
  * System Options -> Auto login to pi
  * Remove splash-screen
  * GPU memory -> 512
  * Enable SSH
  * Advanced -> expand filesystem
* DO NOT DO THE System update and upgrade
* `sudo apt-get install -y git vim wget`

----
## Install RpiSurv
* Set tmp to tmpfs in fstab
* Force set the screen resolution in /boot/config.txt to 1920 / 1080
* Clone `git clone https://github.com/SvenVD/rpisurv` --> dont do the install yet
* [More details here|https://github.com/SvenVD/rpisurv]


----
## Install
* from https://github.com/bluenviron/mediamtx/releases
* `wget https://github.com/bluenviron/mediamtx/releases/download/v1.4.0/mediamtx_v1.4.0_linux_armv7.tar.gz`
* `tar -xzvf mediamtx_v1.2.1_linux_armv7.tar.gz`

----
## Instal older version of VLC
* `sudo apt remove vlc -y && sudo apt autoremove -y`
* `scp -pr vlc-3.0.17.4.tar.xz pi@campi1:/home/pi`
* `sudo apt-get install libavformat-dev libavcodec-dev libavutil-dev libswscale-dev libavdevice-dev xcb`
* `./configure --disable-lua --disable-avcodec --disable-a52`
