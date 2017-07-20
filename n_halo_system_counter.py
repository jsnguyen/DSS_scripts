import math
import matplotlib.pyplot as plt
import numpy as np

filename = '/home/jsnguyen/DSS_data/n_subhalo_reduced_5Mpc_mass_filter_subhalos_1e+14.txt'

halos=[]
new_sys=False

with open(filename) as f:
    f.next() #skip header
    for line in f:

        if line.strip() == '#### SYSTEM START ####':
            i=0

        elif line.strip() == '#### SYSTEM END ####':
            if i is not None:
                halos.append(i)

        else:
            i+=1


for el in set(halos):
    print el,'halo systems:',halos.count(el)
