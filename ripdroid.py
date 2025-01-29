import os
import argparse


if __name__ == "__main__":

    # Parser Logic
    parser = argparse.ArgumentParser(
        prog="RipDroid",
        description="An android forensic tool"
    )
    parser.add_argument('-a', '--all', action='store_true', help="Print the accounts, connectivity logs and WiFi SSID stored on the device")
    parser.add_argument('--account', action='store_true', help="Print the accounts stored on the device")
    parser.add_argument('--connectivity', action='store_true', help="Print the connectivity log (Wifi/Cellular) the device")
    parser.add_argument('--wifi', action='store_true', help="Print the stored WiFi SSID on the device")
    args = parser.parse_args()


    # Treating args
    if not any(vars(args).values()):
        print("No arguments provided.")
        exit(1)
    
    all = False
    if args.all:
        all = True

    if all or args.account:
        if(os.system("adb shell \"dumpsys account\" > ./data/account.txt") != 0):
            print("Please connect a phone via USB and make sure it is detected by ADB.")
    
    if all or args.connectivity:
        if(os.system("adb shell \"dumpsys connectivity\" > ./data/connectivity.txt") != 0):
            print("Please connect a phone via USB and make sure it is detected by ADB.")
    
    if all or argparse.Namespace(wifi=True):
        if(os.system("adb shell \"dumpsys wifi\" > ./data/wifi.txt") != 0):
            print("Please connect a phone via USB and make sure it is detected by ADB.")
    
    