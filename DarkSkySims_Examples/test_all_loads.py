import yt
import numpy as np

#fn = '/nfs/slac/g/ki/darksky/ds14_g/ds14_g_800_4096/ds14_g_800_4096_1.0000'
fn = "http://darksky.slac.stanford.edu/simulations/ds14_g/ds14_g_800_4096/ds14_g_800_4096_1.0000"
midx = fn + '.midx8'
# Simple load
ds = yt.load(fn)

# Better load, gives you midx, but no yt plot functionality
ds = yt.load(fn, midx_filename=midx)
ds.midx

if 'http' in fn:
    pos = np.zeros(3)
else:
    # This takes a while on HTTP. Beware.
    pos = ds.midx.find_max_cell_center()

# Load a bounding box, this allows you to get data.
width = 20000. # kpc
#pos = np.zeros(3)
left = pos - width/2
right = pos + width/2
bbox = np.array([left, right]).T.copy()

ds = yt.load(fn, midx_filename=midx, bounding_box=bbox)
ad = ds.sphere(ds.domain_center, (width/2.,'code_length'))

for ax in 'xyz':
    p = yt.ProjectionPlot(ds, ax, ('deposit','dark_matter_density'),
                          weight_field=None,
                          data_source=ad,
                          center=ds.domain_center,
                          origin='lower-native'
                         )
    p.set_zlim('all',None,'max',dynamic_range=1.0e4)
    p.save()

