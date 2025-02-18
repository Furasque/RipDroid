import os
import argparse
import re


ACCOUNT_FILE_NAME = "./data/account.txt"
WIFI_FILE_NAME = "./data/wifi.txt"
COLUMN_WIDTH = 40


def print_account_info_from_file(raw : bool) -> None :

    print("--------------Accounts BEGIN--------------")
    with open(ACCOUNT_FILE_NAME, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            match = re.search(r"^\s*Accounts:\s*(\d+)", line)
            
            if match:
                print(line)
                for j in range(1, int(match.group(1))+1):
                    if raw : 
                        print(lines[i+j].strip())
                    else:
                        clean_line = re.sub(r'^Account \{name=|\}$', '', lines[i+j].strip())
                        clean_line = re.sub(r", type=", "\tapp: ", clean_line)
                        login, service = clean_line.split("\t")
                        print(f"{login.ljust(COLUMN_WIDTH)}{service}")
    
    print("---------------Accounts END---------------\n")
    
    
    print("-------------Cached Auth BEGIN-------------")
    with open(ACCOUNT_FILE_NAME, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            match = re.search(r"^\s*RegisteredServicesCache:\s*(\d+)", line)
            
            if match:
                print(line)
                for j in range(1, int(match.group(1))+1):
                    if raw:
                        print(lines[i+j].strip()) 
                    else:
                        clean_line = re.sub(r'^ServiceInfo: AuthenticatorDescription {type=|\}.*$', '', lines[i+j].strip())
                        print(clean_line)
    print("--------------Cached Auth END--------------\n")
    

    
    print("-------------SSO Signin BEGIN-------------")
    with open(ACCOUNT_FILE_NAME, "r") as file:
        lines = file.readlines()
        match = False
        for i, line in enumerate(lines):
            line = line.strip()
            if re.search(r"^\s*Account visibility:", line):
                match = True
            if line == "":
                match = False           
            if match:
                if '@' in line:
                    print("")
                if raw:
                    print(line)
                else:
                    if not re.search(r"^\s*com.google", line) and not re.search(r"^\s*Account visibility:", line) and not "Accounts" in line:
                        print(line.split(',')[0])
                    
    print("--------------SSO Signin END--------------\n")
    return


def print_wifi_info_from_file(raw : bool) -> None :
    print("--------------Stored Wifi BEGIN--------------")
    with open(WIFI_FILE_NAME, "r") as file:
        lines = file.readlines()
        match = False

        for i, line in enumerate(lines):
            line = line.strip()
            
            if "Configured networks End" in line:
                match = False
            if match:
                if raw:
                    print(line)  
                else:
                    clean_line = ""
                    print(clean_line)
            if "Configured networks Begin" in line:
                match = True

    print("---------------Stored Wifi END---------------")

    print("--------------Wifi Hotspot settings BEGIN--------------")
    with open(WIFI_FILE_NAME, "r") as file:
        lines = file.readlines()
        match = False

        for i, line in enumerate(lines):
            line = line.strip()

            if line == "":
                match = False

            if match:
                if raw:
                    print(line)
                else:
                    clean_line = ""
                    print(clean_line)
            
            if "WifiApConfigStore config" in line:
                match = True
            
    print("---------------Wifi Hotspot settings END---------------")




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

        
    
    if all or args.wifi:
        if(os.system(f"adb shell \"dumpsys wifi\" > {WIFI_FILE_NAME}") != 0):
            print("Please connect a phone via USB and make sure it is detected by ADB.")
            exit(1)
        print_wifi_info_from_file(args.raw)