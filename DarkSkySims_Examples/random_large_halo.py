import matplotlib; matplotlib.use('Agg')
import matplotlib.pylab as pl
import sys
import yt
import numpy as np
from enhance import enhance
from yt.utilities.sdf import load_sdf
from yt.utilities.lib.image_utilities import add_rgba_points_to_image


raise RuntimeError("Broken Script")
# Find a halo of interest
filename = "http://darksky.slac.stanford.edu/simulations/ds14_a/halos/ds14_a_halos_1.0000"
midx = "http://darksky.slac.stanford.edu/simulations/ds14_a/halos/ds14_a_halos_1.0000.idx0_7"
midx_hdr = "http://darksky.slac.stanford.edu/simulations/ds14_a/halos/ds14_a_halos_1.0000.idx0_7.hdr"

halo_ds = yt.load(filename, midx_filename=midx, midx_header=midx_hdr, midx_level=7)
halo_ds.wandering_particles = False
le = (halo_ds.domain_center - halo_ds.quan(128.0, 'Mpc/h')).in_units('code_length').d
re = (halo_ds.domain_center + halo_ds.quan(128.0, 'Mpc/h')).in_units('code_length').d
max_m = 0.0

for dd in halo_ds.midx.iter_bbox_data(le, re, ['x','y','z','m200b']):
    if dd['m200b'].max() > max_m:
        ind = np.argmax(dd['m200b'])
        max_m = dd['m200b'][ind]
        max_x = dd['x'][ind]
        max_y = dd['y'][ind]
        max_z = dd['z'][ind]

max_halo_ind = np.argmax(dd['m200b'])
print 'Largest halo: %e Msun/h, position: np.array([%e, %e, %e])' % (
    max_m,
    max_x,
    max_y,
    max_z
)

center = halo_ds.arr([max_x, max_y, max_z], 'code_length')
width = halo_ds.quan(20.0, 'Mpc/h')
offset = halo_ds.domain_center
le = center-width/2 - offset
re = center+width/2 - offset

bbox = np.array([le.in_units('kpc').d, re.in_units('kpc').d])

filename = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000"
midx = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000.idx0_9"
midx_hdr = "http://darksky.slac.stanford.edu/simulations/ds14_a/midx10.hdr"
# Load particles
ds = yt.load(filename,
                midx_filename=midx,
                midx_header=midx_hdr,
                midx_level=9,
                bounding_box = bbox,
                )


# Splat 
ad = ds.all_data()
Npix = 1024
image = np.zeros([Npix, Npix, 4], dtype='float64')

cbx = yt.visualization.color_maps.mcm.Reds
col_field = ad['particle_velocity_magnitude']

# Calculate image coordinates ix and iy based on what your view width is
#
ix = (ad['particle_position_x'] - ds.domain_left_edge[0])/ds.domain_width[0]
iy = (ad['particle_position_y'] - ds.domain_left_edge[1])/ds.domain_width[1]
#
col_field = (col_field - col_field.min()) / (col_field.mean() + 4*col_field.std() - col_field.min())
add_rgba_points_to_image(image, ix.astype('float64'), iy.astype('float64'), cbx(col_field))
#

yt.write_bitmap(enhance(image), 'big_halo.png')
print 'Splatted %i particles' % ad['particle_position_x'].size
#
#particle_file = open("largest_halo.npy", 'wb')
#dtype = np.dtype(['x':np.float32, 'y':np.float32, 'z':np.float32, 'r':np.float32])
#
#
#halo_data = np.array([ad['particle_position_x'].T, ad['particle_position_y'].T, ad['particle_position_z'].T, ad['particle_radius'].T], dtype=dtype)
#np.save(particle_file, halo_data)
#
