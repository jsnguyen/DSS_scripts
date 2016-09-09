import matplotlib; matplotlib.use('Agg')
matplotlib.rcParams['font.size']=14
matplotlib.rcParams['lines.linewidth']=2
matplotlib.rcParams['axes.linewidth']=2
matplotlib.rcParams['axes.grid']=True
import matplotlib.pylab as pl
import sys
import yt
import numpy as np
from yt.utilities.sdf import load_sdf

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

# Get the halo position in ds14_a coordinates.  Need to subtract
# off the halo catalog dataset center, and convert everything to
# code lengths of ds14_a (kpccm).
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

# Create a projection, just for fun.
p = yt.ProjectionPlot(ds, 0, ('deposit', 'all_density'),
                      weight_field=None, origin='left-domain')
p.save('halo_proj')

# Create a binned profile. This needs to be set up in units of cm, and can later be converted back to whatever we want.
bp = yt.BinnedProfile1D(ds.all_data(), 128, 'particle_radius',
                        ds.quan(10.0, 'kpc/h').in_units('cm'),
                        ds.quan(10.0, 'Mpc/h').in_units('cm'))
bp.add_fields(['particle_mass'], weight=None,
              accumulation=False, fractional=False)
radius = ds.arr(bp._bins, 'cm').in_units('Mpc/h')
mass = ds.arr(bp['particle_mass'], 'g').in_units('Msun/h')
volume = 4*np.pi*radius[:-1]**2 * (radius[1:]-radius[:-1])
density = mass[:-1]/volume

pl.figure(figsize=[8,8])
pl.loglog(radius[:-1], density, 'k')
pl.xlabel(r'$r [Mpc/h]$')
pl.ylabel(r'$\rho_{dm} [(Msun/h)/(Mpc/h)^3]$')
pl.savefig('rhodm_vs_r.png')
