import math
import matplotlib.pyplot as plt
from yt.utilities.sdf import load_sdf
import numpy as np

HUBBLE_CONST = 0.688062

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'
sdf_data = load_sdf(sim_file)

save_directory = '/home/jsnguyen/Desktop/DSS_Data/'

difference = []

bins = np.linspace(0, 100, 100)

f_pairs = open(save_directory+'reduced_halo_pairs.txt','r')
f_pairs.next()

for line in f_pairs:

    halo_a = int(line.split()[0])
    halo_b = int(line.split()[1])

    ar200b = sdf_data['r200b'][halo_a]/HUBBLE_CONST
    br200b = sdf_data['r200b'][halo_b]/HUBBLE_CONST

    difference.append(abs(ar200b-br200b))

    #print halo_a,halo_b

f_pairs.close()

plt.subplot(111)
plt.hist(difference,label='Data',histtype='step',linewidth=2.5)
plt.xlabel('Difference Between Halo Pair Indicies')
plt.ylabel('Counts')
plt.legend(loc='upper right')
#plt.yscale('log')
#plt.axis([0, 8, 0, 1000]) #for log plot ymin > 0 (CANNOT BE ZERO!)
plt.grid(True)

plt.show()
