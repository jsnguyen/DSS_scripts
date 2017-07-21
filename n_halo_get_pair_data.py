from yt.utilities.sdf import load_sdf
import math
import pickle
import json

def get_data(sim_file,halo_index):

    HUBBLE_CONST = 0.688062

    sdf_data = load_sdf(sim_file)

    x = float(sdf_data['x'][halo_index]/HUBBLE_CONST)
    y = float(sdf_data['y'][halo_index]/HUBBLE_CONST)
    z = float(sdf_data['z'][halo_index]/HUBBLE_CONST)

    vx = float(sdf_data['vx'][halo_index])
    vy = float(sdf_data['vy'][halo_index])
    vz = float(sdf_data['vz'][halo_index])

    mvir = float(sdf_data['mvir'][halo_index]/HUBBLE_CONST)
    r200b = float(sdf_data['r200b'][halo_index]/HUBBLE_CONST)

    hid = int(sdf_data['id'][halo_index])
    hpid = int(sdf_data['pid'][halo_index])

    data = {'x':x,'y':y,'z':z,
            'vx':vx,'vy':vy,'vz':vz,
            'mvir':mvir,'r200b':r200b,
            'id':hid, 'pid':hpid}

    return data


sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

root_directory = '/home/jsnguyen/DSS_data/'
load_file = 'n_subhalo_reduced_5Mpc_mass_filter_subhalos_1e+14.txt'
save_file='full_data_'+load_file[:-4]+'.json'

json_f = open( root_directory+save_file, 'w' )
json_f.close()

with open(root_directory+load_file,'r') as f_pairs:
    f_pairs.next() #skip header line

    sys_counter=0
    for i,line in enumerate(f_pairs):

        if line.strip() == '#### SYSTEM START ####':
            halo_system=[]
            sys_counter+=1

        elif line.strip() == '#### SYSTEM END ####':
            #print 'dumping to json file...'
            with open( root_directory+save_file, 'a' ) as json_f:
                json_f.write(json.dumps(halo_system)+'\n')

        else:
            index = int(line)
            halo = get_data(sim_file,index)
            halo_system.append(halo)

        if i % 1000 == 0:
            print i
