114219 * 3.9e10
114219 * 3.9e10/1.0e15
p = yt.ProjectionPlot(ds, 0, ('deposit', 'all_density'), weight_field=None, origin='left-domain')
p.save()
bp = yt.BinnedProfile1D?
bp = yt.BinnedProfile1D(ds.all_data(), 128, 'particle_radius', (10.0, 'kpc'), (10.0, 'mpc'))
bp = yt.BinnedProfile1D(ds.all_data(), 128, 'particle_radius', ds.quan(10.0, 'kpc'), ds.quan(10.0, 'mpc'))
bp.add_fields?
bp.add_fields(['particle_mass'], weight=None, accumulation=False, fractional=False)
pl.figure(figsize=[10.,10.])
pl.loglog(bp._bins, bp['particle_mass'])
bp._bins
ad
ad['particle_radius'].min()
ad['particle_radius'].max()
ad['particle_radius'].min().in_units('kpc/h')
ad.center
ds.domain_center
max_x
bp = yt.BinnedProfile1D(ds.all_data(), 128, 'particle_radius', ds.quan(10.0, 'kpc'), ds.quan(10.0, 'Mpc/h'))
bp.add_fields(['particle_mass'], weight=None, accumulation=False, fractional=False)
pl.clf()
pl.loglog(bp._bins, bp['particle_mass'])
bp._bins
bp = yt.BinnedProfile1D(ds.all_data(), 128, 'particle_radius', ds.quan(10.0, 'kpc').in_units('cm'), ds.quan(10.0, 'Mpc/h').in_units('cm'))
bp.add_fields(['particle_mass'], weight=None, accumulation=False, fractional=False)
bp._bins
bp['particle_mass']
radius = ds.arr(bp._bins, 'cm').in_units('Mpc/h')
mass = ds.arr(bp['particle_mass'], 'g').in_units('Msun/h')
pl.loglog(radius, mass)
mass
radius
radius.shape
mass.shape
pl.loglog(radius.d, mass.d)
pl.clf()
pl.loglog(radius.d, mass.d)
pl.loglog(radius, mass)
pl.clf()
pl.loglog(radius, mass, )
pl.loglog(radius, mass, 'k')
pl.clf()
pl.loglog(radius, mass, 'k')
pl.xlabel('r [Mpc/h]')
pl.loglog(radius[:-1], mass[:-1]/(4*np.pi*radius[:-1]**2 * (radius[1:]-radius[:-1])), 'k')
pl.clf()
pl.loglog(radius[:-1], mass[:-1]/(4*np.pi*radius[:-1]**2 * (radius[1:]-radius[:-1])), 'k')
pl.xlabel('r [Mpc/h]')
pl.ylabel(r'$\rho_{dm} [(Msun/h)/(Mpc/h)^3$]')
pl.savefig('rhodm_vs_r.png')
hist -f dm_profile.py
