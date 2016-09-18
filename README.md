# DSS_scripts
Dark Sky Simulation pair search scripts.

**halo_mass_filter.py**
Filters halo by mass (2E14 solar masses). 
Input: ds14_a_halos_1.0000
Output: mass_filter.txt, writes the indicies and coordinates of the halos.

**reduced_halo_pair_finder.cpp**
Filters halo by separation distance, less than 1.0 Mpc/h
Input: mass_filter.txt
Output: reduced_halo_pairs.txt, writes the indicies the halos.

**halo_get_pair_data.py**
Gets pair data for all the pairs.
Input: ds14_a_halos_1.0000, reduced_halo_pairs.txt
Output: reduced_halo_pairs_full_data.txt, writes out all relevant halo attributes.

**halo_pair_check.py**
Checks if a pair is not itself. (i.e. In the case of halo and its subhalo.)
Input: ds14_a_halos_1.0000, reduced_halo_pairs.txt
Output: print statements of pairs that are its halo and its subhalo

**pair_search.cpp, pair_search_functions.cpp, pair_search_functions.h**
Searches the database of pairs (reduced_halo_pairs_full_data.txt) for specific criterion.
Filters by mass, separation and velocity. Checks for a specific viewing angle of the
halo system. Integrates spherical coordinates phi and theta over the entire "viewing" sphere
and checks if the projected separation and projected velocity are within our search critereon.
Makefile produces pair_search.exe as the executable file.
Input: reduced_halo_pairs_full_data.txt
Output: print statements of pairs that fulfil the critereon

##PRODUCING PAIR DATABASE FILE
halo_mass_filter.py
        |
        | mass_filter.txt
        v
reduced_halo_pair_finder.cpp
        |
        | reduced_halo_pairs.txt
        v
halo_get_pair_data.py
        |
        | reduced_halo_pairs_full_data.txt
        v
halo_pair_check.py (optional, this step is to verify that the pairs are correct.)
        |
        |
        v
reduced_halo_pairs_full_data.txt
