import math
import matplotlib.pyplot as plt
import numpy as np

filename = '/home/jsnguyen/Desktop/reduced_halo_pairs_1e14_5Mpc.txt'

halos=[]
new_sys=False
i=None
with open(filename) as f:
    f.next() #skip header
    for line in f:

        if '#' in line:
            new_sys=True
        else:
            i+=1
            new_sys=False

        if new_sys == True:
            if i is not None:
                halos.append(i)
            i=1

for el in set(halos):
    print el,'halo systems:',halos.count(el)
