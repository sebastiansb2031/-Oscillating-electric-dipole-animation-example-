
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
r,theta = meshgrid( linspace(0.1,10,200), linspace(0,2*pi,360))
x=r*cos(theta);
y=r*sin(theta);

N=10
X=10
font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

def update(t):
	plt.cla()	
	plt.title(' Simulacion del Campo Electrico Radiado por un Dipolo Electrico Oscilante ', fontdict=font)
	z = power((sin(theta+pi/2)),2)*cos(0.1*t-r+arctan(r))
	wframe=plt.contour(x,y,z,N)
	plt.contour(x,-y,z,N)
	ax.set_xlim(-X, X)
	ax.set_ylim(-X, X)
	return wframe,

ani = animation.FuncAnimation(fig, update, frames=250, interval=50)

ani.save('Dipoloosc.mp4')

plt.show()
