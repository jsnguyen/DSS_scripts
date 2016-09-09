import thingking
import matplotlib.pyplot as plt

# Remotely load the cosmology table associated with the ds14_a simulation.
a = thingking.loadtxt(
    "http://darksky.slac.stanford.edu/data_release/ds14_a/cosmology.tbl"
)

# Plot the distance as a function of redshift.
plt.plot(a[:, 4], a[:, 1])
plt.title("Conformal Distance vs Redshift")

# Add title, limits, and labels.
plt.xlim((0, 10000))
plt.ylim((0, 10))
plt.xlabel("r [Mpc]")
plt.ylabel("z")

# Show it, if you are using an interactive matplotlib backend
plt.show()

# Save the figure
plt.savefig('rzplot.png')
