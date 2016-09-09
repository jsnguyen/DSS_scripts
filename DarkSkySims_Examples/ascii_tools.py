import numpy as np

#id num_p mvir mbound_vir rvir vmax rvmax vrms x y z vx vy vz Jx Jy Jz E Spin PosUncertainty VelUncertainty bulk_vx bulk_vy bulk_vz BulkVelUnc n_core m200b m200c m500c m2500c Xoff Voff spin_bullock b_to_a c_to_a A[x] A[y] A[z] b_to_a(500c) c_to_a(500c) A[x](500c) A[y](500c) A[z](500c) Rs Rs_Klypin T/|U| M_pe_Behroozi M_pe_Diemer idx i_so i_ph num_cp mmetric

#msw_hdir = "/lustre/atlas1/ast102/scratch/msw/chunk_halos/halos/"
#hfile = "halos_0074173.ascii"


def get_ascii_halos(halo_file, left, right, pos_offset=0.0):
    assert ".ascii" in halo_file
    ident, num_p, mvir, mbound_vir, rvir, vmax, rvmax, vrms, x, y, z, vx, vy, vz, Jx, Jy, Jz, E, Spin, \
        PosUncertainty, VelUncertainty, bulk_vx, bulk_vy, bulk_vz, BulkVelUnc, n_core, \
        m200b, m200c, m500c, m2500c, Xoff, Voff, spin_bullock, b_to_a, c_to_a, \
        Ax, Ay, Az, b_to_a500c, c_to_a500c, Ax500c, Ay500c, \
        Az500c, Rs, Rs_Klypin, kin_to_pot, M_pe_Behroozi, M_pe_Diemer, \
        idx, i_so, i_ph, num_cp, mmetric = np.loadtxt(halo_file, unpack=True)

    #Box size: 7999.999857 Mpc/h
    #Force resolution assumed: 0.0367764 Mpc/h
    #Units: Masses in Msun / h
    #Units: Positions in Mpc / h (comoving)
    #Units: Velocities in km / s (physical, peculiar)
    #Units: Halo Distances, Lengths, and Radii in kpc / h (comoving)
    #Units: Angular Momenta in (Msun/h) * (Mpc/h) * km/s (physical)
    #Units: Spins are dimensionless
    #Np is an internal debugging quantity.
    h = 0.6880620000000001
    for p in [x,y,z]:
        p[:] = (p[:] * 1000 - 4.0e6)/ h  # kpc

    big = np.argmax(m200b)
    xc, yc, zc = x[big], y[big], z[big]
    velc = vmax[big]/0.977792221513 # in kpc/Gyr

    mask = x >= left[0]
    mask *= y >= left[1]
    mask *= z >= left[2]
    mask *= x < right[0]
    mask *= y < right[1]
    mask *= z < right[2]
    halos = {}
    halos['ident'] = ident[mask]
    halos['x'] = x[mask]
    halos['y'] = y[mask]
    halos['z'] = z[mask]
    halos['r200b'] = Rs[mask]
    halos['m200b'] = m200b[mask]
    return halos

