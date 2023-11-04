# Setting up a pi for monitoring the network

## Intial setup
* From NEMS main site download the image and burn it
* Dont set the WIFI credentials as this is due to be physical connection to the network

## To set up the agents on all the services you want monitored
* add monitorpi ip to the /etc/hosts 
* `sudo apt install nagios-nrpe-server monitoring-plugins -y`
* edit `/etc/nagios/nrpe.cfg` and add "monitorpi" to the allowed_hosts plus enbale logging
* `sudo systemctl restart nagios-nrpe-server`

## Notifications
* https://docs.nemslinux.com/en/latest/notifications/telegram.html
* https://docs.nemslinux.com/en/latest/gettingstarted/smtp.html
