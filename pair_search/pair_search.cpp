#include "pair_search_functions.h"

using namespace std;

int main(int argc, char *argv[]){

  bool VERBOSE = false;

  if ( argc !=1 && string(argv[1]) == "-v" ){
    VERBOSE = true;
  }

  vector<pair_t> pair(N_PAIRS); // This is our giant vector where we store all the halo pairs in the heap

  cartesianCoord obs, obs_sep, obs_vel, rel_v, rel_p;
  sphericalCoord sph;
  bounds_t b_sep, b_vel, b_mass_a, b_mass_b;
  double area_counter=0;

  string halo_a_str, halo_b_str, pair_id_str, temp;

  int i,j,k,l, pair_count=0;

  bool valid_pair=false;

  string save_directory = "/home/jsnguyen/DSS_Data/";

/*
 * Theta has a range of 0 to pi.
 * Phi has a range of 0 to 2pi.
 * Since phi covers twice the interval, we do ANGULAR_RES*2.
 * This vector stores all the viewing angles that fulfil the search criterion.
 * Angular resolution determines the number of "pixels" on this sphere.
 */

  vector <sphericalCoord> good_angles;

  b_sep.get_range_input("separation"); // Units: Mpc
  b_vel.get_range_input("velocity"); // Units: km/s
  b_mass_a.get_range_input("mass_a"); // Units: Msun (Solar Masses)
  b_mass_b.get_range_input("mass_b"); // Units: Msun (Solar Masses)

  cout << "------------------------------------------" << endl;

  ifstream f_halo_data;
  f_halo_data.open(save_directory+"reduced_halo_pairs_full_data.txt");

  if (f_halo_data.is_open()){

    // Skip header
    for(i = 0; i < N_HEADER_LINES; i++){
      getline(f_halo_data,temp);
    }

    // This loop sticks everything into a giant vector of type pair
    for(i=0; i< N_PAIRS; i++){

      getline(f_halo_data,pair_id_str); //halo pair id
      getline(f_halo_data,halo_a_str); // halo a data
      getline(f_halo_data,halo_b_str); // halo b data

      pair[i].id = atoi(pair_id_str.c_str());
      pair[i].a.halo_t_parser(halo_a_str); // Parses pair.a data into halo_t retainer
      pair[i].b.halo_t_parser(halo_b_str); // Parses pair.b data into halo_t retainer

      if (i%10000 == 0){
        cout << "Processing... " <<  double(i)/double(N_PAIRS)*100 << "%\r";
        cout.flush();
      }
    }
    cout << "Processing... 100% Complete."<< endl;
  }

  else {
    cout << "Error: Cannot open file." << endl;
    return 1;
  }

  cout << "Searching for matching pairs..." << " 0%\r";
  cout.flush();

  ofstream pair_out; //pair output
  pair_out.open(save_directory+"pair_output.txt");

  ofstream angle_out; //angle output
  angle_out.open(save_directory+"angle_out.txt");

  // Iterates over all the pairs
  for(k=0; k < N_PAIRS; k++){

   // Print progress in percentage
    if (k%1000 == 0){
      cout << "Searching for matching pairs... " << double(k)/double(N_PAIRS)*100 << "%\r";
      cout.flush();
    }

    // Mass check
    if( ( ((pair[k].a.mvir > b_mass_a.low) && (pair[k].a.mvir <  b_mass_a.up))    &&
          ((pair[k].b.mvir > b_mass_b.low) && (pair[k].b.mvir <  b_mass_b.up)) )  ||
        ( ((pair[k].a.mvir > b_mass_b.low) && (pair[k].a.mvir <  b_mass_b.up))    &&
          ((pair[k].b.mvir > b_mass_a.low) && (pair[k].b.mvir <  b_mass_a.up)) )  ){


      // Integrating over the sphere
      // The difference between steps in theta are the same as steps in phi
      for(i = 0; i < ANGULAR_RES; i++){ //theta
        sph.set_theta(double(PI)/double(ANGULAR_RES) * double(i)); // Range for theta is 0 to pi
        for(j = 0; j < ANGULAR_RES*2; j++){ //phi, must be ANGULAR_RES*2 because we are integrating over 2pi
          sph.set_phi(double(PI*2.0)/double(ANGULAR_RES*2.0) * double(j)); // Range for phi is 0 to 2pi

          obs =  sph.sph_to_cart(); // Convert spherical coordinates to cartesian

          rel_p = pair[k].a.pos-pair[k].b.pos; // Calculate relative position
          rel_v = pair[k].a.vel-pair[k].b.vel; // Calculate relative velocity

          obs_vel = rel_v.projection(obs); // Calculate observed velocity
          obs_sep = rel_p.sep_projection(obs); // Calculate observed separation

          // Observed Velocity check
          if(obs_vel.magnitude() > b_vel.low && obs_vel.magnitude() < b_vel.up){
            // Observed Separation check
            if(obs_sep.magnitude() > b_sep.low && obs_sep.magnitude() < b_sep.up){
              valid_pair = true;
              good_angles.push_back(sph);
              area_counter += ( double(PI)/double(ANGULAR_RES) ) * ( cos( sph.get_theta() - ( double(PI)/double(ANGULAR_RES) ) ) - cos(sph.get_theta()) );

            }
          }
        }
      }
    }

    else {
      continue; // checks if mass criterion is satisfied, if not, skip calculating projection stuff
    }

    pair[k].prob = area_counter / double(4*PI); //area that works divided by the surface area of the sphere
    area_counter = 0;

    // Check if there is at least one angle for which the pair can be an analog
    if(valid_pair==true){
      valid_pair = false; //Reset valid_pair flag
      pair_count++;

    if (VERBOSE == true) {
      //Print pair attributes
      cout << pair[k].id << endl;
      pair[k].a.print_halo();
      pair[k].b.print_halo();
      cout << "probability: " << pair[k].prob << endl;
      cout << "------------------------------------------" << endl;
    }

      //Save pair attributes
      pair_out << pair[k].id << endl;
      pair[k].a.save_halo(pair_out);
      pair[k].b.save_halo(pair_out);
      pair_out << pair[k].prob << endl; //store data in output file

      //Save good pair angles to a file
      angle_out << "#" << endl; //Delimiter
      for( l = 0; l< int(good_angles.size()); l++){
        angle_out << good_angles[l].get_theta() << " " << good_angles[l].get_phi() << endl;
      }
      //Reset good angles vector
      good_angles.clear();

    }
  }

  pair_out.close();
  angle_out.close();

  cout << "100%\nComplete."<< endl;

//##################################################################

  cout << endl << "Total Pairs: " << pair_count << endl << endl;
  cout << "(id)                  pair_id" << endl;
  cout << "(halo a attributes)   aindex ax ay az avx avy avz amvir ar200b" << endl;
  cout << "(halo b attributes)   bindex bx by bz bvx bvy bvz bmvir br200b" << endl;

  return 0;
}
