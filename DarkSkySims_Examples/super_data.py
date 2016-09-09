import yt
from yt.funcs import mylog
import numpy as np

known_length_fields = [
    'x','y','z',
]

class SuperData(object):
    def __init__(self, particle_dataset, halo_dataset):
        self.particle_dataset = particle_dataset
        self.halo_dataset = halo_dataset
        original_pds = particle_dataset
        if self.particle_dataset._subspace:
            original_pds = yt.load(particle_dataset.parameter_filename)
        self.full_particle_dataset = original_pds

    def ensure_yt_len(self, position, coords_ds=None):
        if coords_ds is None:
            coords_ds = self.full_particle_dataset
        if not isinstance(position, yt.YTArray):
            position = coords_ds.arr(position, 'code_length')
        return position

    def iter_halos_bbox(self, left, right, fields,
                        coords_ds=None):
        """
        left, right are yt_array's with units
        coords_ds is the dataset used to determine absolute position
        of left/right
        """
        if coords_ds is None:
            coords_ds = self.full_particle_dataset
        print '1', left, right
        left = self.ensure_yt_len(left, coords_ds)
        right = self.ensure_yt_len(right, coords_ds)
        print '2', left, right

        h_dom_c = self.halo_dataset.domain_center.in_units('kpc')
        u_dom_c = coords_ds.domain_center.in_units('kpc')
        offset = h_dom_c - u_dom_c
        print 'Offset:', offset
        h_left = self.halo_dataset.arr(left + offset, 'kpc').in_units('code_length')
        h_right = self.halo_dataset.arr(right + offset, 'kpc').in_units('code_length')
        print '2', h_left, h_right
        print '3', self.halo_dataset.domain_left_edge, self.halo_dataset.domain_right_edge

        for halos in self.halo_dataset.midx.iter_bbox_data(
            h_left.d, h_right.d, fields):
            for f in fields:
                if f in known_length_fields:
                    halos[f] = self.particle_position(halos[f])
            yield halos

    def conv_position(self, old_pos, old_ds, new_ds):
        old_pos = self.ensure_yt_len(old_pos, old_ds)
        h_dom_c = old_ds.domain_center.in_units('kpc')
        p_dom_c = new_ds.domain_center.in_units('kpc')
        offset = p_dom_c - h_dom_c
        assert np.all(offset[0] == offset) # Not a good solution yet for varying offsets
        offset = offset[0]
        new_pos = new_ds.arr(
            halo_position.in_units('kpc') + offset, 'kpc')
        return new_pos.in_units('code_length')

    def conv_arr(self, old_arr, new_ds):
        old_unit = str(old_arr.units)
        old_arr_cgs = old_arr.in_cgs()
        return new_ds.arr(old_arr_cgs.d, str(old_arr_cgs.units)).in_units(old_unit)

    def particle_position(self, halo_position):
        halo_position = self.ensure_yt_len(halo_position, self.halo_dataset)
        h_dom_c = self.halo_dataset.domain_center.in_units('kpc')
        p_dom_c = self.full_particle_dataset.domain_center.in_units('kpc')
        offset = p_dom_c - h_dom_c
        assert np.all(offset[0] == offset) # Not a good solution yet for varying offsets
        offset = offset[0]
        new_pos = self.full_particle_dataset.arr(
            halo_position.in_units('kpc') + offset, 'kpc')
        return new_pos.in_units('code_length')

    def halo_position(self, particle_position):
        particle_position = self.ensure_yt_len(particle_position, self.full_particle_dataset)
        h_dom_c = self.halo_dataset.domain_center.in_units('kpc')
        p_dom_c = self.full_particle_dataset.domain_center.in_units('kpc')
        offset = h_dom_c - p_dom_c
        assert np.all(offset[0] == offset) # Not a good solution yet for varying offsets
        offset = offset[0]
        new_pos = self.halo_dataset.arr(
            particle_position.in_units('kpc') + offset, 'kpc')
        return new_pos.in_units('code_length')

    #ident = halos['id']
    #x = coords_ds.arr(halos['x'], 'Mpccm/h').in_units('kpc') - offset
    #y = coords_ds.arr(halos['y'], 'Mpccm/h').in_units('kpc') - offset
    #z = coords_ds.arr(halos['z'], 'Mpccm/h').in_units('kpc') - offset
    #r200b = full_ds.arr(halos['r200b'], 'Mpccm/h').in_units('kpc')
    #m200b = halos['m200b']
    #hmask = np.ones_like(r200b, dtype='bool')





