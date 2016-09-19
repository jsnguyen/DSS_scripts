import math
import matplotlib.pyplot as plt
import numpy as np

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

save_directory = '/home/jsnguyen/Desktop/DSS_Data/'

difference = []
a = []
b = []


#bins = np.linspace(0, 10, 10)
j=0
f_pairs = open(save_directory+'reduced_halo_pairs.txt','r')
for line in f_pairs:

    halo_a = int(line.split()[0])
    halo_b = int(line.split()[1])


    a.append(halo_a)
    b.append(halo_b)

f_pairs.close()

for i in range(len(a)):
    if i == len(a)-1:
        break
    if a[i] == a[i+1]:
        j+=1

print j

plt.subplot(111)
plt.hist(j,bins,label='Data',histtype='step',linewidth=2.5)
plt.xlabel('Difference Between Halo Pair Indicies')
plt.ylabel('Counts')
plt.legend(loc='upper right')
#plt.yscale('log')
#plt.axis([0, 8, 0, 1000]) #for log plot ymin > 0 (CANNOT BE ZERO!)
plt.grid(True)

#plt.show()
