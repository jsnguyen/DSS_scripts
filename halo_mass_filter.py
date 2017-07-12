from yt.utilities.sdf import load_sdf
import time

start_time = time.time()

sim_file ='/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'

save_directory = '/home/jsnguyen/DSS_data/'

N_TOTAL_HALOS = 4675339354 #total number of halos in the file
HUBBLE_CONST = 0.688062

mass_type = 'mvir' #measure of mass
mass_cutoff = 6e13 #cutoff limit
n_halos = N_TOTAL_HALOS #number of halos searched through

f_mass_filter_halos = open(save_directory+'mass_filter_halos_'+str(mass_cutoff)+'.txt','w')
f_mass_filter_halos.write('#mass_type '+mass_type+'\n'+'#mass_cutoff (Msun) '+str(mass_cutoff)+'\n'+'#n_halos '+str(n_halos)+'\n') #header
f_mass_filter_halos.close()

f_mass_filter_subhalos = open(save_directory+'mass_filter_subhalos_'+str(mass_cutoff)+'.txt','w')
f_mass_filter_subhalos.write('#mass_type '+mass_type+'\n'+'#mass_cutoff (Msun) '+str(mass_cutoff)+'\n'+'#n_halos '+str(n_halos)+'\n') #header
f_mass_filter_subhalos.close()

f_mass_filter_halos = open(save_directory+'mass_filter_halos_'+str(mass_cutoff)+'.txt','a')
f_mass_filter_subhalos = open(save_directory+'mass_filter_subhalos_'+str(mass_cutoff)+'.txt','a')

sdf_data = load_sdf(sim_file)

i = 0
while i < n_halos:

    if i%1000000 == 0:
        print i

    if sdf_data['mvir'][i]/HUBBLE_CONST > mass_cutoff:

        x = str(sdf_data['x'][i]/HUBBLE_CONST)
        y = str(sdf_data['y'][i]/HUBBLE_CONST)
        z = str(sdf_data['z'][i]/HUBBLE_CONST)

        halo_data = str(i)+ ' ' + x + ' ' + y + ' ' + z + '\n'

        if int(sdf_data['pid'][i]) == -1:
            f_mass_filter_halos.write(halo_data) #only writes halo indicies
        else:
            f_mass_filter_subhalos.write(halo_data) #only writes halo indicies

    i+=1

f_mass_filter_halos.close()
f_mass_filter_subhalos.close()

print ('The script took {0} seconds!'.format(time.time() - start_time))
