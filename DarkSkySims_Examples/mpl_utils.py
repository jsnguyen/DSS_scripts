import pylab
import matplotlib
from matplotlib.colors import Normalize, LogNorm
def my_circle_scatter(axes, x_array, y_array, radius=0.5, **kwargs):
    for x, y in zip(x_array, y_array):
        circle = pylab.Circle((x,y), radius=radius, **kwargs)
        axes.add_patch(circle)
    return True

def my_square_scatter(axes, x_array, y_array, size=0.5, **kwargs):
    size = float(size)
    for x, y in zip(x_array, y_array):
        square = pylab.Rectangle((x-size/2,y-size/2), size, size, **kwargs)
        axes.add_patch(square)
    return True

def my_polygon_scatter(axes, x_array, y_array, resolution=5, radius=0.5, **kwargs):
    ''' resolution is number of sides of polygon '''
    for x, y in zip(x_array, y_array):
        polygon = matplotlib.patches.CirclePolygon((x,y), radius=radius, resolution=resolution, **kwargs)
        axes.add_patch(polygon)
    return True

def my_circle_scatter_radii(axes, x_array, y_array, radii_array, mass_array, **kwargs):
    for (x, y, r, m) in zip(x_array, y_array, radii_array, mass_array):
        circle = pylab.Circle((x,y), radius=r, **kwargs)
        circle.set_facecolor( "none" )
        text = pylab.text(x-750, y+r+100, "%0.4e" % m, color='w')
        axes.add_patch(circle)
    return True

#id num_p mvir mbound_vir rvir vmax rvmax vrms x y z vx vy vz Jx Jy Jz E Spin PosUncertainty VelUncertainty bulk_vx bulk_vy bulk_vz BulkVelUnc n_core m200b m200c m500c m2500c Xoff Voff spin_bullock b_to_a c_to_a A[x] A[y] A[z] b_to_a(500c) c_to_a(500c) A[x](500c) A[y](500c) A[z](500c) Rs Rs_Klypin T/|U| M_pe_Behroozi M_pe_Diemer idx i_so i_ph num_cp mmetric


