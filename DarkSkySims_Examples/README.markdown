Dark Sky Simulations Examples
=============================

Welcome to the dark side. In this repository you'll find a number of example
analysis scripts that can be used to analyze data from the Dark Sky Simulations
Early Data Release.  As opposed to a traditional data product servers, there
are no server-side compute. All data is requested through the world wide
web (WWW), and returned to your locally running analysis for further action.
This allows you request any subset of the data that you'd like, and do whatever
you want with it, without any of us getting in your way.

Before you get started check out the pre-requisites below. 


Prerequisites
-------------

Use a recent version from of https://bitbucket.org/darkskysims/yt-dark.  In 
the near future, all of these capabilities will be included in the main line
of yt, but for now as we work out all the kinks, you'll need this one.

We manage our remote data access through ``thingking``, a handy package that
exposes Numpy ``memmap`` access to data on the WWW.  Grab the latest using
``pip install thingking`` and you should be set. It can also be installed from
source -- just grab a copy from https://bitbucket.org/zeropy/thingking and
run ``python setup.py develop`` or ``python setup.py install``.

If you install thingking from source, you'll need to also manually install the
``requests`` and ``functools32`` packages.


Current Examples
----------------

* ``rzplot.py``: Load the cosmology table used for the ds14 simulations, and
  plot the conformal distance against redshift.
* ``mass_function.py``: Load the mass function histograms from the Dark Sky
  Simulations and plot the mass function and it's relative value to Tinker
  et al 2008.
* ``load_remote_sdf.py``: Load the SDF data directly and print out some
  information.
* ``load_bbox.py``: Load a region around the most massive galaxy cluster in
  ``ds14_a_1.0000`` and create a projection of the dark matter density.
* ``annotated_halo.py``: Load the region around the largest halo in
  ``ds14_a_1.0000`` into ``yt`` and make a projection of the dark matter
  density, annotated by the halo mass and ``R_200`` radius. 
* ``plot_halos.py``: For a sub-volume of the ``ds14_a`` dataset, load up all of
  the particles and halos, annotating all halos above 1e14 Msun/h.
* ``splat_viz.py``: Load up a (100 Mpc)\*\*3 volume, and splat the particles
  using their line-of-sight velocity.
* ``test_all_loads``: Doesn't test *all* of the possible ways to load
  a dataset, but quite a few!
* ``test_performance.py``: Tests how long it takes to access 100 values of
  particle position, all separated by 10M particles. Good way to use a lot of
  bandwidth for very little useful information.
* ``SDSS_photoz.py``: Remotely SDSS catalog of photometric redshift data, and plot
  each objects RA and DEC.



Gotcha's
--------

Many of these examples are designed to use a decent amount of data, but not
a tremendous amount. If things are taking a while, feel free to modify the
examples and either decrease the bounding boxes of the regions you are
interested in, or decrease the number of halos you are attempting to load.
Also, maybe don't use access this from the free coffee shop wireless.

There are some support files in here that will likely make it into a proper
python package at some point, and a few examples that don't currently work, 
and will error saying so.


Contribution
------------

Got an awesome script that you want to share with the world?  Fork this repo
and submit a pull request. We'd love to include it!

