from yt.utilities.sdf import load_sdf
import math
import pickler
from collections import defaultdict

HUBBLE_CONST = 0.688062

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

save_directory = '/home/jsnguyen/Desktop/'
save_filename = 'reduced_halo_pairs_full_data_b.txt'
load_filename = 'reduced_halo_pairs_b.txt'

sdf_data = load_sdf(sim_file)

with open(save_directory+save_filename,'w') as f_pairs_data:

#header describes the format of how a pair is stored
#f_pairs_data.write('# pair_id\n')
#f_pairs_data.write('# ax ay az avx avy avz amvir ar200b\n')
#f_pairs_data.write('# bx by bz bvx bvy bvz bmvir br200b\n')

#f_pairs_data.close()
halos=[]
system_holder = defaultdict(list)
indicies=[]
    with open(save_directory+load_filename,'r') as f_pairs:
        f_pairs.next() #skip header line
        i=0
        j=None

        for line in f_pairs:

            if '#' in line:
                new_sys=True
                if not indicies: #is not empty
                    for el in indicies:
                        system_holder[el] = {
                                            'x': None, 'y': None, 'z': None,
                                            'vx': None, 'vy': None, 'vz': None,
                                            'mvir': None, 'ar200b': None
                                            }
            else:
                i+=1
                new_sys=False
                indices.append(int(line))

            if new_sys == True:
                if j is not None:
                    halos.append(system_holder)
                j=1

            system_holder['']

            if i % 1000 == 0:
                print i
            i+=1


            '''
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

            f_pairs_data = open(save_directory+'reduced_halo_pairs_full_data.txt','a')
            f_pairs_data.write(str(i)+'\n')
            f_pairs_data.write(str(halo_a)+' '+str(ax)+' '+str(ay)+' '+str(az)+' '+str(avx)+' '+str(avy)+' '+str(avz)+' '+str(amvir)+' '+str(ar200b)+' '+'\n')
            f_pairs_data.write(str(halo_b)+' '+str(bx)+' '+str(by)+' '+str(bz)+' '+str(bvx)+' '+str(bvy)+' '+str(bvz)+' '+str(bmvir)+' '+str(br200b)+' '+'\n')
            '''
