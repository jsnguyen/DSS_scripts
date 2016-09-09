from yt.utilities.sdf import load_sdf
from dark_loader import prefix

# Get the filename for the z=0 ds14_a halos.
filename = prefix + "ds14_a/halos/ds14_a_halos_1.0000"

# Load the sdf data directly.
sdfdata = load_sdf(filename)

# sdfdata is now numpy-array like, can you can get arbitrary
# slices into the full dataset
print 'xyz of first halo: ', sdfdata['x'][0], sdfdata['z'][0], sdfdata['y'][0]
print 'Available halo quantities:', sdfdata.keys()
print 'Most massive halo out of the first 1000:', sdfdata['m200b'][:1000].max()

# Now get the the raw particles.
pfilename = prefix + "ds14_a/ds14_a_1.0000"
sdfdata = load_sdf(pfilename)

print 'Total particles: ', sdfdata['x'].size

