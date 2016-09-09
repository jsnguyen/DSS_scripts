from yt.utilities.sdf import load_sdf

filename = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000"
sdfdata = load_sdf(filename)

print 'Total particles: ', sdfdata['x'].size

