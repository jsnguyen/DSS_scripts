# Grabs all relevant information for both halos in a pair from the sim file.
# Header in output file outlines a prototype for the information structure.
# The data straight from the simulation file uses length unit Mpc/h and mass unit Msun/h
# In this file we convert the simulation units to Mpc and Msun
#  In: reduced_halo_pairs.txt, ds14_a_halos_1.0000
# Out: reduced_halo_pairs_full_data.txt

from yt.utilities.sdf import load_sdf
import math

HUBBLE_CONST = 0.688062

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

sdf_data = load_sdf(sim_file)

f_pairs_data = open('/home/jsnguyen/Desktop/reduced_halo_pairs_full_data.txt','w')
f_pairs_data.write('# pair_id\n')
f_pairs_data.write('# ax ay az avx avy avz amvir ar200b\n')
f_pairs_data.write('# bx by bz bvx bvy bvz bmvir br200b\n')
f_pairs_data.close()

f_pairs = open('/home/jsnguyen/Desktop/reduced_halo_pairs.txt','r')
i=0
for line in f_pairs:

    if i % 1000 == 0:
        print i


    halo_a = int(line.split()[0])
    halo_b = int(line.split()[1])

    ax = sdf_data['x'][halo_a]/HUBBLE_CONST
    ay = sdf_data['y'][halo_a]/HUBBLE_CONST
    az = sdf_data['z'][halo_a]/HUBBLE_CONST

    avx = sdf_data['vx'][halo_a]
    avy = sdf_data['vy'][halo_a]
    avz = sdf_data['vz'][halo_a]

    amvir = sdf_data['mvir'][halo_a]/HUBBLE_CONST
    ar200b = sdf_data['r200b'][halo_a]/HUBBLE_CONST

    bx = sdf_data['x'][halo_b]/HUBBLE_CONST
    by = sdf_data['y'][halo_b]/HUBBLE_CONST
    bz = sdf_data['z'][halo_b]/HUBBLE_CONST

    bvx = sdf_data['vx'][halo_b]
    bvy = sdf_data['vy'][halo_b]
    bvz = sdf_data['vz'][halo_b]

    bmvir = sdf_data['mvir'][halo_b]/HUBBLE_CONST
    br200b = sdf_data['r200b'][halo_b]/HUBBLE_CONST

    f_pairs_data = open('/home/jsnguyen/Desktop/reduced_halo_pairs_full_data.txt','a')
    f_pairs_data.write(str(i)+'\n')
    f_pairs_data.write(str(halo_a)+' '+str(ax)+' '+str(ay)+' '+str(az)+' '+str(avx)+' '+str(avy)+' '+str(avz)+' '+str(amvir)+' '+str(ar200b)+' '+'\n')
    f_pairs_data.write(str(halo_b)+' '+str(bx)+' '+str(by)+' '+str(bz)+' '+str(bvx)+' '+str(bvy)+' '+str(bvz)+' '+str(bmvir)+' '+str(br200b)+' '+'\n')

    i+=1

    f_pairs_data.close()


f_pairs.close()
