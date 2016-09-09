from yt.utilities.sdf import load_sdf

sim_file = '/media/jsnguyen/JK-PEXHD/ds14_a_halos_1.0000'


sdf_data = load_sdf(sim_file)

f_pairs = open('reduced_halo_pairs.txt','r')
i=0
for line in f_pairs:

    if i % 1000 == 0:
        print i


    halo_a = int(line.split()[0])
    halo_b = int(line.split()[1])

    #print sdf_data['mvir'][halo_a],',{',sdf_data['x'][halo_a],',',sdf_data['y'][halo_a],',',sdf_data['z'][halo_a],'}'
    #print sdf_data['mvir'][halo_b],',{',sdf_data['x'][halo_b],',',sdf_data['y'][halo_b],',',sdf_data['z'][halo_b],'}'

    if sdf_data['x'][halo_a] == sdf_data['x'][halo_b] and sdf_data['y'][halo_a] == sdf_data['y'][halo_b] and sdf_data['z'][halo_a] == sdf_data['z'][halo_b]:
        print halo_a
        print halo_b

    i+=1
