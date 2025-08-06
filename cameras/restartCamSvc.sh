#!/bin/sh

echo "stopping rpisurv"
sleep 5
systemctl stop rpisurv

echo "starting rpisurv"
sleep 5
systemctl start rpisurv

