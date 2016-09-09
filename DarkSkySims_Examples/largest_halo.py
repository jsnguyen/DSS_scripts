import matplotlib; matplotlib.use('Agg')
import matplotlib.pylab as pl
import sys
import yt
from yt.mods import mylog
import numpy as np
from yt.utilities.lib.image_utilities import add_rgba_points_to_image
from dark_loader import load_ds14_a
from enhance import enhance


center = np.array([-2505805.31114929,  -3517306.7572399, -1639170.70554688])
radius = 50000.0 # 50 Mpc
bbox = np.array([center-radius, center+radius])

print bbox
ds = load_ds14_a(midx=True, bbox=bbox)

ad = ds.all_data()
Npix = 2048
image = np.zeros([Npix, Npix, 4], dtype='float64')

cbx = yt.visualization.color_maps.mcm.seismic
col_field = ad['particle_velocity_z'].in_units('km/s').d

# Calculate image coordinates ix and iy based on what your view width is
#
ix = (ad['particle_position_x'] - ds.domain_left_edge[0])/ds.domain_width[0]
iy = (ad['particle_position_y'] - ds.domain_left_edge[1])/ds.domain_width[1]
#
col_min = col_field.min()
col_max = col_field.max()
col_mean = col_field.mean()
print col_min, col_max, col_mean
col_min = col_mean - 200.0
col_max = col_mean + 200.0

col_field = (col_field - col_min) / (col_max-col_min)
np.clip(col_field, 0.0, 1.0)
add_rgba_points_to_image(image, ix.astype('float64'), iy.astype('float64'), cbx(col_field))
#

yt.write_bitmap(image, 'all_channels.png')
yt.write_bitmap(image[:,:,:3], 'black_background.png')

# # OR
yt.write_bitmap(enhance(image), 'enhanced.png')
print 'Splatted %i particles' % ad['particle_position_x'].size
