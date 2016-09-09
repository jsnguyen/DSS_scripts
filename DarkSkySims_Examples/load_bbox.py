import yt
import numpy as np
from dark_loader import load_ds14_a

center = np.array([-2505805.31114929,  -3517306.7572399, -1639170.70554688])
radius = 50.0e3  # 100 Mpc width

bbox = np.array([center-radius, center+radius])
ds = load_ds14_a(midx=True, bbox=bbox)
p = yt.ProjectionPlot(ds, 0, 'dark_matter_density', weight_field=None)
p.save()
