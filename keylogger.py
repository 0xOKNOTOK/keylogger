#!/usr/bin/python3
try:
    import subprocess
    import keyboard

except ModuleNotFoundError:
    packages = ["keyboard","sounddevice","pynput"]
    subprocess.call("pip install " + ' '.join(packages), shell=True)

finally:
    USER_IP = "" #Same as MAC.
    USER_MAC = "" #Currently string could be int.
    def get_mac_address(interface):#Specific interface required, perhaps scan for multiple if possible.
        try:
            #use some function/module to extract MAC (x-platform)
        except:
            #Error handling...
        return mac_address
