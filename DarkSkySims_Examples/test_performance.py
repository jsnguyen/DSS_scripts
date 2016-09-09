import matplotlib; matplotlib.use('Agg')
import matplotlib.pylab as pl
import sys
import yt
import numpy as np
from yt.utilities.sdf import load_sdf
from time import time

filename = "http://darksky.slac.stanford.edu/simulations/ds14_a/ds14_a_1.0000"
sdfdata = load_sdf(filename)

t1 = time()
start = 10000
for i in range(start, start + 100):
    print sdfdata['x'][i * int(1e7)]
t2 = time()
print 'Total time: %e' % (t2-t1)
