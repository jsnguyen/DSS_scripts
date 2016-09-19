# DSS_scripts

**Notes** <br />
*Sim Units*: <br />
*Length: Mpccm/h, (comoving)
*Mass: Msun/h

Sim units are ALWAYS converted from unit/h to unit when getting data from the sim file. <br />
Using virial mass (mvir) and 200b radius (r200b). <br />
Most output files will have a header with a prototype of how the data is stored <br />

**halo_mass_filter.py** <br />
*Description:* Filters halo by preset mass. Variable is mass_cutoff, units of Msun. <br />
*Input:* ds14_a_halos_1.0000 <br />
*Output:* mass_filter.txt, writes the indicies and coordinates of the halos. <br />

**reduced_halo_pair_finder.cpp**  <br />
*Description:* Filters halo by separation distance, less than 1.0 Mpc/h. Creates a very large vector, requires ~1.3 Gb of RAM. Stores all the data from the file in memory because repeated file access is very costly. <br />
*Input:* mass_filter.txt <br />
*Output:* reduced_halo_pairs.txt, writes the indicies the halo pairs. <br />

**halo_get_pair_data.py** <br />
*Description:* Gets pair data for all the pairs from the sim file. <br />
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

### PRODUCING PAIR DATABASE FILE
**halo_mass_filter.py** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| *mass_filter.txt* <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
**reduced_halo_pair_finder.cpp** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| *reduced_halo_pairs.txt* <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
**halo_get_pair_data.py** <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| *reduced_halo_pairs_full_data.txt* <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
**halo_pair_check.py** *(optional, this step is to verify that the pairs are correct.)* <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| *reduced_halo_pairs_full_data.txt* <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| <br />
