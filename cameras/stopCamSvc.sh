#!/bin/sh

echo "stopping camera service"
sleep 5
systemctl stop lightdm.service

echo "stopping screen to save the screen"
sleep 5
xset dpms force off
