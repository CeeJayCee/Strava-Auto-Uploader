import os
import datetime as dt
import shutil

from subprocess import call

print("Starting")

call(["touch", "/home/pi/garmin_run"])

print("Getting times")
now=dt.datetime.now()
last_run=dt.datetime.fromtimestamp(os.stat('/home/pi/garmin_last_run').st_mtime)
ago=now-last_run

os.environ["ACCESS_TOKEN"] = ''

print("Finding files")
for root,dirs,files in os.walk('/media/usb/GARMIN/ACTIVITY/'):
        for fname in files:
                path = os.path.join(root,fname)
                st = os.stat(path)
                mtime = dt.datetime.fromtimestamp(st.st_mtime)
                if mtime > last_run:
                        print("Found file: " + fname)
                        call(["python", "/home/pi/stravalib/stravaup.py", "-t", ".fit", "-P", "-E", "True", path])

print("Touching last run")
call(["touch", "/home/pi/garmin_last_run"])
print("Finished")
