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
* `sudo apt-get install -y git vim wget`
* Set tmp to tmpfs in fstab
*  tmpfs /var/tmp tmpfs defaults,nodiratime,noatime 0 0
*  tmpfs /tmp tmpfs defaults,nodiratime,noatime 0 0
* Change /boot/confit.txt
*  Force set the screen resolution 1920 / 1080
*  Change `dtoverlay=vc4-kms-v3d` to `dtoverlay=vc4-fkms-v3d` ... add the 'f'
* Sort .bashrc so the basics work

----
## Install RpiSurv
* Clone `git clone https://github.com/SvenVD/rpisurv` --> dont do the install yet
* [More details here](https://github.com/SvenVD/rpisurv)
* You may need to tamper with the installer to push on through with the install even with VLC issues
* Once install is done you will need to edit `/etc/rpisurv/display1.yml` or `/etc/rpisurv/display2.yml` (depending which HDMI port you use) to get rid of the bunny cartoons and install the cameras below
* reminder shift + insert to paste into vi
```
essentials:
  screens:
    - streams:
        - url: "rtsp://172.10.0.100:7447/ph6fdduPyeARIwq0"
          force_coordinates: [640, 0, 1920, 720]
        - url: "rtsp://172.10.0.100:7447/HTyBwszxgDTZhzjn"
          force_coordinates: [0, 0, 640, 360]
        - url: "rtsp://172.10.0.100:7447/4EmOx05plChk5Rta"
          force_coordinates: [0, 360, 640, 720]
        - url: "rtsp://172.10.0.100:7447/TZCFSXMxZwOzepzt"
          force_coordinates: [0, 720, 640, 1080]
        - url: "rtsp://172.10.0.100:7447/kbJpCDwgAnCk6MXg"
          force_coordinates: [640, 720, 1280, 1080]
        - url: "rtsp://172.10.0.100:7447/WlMcXZlOlMKhCREJ"
          force_coordinates: [1280, 720, 1920, 1080]
      duration: 20
    - streams:
        - url: "rtsp://172.10.0.100:7447/ph6fdduPyeARIwq0"
        - url: "rtsp://172.10.0.100:7447/kbJpCDwgAnCk6MXg"
        - url: "rtsp://172.10.0.100:7447/HTyBwszxgDTZhzjn"
        - url: "rtsp://172.10.0.100:7447/WlMcXZlOlMKhCREJ"
      duration: 20
      nr_of_columns: 2
```
----
## Opensurv
* https://github.com/opensurv/opensurv <-- use this one ... but not just yet ... its coming soon
* https://github.com/OpenSurv/OpenSurv/discussions/21 <-- details on how to get it working
* `sudo apt install python3-yaml`
* `sudo vim /etc/opensurv/monitor1.yml`
* `sudo systemctl restart lightdm.service`



