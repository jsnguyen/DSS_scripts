import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

#There is only one plane of symmetry because when calculating the projection, the orientation of the pair matters.

pi = 3.1459

save_directory = "/home/jsnguyen/DSS_Data/"
f = open(save_directory+"angle_out.txt")
next(f) #skip first line


x=[]
y=[]
z=[]
theta=[]
phi=[]
i=0

#This only reads the first halo in the angles file!

for i in range(1909):
    next (f)

for line in f:
    line = line.strip()
    i+=1
    if "#" in line:
        print i
        print "id:",line[2:]
        break

    theta_t = float(line.split()[0]) #theta
    phi_t = float(line.split()[1])  #phi

    theta.append(theta_t)
    phi.append(phi_t)

    x.append(math.sin(theta_t)*math.cos(phi_t))
    y.append(math.sin(theta_t)*math.sin(phi_t))
    z.append(math.cos(theta_t))

f.close()



fig = plt.figure(figsize=(8,18))
ax = fig.add_subplot(211,projection='3d')
plt.title("id: "+line[2:])

pole_x = np.zeros(2)
pole_y = np.zeros(2)
pole_z = np.linspace(-1.3,1.3,2)
ax.plot(pole_x,pole_y,pole_z,color='r',alpha=0.3,linewidth=3)


u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
sphere_x = np.outer(np.cos(u), np.sin(v))
sphere_y = np.outer(np.sin(u), np.sin(v))
sphere_z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(sphere_x, sphere_y, sphere_z, rstride=4, cstride=4, color='b',alpha=0.1,linewidth=.3)

ax.scatter(x,y,z)

ax.set_xlim3d(-1,1)
ax.set_ylim3d(-1,1)
ax.set_zlim3d(-1,1)

ax.axis("off")

fig.add_subplot(212)
plt.plot(phi,theta,'bo')
plt.xlim(0, 2*pi)
plt.xlabel("phi")
plt.ylim(0, pi)
plt.ylabel("theta")

plt.savefig('pair_n'+line[2:]+'.png')

plt.grid(True)
plt.show()
