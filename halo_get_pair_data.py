from yt.utilities.sdf import load_sdf
import math

HUBBLE_CONST = 0.688062

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

save_dir = '/home/jsnguyen/DSS_data/'

load_data_fn = 'reduced_5Mpc_mass_filter_subhalos_1e+14.txt'

save_data_fn = 'full_data_'+load_data_fn

sdf_data = load_sdf(sim_file)

f_pairs_data = open(save_dir+save_data_fn,'w')

#header describes the format of how a pair is stored
f_pairs_data.write('# pair_id\n')
f_pairs_data.write('# ax ay az avx avy avz amvir ar200b aid apid\n')
f_pairs_data.write('# bx by bz bvx bvy bvz bmvir br200b aid apid\n')

f_pairs_data.close()

f_pairs = open(save_dir+load_data_fn,'r')
f_pairs.next() #skip header line
i=0
for line in f_pairs:

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

    aid = sdf_data['id'][halo_a]/HUBBLE_CONST
    apid = sdf_data['pid'][halo_a]/HUBBLE_CONST

    bx = sdf_data['x'][halo_b]/HUBBLE_CONST
    by = sdf_data['y'][halo_b]/HUBBLE_CONST
    bz = sdf_data['z'][halo_b]/HUBBLE_CONST

    bvx = sdf_data['vx'][halo_b]
    bvy = sdf_data['vy'][halo_b]
    bvz = sdf_data['vz'][halo_b]

    bmvir = sdf_data['mvir'][halo_b]/HUBBLE_CONST
    br200b = sdf_data['r200b'][halo_b]/HUBBLE_CONST

    bid = sdf_data['id'][halo_a]
    bpid = sdf_data['pid'][halo_a]

    f_pairs_data = open(save_dir+save_data_fn,'a')
    f_pairs_data.write(str(i)+'\n')
    f_pairs_data.write(str(halo_a)+' '+str(ax)+' '+str(ay)+' '+str(az)+' '+str(avx)+' '+str(avy)+' '+str(avz)+' '+str(amvir)+' '+str(ar200b)+' '+str(aid)+' '+str(apid)+' '+'\n')
    f_pairs_data.write(str(halo_b)+' '+str(bx)+' '+str(by)+' '+str(bz)+' '+str(bvx)+' '+str(bvy)+' '+str(bvz)+' '+str(bmvir)+' '+str(br200b)+' '+str(bid)+' '+str(bpid)+' '+'\n')

    if i % 1000 == 0:
        print 'pair no.', i

    i+=1

    f_pairs_data.close()

f_pairs.close()
