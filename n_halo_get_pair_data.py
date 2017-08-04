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

def write_data(f,data):
    to_write = str(data['x']) + ' '
    to_write += str(data['y']) + ' '
    to_write += str(data['z']) + ' '
    to_write += str(data['vx']) + ' '
    to_write += str(data['vy']) + ' '
    to_write += str(data['vz']) + ' '
    to_write += str(data['mvir']) + ' '
    to_write += str(data['r200b']) + ' '
    to_write += str(data['id']) + ' '
    to_write += str(data['pid']) + '\n'
    f.write(to_write)


sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

root_directory = '/home/jsnguyen/Dropbox/DSS_data/n_system/'
load_file = 'n_subhalo_reduced_5Mpc_mass_filter_subhalo_1e+14.txt'
json_save_file='full_data_'+load_file[:-4]+'.json'
save_file='full_data_'+load_file

json_f = open( root_directory+json_save_file, 'w' )
json_f.close()

txt_f = open( root_directory+save_file, 'w' )
txt_f.write('#### HEADER START #####\n')
txt_f.write('x y z vx vy vz mvir r200b id pid\n')
txt_f.write('#### HEADER END ####\n')
txt_f.close()


with open(root_directory+load_file,'r') as f_pairs:
    f_pairs.next() #skip header line

    sys_counter=0
    for i,line in enumerate(f_pairs):

        if line.strip() == '#### SYSTEM START ####':
            halo_system=[]
            sys_counter+=1
            with open( root_directory+save_file, 'a' ) as txt_f:
                txt_f.write('#### SYSTEM START ####\n')


        elif line.strip() == '#### SYSTEM END ####':
            #print 'dumping to json file...'
            with open( root_directory+json_save_file, 'a' ) as json_f:
                json_f.write(json.dumps(halo_system)+'\n')

            #print 'dumping to txt file...'
            with open( root_directory+save_file, 'a' ) as txt_f:
                txt_f.write('#### SYSTEM END ####\n')

        else:
            index = int(line)
            halo = get_data(sim_file,index)
            halo_system.append(halo)
            with open( root_directory+save_file, 'a' ) as txt_f:
                write_data(txt_f,halo)

        if i % 1000 == 0:
            print i
