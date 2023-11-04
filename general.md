# General Pi set up

## Burn SD card
* download and install the Pi Imager app
* set up to use PI OS Lite
* In advanced: 1) enable SSH with hostname (<purpose>pi) 2) username and password (pi) 3) wireless LAN setting
* SSH in (use ssh pi@<purpose>pi.local) then username and pass as above
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
