import os
import argparse


if __name__ == "__main__":
    if(os.system("adb shell \"dumpsys wifi\" > ./data/dumpsys.txt") != 0):
        print("Please connect a phone via USB and make sure it is detected by ADB.")