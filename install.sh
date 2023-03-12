#!/bin/bash

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "	STARTING DATA STREAMER ECHO INSTALLATION"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

header() {
    printf "\n"
    echo "##################################################"
    echo "###     ${1}"
    echo "##################################################"
    printf "\n"
}


header "copying datastreamer folder to /opt"
sudo cp -r ./datastreamer/ /opt

header "moving datastreamer-echo.service to systemd"
sudo mv /opt/datastreamer/datastreamer-echo.service /etc/systemd/system

header "enabling datastreamer-echo.service"
sudo chmod 664 /etc/systemd/system/datastreamer-echo.service
sudo systemctl enable datastreamer-echo.service

header "starting datastreamer-echo.service"
sudo systemctl enable datastreamer-echo.service

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "	COMPLETED DATA STREAMER ECHO INSTALLATION"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

echo "Press any key to exit."
read waitforkey
