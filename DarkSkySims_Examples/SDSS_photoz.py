import thingking
import matplotlib.pyplot as plt
import matplotlib as mpl

references = [
    "http://das.sdss.org/va/photoz2/README",
    "http://adsabs.harvard.edu/abs/2009MNRAS.396.2379C"
]

url = "http://das.sdss.org/va/photoz2/pofz.ra18.0h.dat"

# Specify the data type for each of the columns
type = {'names': ['photoz', 'id', 'ra', 'dec'],
        'formats': ['float64', 'int64', 'float64', 'float64']}
d = thingking.loadtxt(url, usecols=(5, 10, 11, 12), dtype=type)

# Create a cut in photoz redshift
cut = (d['photoz'] > 0.1) & (d['photoz'] < 1.0)

# Create a scatter plot of ra vs dec, colored by redshift
plt.scatter(d['ra'][cut], d['dec'][cut], c=d['photoz'][cut],
            s=4, edgecolors='none', vmin=0, cmap=mpl.cm.spectral)

# Annotate titles, colorbar, and axes
plt.title("SDSS Galaxy Redshift catalog")
plt.colorbar().set_label('Photo z')
plt.xlabel("RA")
plt.ylabel("Dec.")

# Save the figure
plt.savefig("SDSS_photoz.png")
plt.show()
