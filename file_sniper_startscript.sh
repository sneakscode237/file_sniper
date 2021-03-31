#!/bin/bash
echo "File_sniper is written in python3 and requires the additional 'magic' module"
while true; do
    read -p "Do you want to install the addtional module with pip? " yn
    case $yn in
        [Yy]* ) sudo apt-get install libmagic1 && pip3 install python-magic; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
read -p "Press enter to execute the script"
python3 file_sniper.py
while true; do
    read -p "Do you want to run this script at startup? Please save all files in your Documents Folder so that the crontab job works properly! " yn
    case $yn in
        [Yy]* ) crontab -l > crontab.txt && echo "@reboot python3 /home/julian/Documents/file_sniper/file_sniper.py" >> crontab.txt && crontab crontab.txt && rm crontab.txt; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
