import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

pi = 3.1459

save_directory = "/home/jsnguyen/Dropbox/DSS_Data/"
f = open(save_directory+"angle_out.txt")
lines = f.readlines()

x=[]
y=[]
z=[]
theta=[]
phi=[]

for i in range(len(lines)):
    lines[i] = lines[i].split("\n")[0]

for i in range(10299,len(lines)):
    if lines[i] == "#":
        j=i+1
        while lines[j] != "#":
            theta.append(float(lines[j].split()[0])) #theta
            phi.append(float(lines[j].split()[1])) #phi
            j+=1
        print "next halo:",j
        for k in range(len(theta)):
            x.append(math.sin(theta[k])*math.cos(phi[k]))
            y.append(math.sin(theta[k])*math.sin(phi[k]))
            z.append(math.cos(theta[k]))

    break


fig = plt.figure(figsize=(8,16))
ax = fig.add_subplot(211,projection='3d')

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

fig.suptitle('Pair Id:',fontsize=30)
ax.axis("off")

fig.add_subplot(212)
plt.plot(phi,theta,'bo')
plt.xlim(0, pi/2)
plt.xlabel("phi")
plt.ylim(0, pi/2)
plt.ylabel("theta")

plt.grid(True)

theta_c=0
phi_c=0

for i in range(len(phi)):
    if pi <= phi[i] <= 3*pi/2:
        phi_c+=1

print phi_c

plt.show()
