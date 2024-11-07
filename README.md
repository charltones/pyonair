# pyonair
Python powered 'on air' light that comes on during videoconferencing on Mac

I wanted to create a signal for home so my family knows when I'm speaking on Chime / Zoom / Teams because they don't like coming into the room when my camera is on. I've managed to create something and automate it - I thought I would share the details here. This solution is highly specific to a Mac - you'd need a different approach for a PC.

I have a python script (pyonair.py) which runs all the time monitoring for the camera status. If a camera on event is detected it controls a smart plug which powers a USB 'on air' light. The smart plug is controlled by the tuya cloud - there's a python library for this with instructions to set it up here: https://github.com/jasonacox/tinytuya. From the tuya cloud web site you will get a device id, local key and IP address for your smartplug.

I copied the code to /usr/local/bin/pyonair.py. You will also need to copy the plist file to /Library/LaunchDaemons/ to make sure the python script starts on boot and keeps running. Mke sure to edit the plist to ensure the paths match up with where you have put the python code etc.

You can type this to start the script:

sudo launchctl load /Library/LaunchDaemons/com.charltones.onair.plist




