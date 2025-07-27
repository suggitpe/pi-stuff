# Notes on creating a raspberry pi in kiosk mode for a scroll of real time streams from the cameras

This is a Pi Model B v2.0
* [https://www.pololu.com/product/2750]
* [https://www.raspberrypi.com/products/raspberry-pi-2-model-b/]

## Burn SD card
* download and install the Pi Imager app
* set up to use PI OS Lite (need to use "buster" version)
* In advanced: 1) enable SSH with hostname (kioskpi) 2) username and password (pi) 3) wireless LAN setting
* SSH in (use ssh pi@kioskpi.local) then username and pass as above
* Once in run a full upgrade (`update` and `full-update`)

Note: check the hostname is correct after the image ... `hostname`.  You might need to update /etc/hostname and /etc/hosts

## Set up the autologin to the pi user
* Run `sudo raspi-config`
* Scroll through options:
  * Boot to CLI as pi (1 - System options), (S5 - Boot), (B2 - CLI)
  * Network at boot: (1 - System Options), (S6 - Net at Boot), Yes
  * Remove splash: (1 - System options), (S7 - splash), No
  * Overclock it: (4 - Performance), (P1 - Overclock), OK, High
  * Expand to full file system: (6 - Advancced), (A1 - Expand)
  * GPU (4 - Performance), (P2 - GPU memory), 256
* Finish and `Yes` to the reboot
* This should restart with a CLI logged in as "pi"

## Setup the wifi dongle

### Build and Install

Need to build the wifi driver first. Dongle is a rtl8188fu (Obda:f179).

1. sudo apt-get install -y raspberrypi-kernel-headers
2. sudo apt-get install -y build-essential git dkms raspberrypi-kernel-headers
3. sudo ln -s /lib/modules/$(uname -r)/build/arch/arm /lib/modules/$(uname -r)/build/arch/armv7l
4. git clone -b arm https://github.com/kelebek333/rtl8188fu rtl8188fu-arm
5. sudo dkms add ./rtl8188fu-arm
6. sudo dkms build rtl8188fu/1.0
7. sudo dkms install rtl8188fu/1.0
8. sudo cp ./rtl8188fu-arm/firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/

### Configuration
* disable power managment and plugging replugging issues
* `sudo mkdir -p /etc/modprobe.d/`
* `sudo touch /etc/modprobe.d/rtl8188fu.conf`
* `echo "options rtl8188fu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8188fu.conf`
* Disable MAC Address Spoofing
* `sudo mkdir -p /etc/NetworkManager/conf.d/`
* `sudo touch /etc/NetworkManager/conf.d/disable-random-mac.conf`
* Blacklist for kernel 5.15 and newer (No needed for kernel 5.17 and up)
* If you are using kernel 5.15 and newer, you must create a configuration file with following commands for preventing to conflict rtl8188fu module with built-in r8188eu module.
* `echo 'alias usb:v0BDApF179d*dc*dsc*dp*icFFiscFFipFFin* rtl8188fu' | sudo tee /etc/modprobe.d/r8188eu-blacklist.conf`

### Notes
* [https://github.com/corneal64/Realtek-USB-Wireless-Adapter-Drivers]
* [https://github.com/kelebek333/rtl8188fu/tree/arm#how-to-install-for-arm-devices]
* [https://forums.raspberrypi.com/viewtopic.php?t=334503]

## Install the displaycamera software
* `wget https://github.com/Anonymousdog/displaycameras/archive/0.8.3.3.zip`
* `unzip 0.8.3.3.zip`
* `cd displaycameras-0.8.3.3`
* `sudo chmod +x install.sh`
* `sudo ./install.sh`
* locate the layout files in the /etc/displaycameras/displaycameras.conf
* add in the RTSP feeds plus trim down to the relevant screens only
* sudo systemctl restart displaycameras.service
* restart to see changes take effect

## RTSP feeds
* Gate: rtsp://172.10.0.100:7447/ph6fdduPyeARIwq0
* Drive-1: rtsp://172.10.0.100:7447/TZCFSXMxZwOzepzt
* Drive-2: rtsp://172.10.0.100:7447/????
* LongGarden-1: rtsp://172.10.0.100:7447/HTyBwszxgDTZhzjn
* LongGarden-2: rtsp://172.10.0.100:7447/4EmOx05plChk5Rta
* BackGarden: rtsp://172.10.0.100:7447/WlMcXZlOlMKhCREJ

## Links
* [https://www.raspberrypi.com/tutorials/how-to-use-a-raspberry-pi-in-kiosk-mode/]
* [https://reelyactive.github.io/diy/pi-kiosk/]
* [https://www.youtube.com/watch?v=0tvX_gsv2ZU]
* [https://selfhostedhome.com/raspberry-pi-video-surveillance-monitor/]

## Notes:
* `sudo systemctl restart displaycameras.service`
* `sudo systemctl status displaycameras.service`
