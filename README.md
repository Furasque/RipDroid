# RipDroid
RipDroid, a Forensic Android Data Extractor (wifi history extraction)

This is a python script, made for threat intelligence purpose, to analyse data from an android phone with ADB enabled.

It can read accounts stored, as well as WiFi SSID and connectivity logs



## How to run

1. Install Android Platform Tools and install to path   
[Link](https://developer.android.com/tools/releases/platform-tools?hl=fr)

2. Connect the android phone to your PC using a USB cable (and make sure Android Debug Bridge is activated)

3. Run the script  
`python ripdroid.py`



## Options
`python ripdroid.py -h`
  
  
```
usage: RipDroid [-h] [-a] [--account] [--connectivity] [--wifi]

An android forensic tool

options:
  -h, --help      show this help message and exit
  -a, --all       Print the accounts, connectivity logs and WiFi SSID stored on the device
  --account       Print the accounts stored on the device
  --connectivity  Print the connectivity log (Wifi/Cellular) the device
  --wifi          Print the stored WiFi SSID on the device
```