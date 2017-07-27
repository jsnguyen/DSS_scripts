from yt.utilities.sdf import load_sdf
import math
import pickle

if __name__ == '__main__':
    sim_file = 'http://darksky.slac.stanford.edu/simulations/ds14_a/halos/ds14_a_halos_1.0000'
    sdf_data = load_sdf(sim_file)

    halo_indicies = [2086547,2086548,5551226,5551236,9111737,9111738,9440750,9440751,15150723,15150724,15357514,15357515,16173589,16173908]

    for halo_index in halo_indicies:
        print '###############################'
        print 'halo_index:', halo_index
        print sdf_data['x'][halo_index],sdf_data['y'][halo_index],sdf_data['z'][halo_index]
        print sdf_data['vx'][halo_index],sdf_data['vy'][halo_index],sdf_data['vz'][halo_index]
        print sdf_data['mvir'][halo_index],sdf_data['r200b'][halo_index]
        print 'pId:', sdf_data['pid'][halo_index]
