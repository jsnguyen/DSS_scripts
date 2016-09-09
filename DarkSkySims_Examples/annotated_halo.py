import sys
import matplotlib; matplotlib.use('Agg')
from dark_loader import load_halo, prefix
import yt

if __name__ == "__main__":
    root_dir = prefix + 'ds14_a/'
    particles = root_dir + "ds14_a_1.0000"
    halos = root_dir + "halos/ds14_a_halos_1.0000"

    halo_num = 0
    if len(sys.argv) > 1:
        halo_num = int(sys.argv[-1])

    pds, halo, center, radius = load_halo(particles, halos, halo_num)
    p = yt.ProjectionPlot(pds, 0, "dark_matter_density",
                          weight_field=None)
    p.annotate_sphere(center, radius, circle_args={'color':'r'})
    p.annotate_title(r"$M_{200b} = %0.2e \mathrm{M_{\odot}/h}$" % halo['m200b'])
    p.set_cmap("all", "RdGy_r")
    p.set_axes_unit("Mpccm/h")
    p.set_zlim('all', 1.0e-3, 1.0)
    p.save('halo_%04i' % halo_num)

