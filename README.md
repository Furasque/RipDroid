# RipDroid

## Description
RipDroid, a Forensic Android Data Extractor (wifi history extraction)

This is a python script, made for threat intelligence purpose, to analyse data from an android phone with ADB enabled.

It can read accounts stored, as well as WiFi SSID

## Research made
//TODO


## Installation

1. Install Android Platform Tools and install to path   
[Link](https://developer.android.com/tools/releases/platform-tools?hl=fr)

2. Clone the git repo
`git clone https://github.com/Furasque/RipDroid.git`

3. Activate Android Debug Bridge, and connect it to your PC
[Link](https://developer.android.com/studio/debug/dev-options#debugging)

4. Run the script  
`python ripdroid.py`



## Usage
`python ripdroid.py -h`
  
  
```
usage: RipDroid [-h] [-a] [-r] [--account] [--wifi]

An android forensic tool

options:
  -h, --help  show this help message and exit
  -a, --all   Print the accounts and WiFi SSID stored on the device
  -r, --raw   Prints the raw informations from the file. If not set, prints the infos in a more readable way.
  --account   Print the accounts stored on the device
  --wifi      Print the stored WiFi SSID on the device, and WiFi Access Point Config
```

> [!IMPORTANT]  
> Only what the creator deemed important infos are printed out when the `--raw` option is not selected.
> Some details are overlooked if not provided (For the accounts : only SSO not from google services are printed).

## License
This project is released under the [Unlicense](https://unlicense.org), placing it in the public domain. You are free to use, modify, and distribute it however you like, as long as you comply with applicable laws. While crediting the original author is appreciated, it is not required.