import serial
import time
ser = serial.Serial('/dev/cu.usbserial-AM01VC7B', 9600)
z = [0,0,0,0]

while True:
	print ser.readline()
	
quit()
#	sensorValues = sensorValues.split()
#	for i in range(0,2):
#		sensorValues[i] = float(sensorValues[i])
#	for i in range(0,2):
#		for j in range(0,2):
#			pin = 2*i+j
#			z[pin] = (sensorValues[pin]/1023)*20
#			print z[pin]