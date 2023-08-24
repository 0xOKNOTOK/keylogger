#!/usr/bin/python3

try:
    import subprocess
    import keyboard

except ModuleNotFoundError:
    packages = ["keyboard","sounddevice","pynput"]
    subprocess.call("pip install " + ' '.join(packages), shell=True)

finally:
    def start_logger():
        print("logger")
    start_logger()
