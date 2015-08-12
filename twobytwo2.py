from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import serial
ser = serial.Serial('/dev/cu.usbserial-AM01VC7B', 9600)

x=[]
y=[]
z=[]
dx=0.5

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
		deltaV[i] = float(pinValues[])-0;
	deltaV[2] = deltaV[2]*1.25
	deltaV[3] = deltaV[3]*1.25
	print "deltaV= %s" %deltaV	
			
	for i in range(0,2):
		for j in range(0,2):
			if (deltaV[i]-40)>0 and (deltaV[j+2]-40)>0:
				z[2*i+j] = 10;
			ax.add_artist(Rectangle(xy=(x[i],y[j]),facecolor=cmap(z[2*i+j]**2), width=dx, height=dx))
	print "color= %s" %z
	plt.draw()		


	# update colormap values according to sensorValues
#	for i in range(0,2):
#		for j in range(0,2):
#			z[i,j] = (deltaV[i,j]/1023)*15
#			z[i,j] = 20 - int(z[i,j])
#			# print z[i,j]
#	plt.draw()