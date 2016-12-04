import math
import matplotlib.pyplot as plt
import numpy as np


save_directory = '/home/jsnguyen/Dropbox/DSS_Data/'

x = []

bins = np.linspace(0, 1, 100)

f_pairs = open(save_directory+'pair_output_backup.txt','r')

for i in range(3):
    next(f_pairs)

for line in f_pairs:
    line = line.strip() #strips newlines from the end

    #skips the other information stored in the pair_output file
    for i in range(3):
        try:
            next(f_pairs)
        except StopIteration:
            break

    x.append(float(line))

print "total pairs:", len(x)
print "highest probability:",max(x)

plt.subplot(111)
plt.hist(x,bins,label='Data',histtype='step',linewidth=2.5)
plt.title('Musket Ball Cluster Probability Distribution')
plt.xlabel('Probability')
plt.ylabel('Counts')
plt.axis([0, 1, 0, 6000])
plt.grid(True)

plt.show()
