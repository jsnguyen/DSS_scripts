# DSS_scripts

**halo_mass_filter.py**
*Description:* Filters halo by mass (2E14 solar masses). <br />
*Input:* ds14_a_halos_1.0000 <br />
*Output:* mass_filter.txt, writes the indicies and coordinates of the halos. <br />

**reduced_halo_pair_finder.cpp**  <br />
*Description:* Filters halo by separation distance, less than 1.0 Mpc/h <br />
*Input:* mass_filter.txt <br />
*Output:* reduced_halo_pairs.txt, writes the indicies the halos. <br />

**halo_get_pair_data.py** <br />
*Description:* Gets pair data for all the pairs. <br />
*Input:* ds14_a_halos_1.0000, reduced_halo_pairs.txt <br />
*Output:* reduced_halo_pairs_full_data.txt, writes out all relevant halo attributes. <br />

**halo_pair_check.py** <br />
*Description:* Checks if a pair is not itself. (i.e. In the case of halo and its subhalo.) <br />
*Input:* ds14_a_halos_1.0000, reduced_halo_pairs.txt <br />
*Output:* print statements of pairs that are its halo and its subhalo <br />

**pair_search.cpp, pair_search_functions.cpp, pair_search_functions.h** <br />
*Description:* Searches the database of pairs (reduced_halo_pairs_full_data.txt) for specific criterion. Filters by mass, separation and velocity. Checks for a specific viewing angle of the halo system. Integrates spherical coordinates phi and theta over the entire "viewing" sphere and checks if the projected separation and projected velocity are within our search critereon. Makefile produces pair_search.exe as the executable file. <br />
*Input:* reduced_halo_pairs_full_data.txt <br />
*Output:* print statements of pairs that fulfil the critereon <br />

###PRODUCING PAIR DATABASE FILE
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
