#!/bin/sh

echo "stopping camera service"
sleep 5
systemctl stop lightdm.service

echo "starting camera service"
sleep 5
systemctl start lightdm.service

