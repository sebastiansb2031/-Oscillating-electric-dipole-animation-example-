
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
r,theta = meshgrid( linspace(0.4,10,200), linspace(0,2*pi,360))
x=r*cos(theta);
y=r*sin(theta);


font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

def update(t):
	plt.cla()	
	plt.title('Campo Electrico Radiado por un Dipolo Electrico Oscilante ', fontdict=font)
	z = power((sin(theta+pi/2)),2)*((1/power(r,2))+1)*cos(0.4*t-r+arctan(r))
	wframe=ax.plot_surface(x,y,z,rstride=1, cmap=cm.Spectral,linewidth=0, antialiased=False)
	ax.set_xlim(-10, 10)
	ax.set_ylim(-10, 10)
        ax.set_zlim(-10,10)
	return wframe,

ani = animation.FuncAnimation(fig, update, frames=250, interval=50)

ani.save('Dipoloosc.mp4')

plt.show()
