import math
import matplotlib.pyplot as plt
import numpy as np

HUBBLE_CONST = 0.688062

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

save_directory = '/home/jsnguyen/Desktop/DSS_Data/'

difference = []

bins = np.linspace(0, 100, 100)

f_pairs = open(save_directory+'reduced_halo_pairs.txt','r')
i=0
j=0
for line in f_pairs:

    halo_a = int(line.split()[0])
    halo_b = int(line.split()[1])

    difference.append(abs(halo_a-halo_b))

    if abs(halo_a-halo_b) > 1000:
        j+=1


    i+=1

f_pairs.close()

print float(j)/float(len(difference))

plt.subplot(111)
plt.hist(difference,bins,label='Data',histtype='step',linewidth=2.5)
plt.xlabel('Difference Between Halo Pair Indicies')
plt.ylabel('Counts')
plt.legend(loc='upper right')
#plt.yscale('log')
#plt.axis([0, 8, 0, 1000]) #for log plot ymin > 0 (CANNOT BE ZERO!)
plt.grid(True)

plt.show()
