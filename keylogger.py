#!/usr/bin/python3
try: #Try to load modules, if not found install on users machine?
    import keyboard
    import subprocess
    import sys
except:
    def install(packages):
        subprocess.check_call([sys.executable, "-m", "pip", "install", packages])
finally:
    def start_logger():
        return 0
    start_logger()
