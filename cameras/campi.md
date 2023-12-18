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

```
    - camera_streams:
        - url: "rtsp://172.10.0.100:7447/Rm8pDxEh0W0bG3qZ"
        - url: "rtsp://172.10.0.100:7447/TZCFSXMxZwOzepzt"
        - url: "rtsp://172.10.0.100:7447/HTyBwszxgDTZhzjn"
        - url: "rtsp://172.10.0.100:7447/4EmOx05plChk5Rta"
      duration: 30
      nr_of_columns: 2
```



