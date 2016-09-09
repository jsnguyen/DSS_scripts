# Jayke Nguyen 5-27-16
# Gets halo data from internet, scans all the halos and checks the
# mass to see if it's greater than 2e14 mass sun


from yt.utilities.sdf import load_sdf
import time

start_time = time.time()

sim_file ='http://darksky.slac.stanford.edu/simulations/ds14_a/halos/ds14_a_halos_1.0000'

N_TOTAL_HALOS = 4675339354 #total number of halos in the file

mass_type = 'mvir' #measure of mass
mass_cutoff = 2e14 #cutoff limit
n_halos = N_TOTAL_HALOS #number of halos searched through

f_mass_filter = open('mass_filter.txt','w')
f_mass_filter.write('#mass_type '+mass_type+'\n'+'#mass_cutoff '+str(mass_cutoff)+'\n'+'#n_halos '+str(n_halos)+'\n')
f_mass_filter.close()

sdf_data = load_sdf(sim_url+halos)

for i in range(n_halos):

    if i%100000 == 0:
        print i

    if sdf_data['mvir'][i] > mass_cutoff:
        f_mass_filter = open('mass_filter.txt','a')
        f_mass_filter.write(str(i)+'\n') #only writes halo indicies
        f_mass_filter.close()

print ('The script took {0} seconds!'.format(time.time() - start_time))
