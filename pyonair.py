import tinytuya
import time
import subprocess
import sys

# Connect to Device
d = tinytuya.OutletDevice(
    dev_id='<your device id>',
    address='<your device IP address>',      # Or set to 'Auto' to auto-discover IP address
    local_key='<your device local key>', 
    version=3.1)

def offair():
    print('turning off')
    d.turn_off()

def onair():
    print('turning on')
    d.turn_on()

command = [
    "/usr/bin/log",
    "stream",
    "--predicate",
    "sender contains \"ControlCenter\" and composedMessage contains \"Frame publisher cameras changed to\"",
]
process = subprocess.Popen(command, stdout=subprocess.PIPE)
# replace "" with b"" for Python 3
firstTime = True
for line in iter(process.stdout.readline, ""):
    if not line:
        break
    if firstTime:
        # first time through we get one false line which makes us erroneously turn the light on
        firstTime = False
    else:
        print("I got this from the log:", line)
        if b"[:]" in line:
            offair()
        elif b"\", \"unknown\"]]" in line:
            onair()
