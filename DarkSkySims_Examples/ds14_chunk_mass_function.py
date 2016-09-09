import matplotlib; matplotlib.use('Agg')
import matplotlib.pylab as pl
import yt
from yt.funcs import mylog
import numpy as np
from time import time
from dark_loader import load_ds14_a_halos


# Choose your sub-volume size and position.
# Here we choose the lower left 200 Mpc/h.
L = 200 # Mpc/h
center = np.array([L/2, L/2, L/2])

# Create bounding box
bbox = np.array([center - L/2, 
                 center + L/2])

# Create bins for mass function
bins = np.logspace(12, 16.0, 128)

# Make a little timer to see how well we did.
t1 = -time()

# Load ds14_a_halos_1.0000, using the default midx.
ds = load_ds14_a_halos(midx=True, bbox=bbox)

# Get all the data
ad = ds.all_data()

# Get m200b array in Msun/h units
m200b = ad['m200b'].in_units('Msun/h')
mylog.info("Maximum halo mass: %e Msun/h" % m200b.max())
hist, bins = np.histogram(m200b, bins=bins)
t1 += time()
mylog.info("Total time to read %i m200b from 1Gpc^3: %e seconds" % (m200b.size, t1))

# Create N(M) plot
pl.loglog(bins[:-1], hist)
pl.xlabel('m200b')
pl.ylabel('N(M)')
pl.savefig("n_of_m.png")

# Create N(>M) plot
ngtm = np.cumsum(hist[::-1])[::-1]
pl.clf()
pl.loglog((bins[1:] + bins[:-1])/2, ngtm, ls='steps')
pl.xlabel('m200b')
pl.ylabel('N(>M)')
pl.savefig("ngtm.png")

