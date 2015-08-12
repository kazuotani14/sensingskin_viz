from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import serial
import sys
from select import select

ser = serial.Serial('/dev/cu.usbserial-AM01VC7B', 9600)

x=[]
y=[]
z=[]
dx=0.3

#one layer: A0, A1
#other layer: A2,A3

# 0,1 1,1
# 0,0 1,0

#define x,y,dx to draw squares. z is color, to be updated
for i in range(0,2):
	x.append(i*dx)
	y.append(i*dx)
	z = [0,0,0,0] #0 is black, 5 and 10 are red, 20 is white

cmap = plt.cm.hot
fig = plt.figure()
plt.ion()
plt.show()
ax = fig.add_subplot(111, aspect='equal')

initVals = ser.readline()
initVals = initVals.split()
deltaV = [0,0,0,0]

while True: 
	deltaV = [0,0,0,0]
	z = [0,0,0,0]
	# read sensorValues as string, then convert to matrix
	pinValues = ser.readline()
	# print "%s"  %pinValues
	pinValues = pinValues.split()
	
	for i in range(0,4):
		deltaV[i] = int(float(initVals[i]) - float(pinValues[i]))
	#compensate for bottom layer getting less strain
	#currently compensated with 20ko voltage divider vs 68ko voltage divider on top
	#deltaV[2] = int(deltaV[2]*1.5)
	#deltaV[3] = int(deltaV[3]*1.5)
	print "deltaV= %s" %deltaV	
			
	for i in range(0,2):
		for j in range(0,2):
			if (deltaV[i]-50)>0 and (deltaV[j+2]-50)>0:
				z[2*i+j] = 20
			elif (deltaV[i]-30)>0 and (deltaV[j+2]-30)>0:
				z[2*i+j] = 15
			elif (deltaV[i]-15)>0 and (deltaV[j+2]-15)>0:
				z[2*i+j] = 10	
			elif (deltaV[i]-5)>0 and (deltaV[j+2]-5)>0:
				z[2*i+j] = 5
			if deltaV[0]>100:
				sx = 0.25	
			else: 
				sx = 0	
			if deltaV[2]>100:
				sy = 0.25
			else: 
				sy = 0		
			ax.add_artist(Rectangle(xy=(x[i]+s,y[j]+sy),facecolor=cmap(z[2*i+j]**2), width=dx, height=dx))
	print "color values= %s" %z
	plt.draw()		
	
	
	
	#reset initial values if too much drift, by grounding A4. eventually include switch
	if int(pinValues[4]) == 0:
		initVals = pinValues
	
	
	# update colormap values according to sensorValues
#	for i in range(0,2):
#		for j in range(0,2):
#			z[i,j] = (deltaV[i,j]/1023)*15
#			z[i,j] = 20 - int(z[i,j])
#			# print z[i,j]
#	plt.draw()