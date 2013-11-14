# Redstone Lamp project developed by Chris Thompson
# Redstone Lamp plugin by Kyle Yankanich
# 
# This plugin listens for a specific /tell message containing the word "on" or "off"
# This could be any string
# "On" will turn the pin high
# "Off" will turn the pin low
# For the Redstone Lamp replica, pin 16 is connected to the base on a NPN transistor to control 12V LEDs
# CC-BY-SA 2013

import string
import copy
import base64
import re
from datetime import datetime
import RPi.GPIO as GPIO

pin = 16 #the GPIO on the RPi.

class RedstoneLamp:

    def onEnable(self, parser, pluginloader):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)


    def packetReceive(self, packetID, receivedPacket):
        packet = copy.deepcopy(receivedPacket)
        if packetID == "\x03":
                packet['Message'] = filter(lambda x: x in string.printable, packet['Message'])
		
		if re.search(r'on', packet['Message']):
			print "REDSTONE LAMP ON MOFO\n";
			GPIO.output(pin, True)
			with open("redstone.log", "a") as myfile:
				myfile.write(str(datetime.now()) + " - Redstone on\n")

		if re.search(r'off', packet['Message']):
			print "REDSTONE LAMP OFF MOFO\n";
			GPIO.output(pin, False)
			with open("redstone.log", "a") as myfile:
				myfile.write(str(datetime.now()) + " - Redstone off\n")
