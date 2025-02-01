import os
import argparse
import re


ACCOUNT_FILE_NAME = "./data/account.txt"
WIFI_FILE_NAME = "./data/wifi.txt"


def print_raw_account_info_from_file() -> None:
    print("--------------Accounts BEGIN--------------")
    with open(ACCOUNT_FILE_NAME, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            match = re.search("^\s*Accounts:\s*(\d+)", line)
            
            if match:
                print(line)
                for j in range(1, int(match.group(1))+1) :
                    print(lines[i+j].strip()) 
    
    print("---------------Accounts END---------------\n")
    
    
    print("-------------Cached Auth BEGIN-------------")
    with open(ACCOUNT_FILE_NAME, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            match = re.search("^\s*RegisteredServicesCache:\s*(\d+)", line)
            
            if match:
                print(line)
                for j in range(1, int(match.group(1))+1) :
                    print(lines[i+j].strip()) 
    print("--------------Cached Auth END--------------\n")
    
    
    print("-------------SSO Signin BEGIN-------------")
    with open(ACCOUNT_FILE_NAME, "r") as file:
        lines = file.readlines()
        match = False
        for i, line in enumerate(lines):
            line = line.strip()
            if re.search("^\s*Account visibility:", line):
                match = True            
            if match:
                print(line)
    print("--------------SSO Signin END--------------\n")

    
    return

def print_account_info_from_file(raw : bool) -> None :
    if raw:
        print_raw_account_info_from_file()
        return
    

    return






if __name__ == "__main__":

    # Parser Logic
    parser = argparse.ArgumentParser(
        prog="RipDroid",
        description="An android forensic tool"
    )
    parser.add_argument('-a', '--all', action='store_true', help="Print the accounts and WiFi SSID stored on the device")
    parser.add_argument('-r', '--raw', action='store_true', help="Prints the raw informations from the file. If not set, prints the infos in a more readable way.")
    parser.add_argument('--account', action='store_true', help="Print the accounts stored on the device")
    parser.add_argument('--wifi', action='store_true', help="Print the stored WiFi SSID on the device, and WiFi Access Point Config")
    args = parser.parse_args()


    # Treating args
    if not any(vars(args).values()):
        print("No arguments provided.")
        exit(1)
    
    all = False
    if args.all:
        all = True

    if all or args.account:
        if(os.system(f"adb shell \"dumpsys account\" > {ACCOUNT_FILE_NAME}") != 0):
            print("Please connect a phone via USB and make sure it is detected by ADB.")
            exit(1)
        print_account_info_from_file(args.raw)

        
    
    if all or argparse.Namespace(wifi=True):
        if(os.system(f"adb shell \"dumpsys wifi\" > {WIFI_FILE_NAME}") != 0):
            print("Please connect a phone via USB and make sure it is detected by ADB.")
            exit(1)
        

    