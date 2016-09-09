import sys
import matplotlib; matplotlib.use('Agg')
import yt
from yt.funcs import mylog
import numpy as np
from super_data import SuperData
from dark_loader import prefix

def halo_plot(pdf, hdf, left, right):

    particles_midx = pdf + ".midx10"
    halos_midx = hdf + ".midx7"

    bbox = np.array([left, right]).T

    pds = yt.load(pdf,
                  midx_filename=particles_midx,
                  bounding_box = bbox,
                  n_ref=32,
                  )
    hds = yt.load(hdf,
                  midx_filename=halos_midx)

    sl = yt.ProjectionPlot(pds, 0, "dark_matter_density",
                           weight_field=None,
                           origin='lower-native')
    sl.set_cmap("all", "Greys")
    sl.set_axes_unit("Gpc")

    sds = SuperData(pds, hds)

    for halos in sds.iter_halos_bbox(left, right,
                                     ['id', 'x','y','z','r200b','m200b']):

        ident = halos['id']
        x = halos['x']
        y = halos['y']
        z = halos['z']
        r200b = sds.conv_arr(sds.halo_dataset.arr(halos['r200b'], 'code_length'),
                             sds.full_particle_dataset)
        m200b = halos['m200b']
        hmask = np.ones_like(r200b, dtype='bool')
        hmask = m200b > 1.0e14

        mylog.info("Annotating %i halos" % (hmask.sum()))
        for hid, hmass, hx, hy, hz, hr in zip(ident[hmask], m200b[hmask], x[hmask], y[hmask], z[hmask], r200b[hmask]):
            sl.annotate_sphere(np.array([hx, hy, hz]), hr, text=r"$%0.1f\times10^{14}$" % (hmass/1.0e14),
                               text_args={"color":'r', 'size':'large', 'weight':'heavy'}, circle_args={"color":'r'})

    sl.save()

if __name__ == "__main__":
    root_dir = prefix + 'ds14_a/'
    particles = root_dir + "ds14_a_1.0000"
    halos = root_dir + "halos/ds14_a_halos_1.0000"

    center = np.array([1000.0]*3)*1.0e3 # kpc, no h's!
    width = np.array([100.0]*3) * 1e3 # kpc, no h's!
    width[0] /= 10
    left = center - width/2
    right = center + width/2

    halo_plot(particles, halos, left, right)
