import math
import matplotlib.pyplot as plt
import numpy as np


save_directory = '/home/jsnguyen/Dropbox/DSS_Data/'

x = []

bins = np.linspace(0, 1, 100)

f_pairs = open(save_directory+'pair_output.txt','r')

for i in range(3):
    next(f_pairs)

for line in f_pairs:
    for i in range(3):
        try:
            next(f_pairs)
        except StopIteration:
            break

    x.append(float(line))
    if float(line) > 0.3:
        print line.strip()

plt.subplot(111)
plt.hist(x,bins,label='Data',histtype='step',linewidth=2.5)
plt.title('Musket Ball Cluster Probability Distribution')
plt.xlabel('Probability')
plt.ylabel('Counts')
#plt.legend(loc='upper right')
#plt.yscale('log')
plt.axis([0, 1, 0, 6000]) #for log plot ymin > 0 (CANNOT BE ZERO!)
plt.grid(True)

plt.show()
