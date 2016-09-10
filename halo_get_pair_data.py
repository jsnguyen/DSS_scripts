# Grabs all relevant information for both halos in a pair from the sim file.
# Header in output file outlines a prototype for the information structure.
#  In: reduced_halo_pairs.txt, ds14_a_halos_1.0000
# Out: reduced_halo_pairs_full_data.txt

from yt.utilities.sdf import load_sdf
import math

def mag(ax,ay,az,bx,by,bz): # A relative to B
    mag = math.sqrt( ((ax-bx)*(ax-bx)) + ((ay-by)*(ay-by)) + ((az-bz)*(az-bz)) )
    return mag

def scalar_proj(ax,ay,az,bx,by,bz): # scalar projection of B onto A
    proj = ( (ax*bx) + (ay*by) + (az*bz) ) / mag(ax,ay,az,0,0,0)
    return proj

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

sdf_data = load_sdf(sim_file)

f_pairs_data = open('../reduced_halo_pairs_full_data.txt','w')
f_pairs_data.write('# pair_id\n')
f_pairs_data.write('# ax ay az avx avy avz amvir ar200b\n')
f_pairs_data.write('# bx by bz bvx bvy bvz bmvir br200b\n')
f_pairs_data.write('# separation mag_rel_v scalar_proj\n')
f_pairs_data.close()

f_pairs = open('reduced_halo_pairs.txt','r')
i=0
for line in f_pairs:

    if i % 1000 == 0:
        print i


    halo_a = int(line.split()[0])
    halo_b = int(line.split()[1])

    ax = sdf_data['x'][halo_a]
    ay = sdf_data['y'][halo_a]
    az = sdf_data['z'][halo_a]

    avx = sdf_data['vx'][halo_a]
    avy = sdf_data['vy'][halo_a]
    avz = sdf_data['vz'][halo_a]

    amvir = sdf_data['mvir'][halo_a]
    ar200b = sdf_data['r200b'][halo_a]

    bx = sdf_data['x'][halo_b]
    by = sdf_data['y'][halo_b]
    bz = sdf_data['z'][halo_b]

    bvx = sdf_data['vx'][halo_b]
    bvy = sdf_data['vy'][halo_b]
    bvz = sdf_data['vz'][halo_b]

    bmvir = sdf_data['mvir'][halo_b]
    br200b = sdf_data['r200b'][halo_b]

    separation = mag(ax,ay,az,bx,by,bz)
    rel_vel = mag(avx,avy,avz,bvx,bvy,bvz)
    scal_p = scalar_proj(ax-bx,ay-by,az-bz,avx-bvx,avy-bvy,avz-bvz) #separation is A vector, velocity is B vector

    f_pairs_data = open('reduced_halo_pairs_full_data.txt','a')
    f_pairs_data.write(str(i)+'\n')
    f_pairs_data.write(str(halo_a)+' '+str(ax)+' '+str(ay)+' '+str(az)+' '+str(avx)+' '+str(avy)+' '+str(avz)+' '+str(amvir)+' '+str(ar200b)+' '+'\n')
    f_pairs_data.write(str(halo_b)+' '+str(bx)+' '+str(by)+' '+str(bz)+' '+str(bvx)+' '+str(bvy)+' '+str(bvz)+' '+str(bmvir)+' '+str(br200b)+' '+'\n')
    f_pairs_data.write(str(separation)+' '+str(rel_vel)+' '+str(scal_p)+'\n')

    i+=1

    f_pairs_data.close()


f_pairs.close()
