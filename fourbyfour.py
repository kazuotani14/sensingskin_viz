#test code without serial

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

x=[]
y=[]
z=[]
dx=[]
for i in range(0,4):
	x.append(i*0.25)
	y.append(i*0.25)
	z = [0,5,10,20]
	dx = 0.25	

cmap = plt.cm.hot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

for x in range(0,4):
	for y in range(0,4):
		ax.add_artist(Rectangle(xy=(x[x],y[x]),facecolor=cmap(z[x]**2), width=dx, height=dx))

plt.show()
quit()

#############################

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import serial
ser = serial.Serial('/dev/tty.usbserial', 9600)

while true: 
	sensorValue = ser.readline()
	print "%s"  %sensorValue
	
	x=[]
	y=[]
	z=[]
	dx=[]
	for i in range(0,4):
		x.append(i*0.25)
		y = 0
		z = [0,5,10,20]
		dx = 0.25	

	cmap = plt.cm.hot
	fig = plt.figure()
	ax = fig.add_subplot(111, aspect='equal')

	for i in range(0,4):
		ax.add_artist(Rectangle(xy=(x[i],y),facecolor=cmap(z[i]**2), width=dx, height=dx))
	plt.show()

