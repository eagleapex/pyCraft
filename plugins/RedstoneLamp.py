import string
import copy
import base64
import re
from datetime import datetime
import RPi.GPIO as GPIO

class RedstoneLamp:

    def onEnable(self, parser, pluginloader):
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, False)


    def packetReceive(self, packetID, receivedPacket):
        packet = copy.deepcopy(receivedPacket)
        if packetID == "\x03":
                packet['Message'] = filter(lambda x: x in string.printable, packet['Message'])
		
		if re.search(r'on', packet['Message']):
			print "REDSTONE LAMP ON MOFO\n";
			GPIO.output(16, True)
			with open("redstone.log", "a") as myfile:
				myfile.write(str(datetime.now()) + " - Redstone on\n")

		if re.search(r'off', packet['Message']):
			print "REDSTONE LAMP OFF MOFO\n";
			GPIO.output(16, False)
			with open("redstone.log", "a") as myfile:
				myfile.write(str(datetime.now()) + " - Redstone off\n")
