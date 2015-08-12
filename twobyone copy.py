# Conductive carbon grease strain and pressure sensor, 1x2 grid, simple 

#import modules, set serial port and baud rate
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import serial
ser = serial.Serial('/dev/cu.usbserial-AM01VC7B', 9600)

#initialize variables for drawing squares
x=[]
y=[]
z=[]
dx=0.5
sensorValues = np.array([0,5.5],float) #initialize 1x2 array

#define x,y,dx to draw squares. z is initial colors updated
for i in range(0,2):
	x.append(i*dx)
	y.append(i*dx)
	z = sensorValues #0 is black, 5 and 10 are red, 20 is white

cmap = plt.cm.hot
fig = plt.figure()
plt.ion()
plt.show()
ax = fig.add_subplot(111, aspect='equal')

#read initial sensor values at rest, to compare later
initVals = ser.readline()
initVals = initVals.split()
deltaV = [0,0]

#code below loops
while True: 
	# read sensorValues as string, then convert to list
	pinValues = ser.readline()
	pinValues = pinValues.split()
	
	for i in range(0,2):
		deltaV[i] = float(initVals[i])-float(pinValues[i])
		print "%s" %deltaV
	# update colormap values according to sensorValues
	for i in range(0,2):
		for j in range(0,2):
			z[i] = (deltaV[i]/1023)*20
			#z[i] = 20 - int(z[i])
			ax.add_artist(Rectangle(xy=(x[i],y[j]),facecolor=cmap(z[i]**2), width=dx, height=dx))
	plt.draw()