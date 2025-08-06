#!/bin/sh

echo "stopping rpisurv"
sleep 5
systemctl stop rpisurv

echo "stopping screen to save the screen"
sleep 5
xset dpms force off
