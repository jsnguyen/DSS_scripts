from yt.utilities.sdf import load_sdf
import math
import pickle

def get_data(sim_file,halo_index):

    HUBBLE_CONST = 0.688062

    sdf_data = load_sdf(sim_file)



    x = sdf_data['x'][halo_index]/HUBBLE_CONST
    y = sdf_data['y'][halo_index]/HUBBLE_CONST
    z = sdf_data['z'][halo_index]/HUBBLE_CONST

    vx = sdf_data['vx'][halo_index]
    vy = sdf_data['vy'][halo_index]
    vz = sdf_data['vz'][halo_index]

    mvir = sdf_data['mvir'][halo_index]/HUBBLE_CONST
    r200b = sdf_data['r200b'][halo_index]/HUBBLE_CONST

    data = {'x':x,'y':y,'z':z,
            'vx':vx,'vy':vy,'vz':vz,
            'mvir':mvir,'r200b':r200b}

    return data



sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

root_directory = '/home/jsnguyen/Desktop/'
save_file='reduced_halo_pairs_1e14_5Mpc_b_full_data.p'

load_file = 'reduced_halo_pairs_1e14_5Mpc_b.txt'

#f_pairs_data = open(save_directory+'reduced_halo_pairs_full_data.txt','w')

#header describes the format of how a pair is stored
#f_pairs_data.write('# pair_id\n')
#f_pairs_data.write('# ax ay az avx avy avz amvir ar200b\n')
#f_pairs_data.write('# bx by bz bvx bvy bvz bmvir br200b\n')

#f_pairs_data.close()

n_halo_system=[]
n_halo_system.append([])


with open(root_directory+load_file,'r') as f_pairs:
    f_pairs.next() #skip header line

    j=None
    sys_counter=0
    for i,line in enumerate(f_pairs):
        halo={}

        if '#' in line:
            new_sys=True

        else:
            j+=1
            index = int(line)
            halo[index] = get_data(sim_file,index)
            n_halo_system[sys_counter].append(halo)
            new_sys=False

        if new_sys == True:
            if j is not None:
                n_halo_system.append([])
                sys_counter+=1
            j=1


        if i % 1000 == 0:
            print i

    print 'dumping to pickle file...'
    pickle.dump( n_halo_system, open( root_directory+save_file, 'wb' ) )



        #f_pairs_data = open(save_directory+'reduced_halo_pairs_full_data.txt','a')
        #f_pairs_data.write(str(i)+'\n')
        #f_pairs_data.write(str(halo_a)+' '+str(ax)+' '+str(ay)+' '+str(az)+' '+str(avx)+' '+str(avy)+' '+str(avz)+' '+str(amvir)+' '+str(ar200b)+' '+'\n')
        #f_pairs_data.write(str(halo_b)+' '+str(bx)+' '+str(by)+' '+str(bz)+' '+str(bvx)+' '+str(bvy)+' '+str(bvz)+' '+str(bmvir)+' '+str(br200b)+' '+'\n')

        #f_pairs_data.close()
