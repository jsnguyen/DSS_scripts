#include "pair_search_functions.h"

using namespace std;

int main(){

  halo_t halo_a, halo_b;
  cart_t obs, obs_sep, obs_vel, rel_v, rel_p;
  sph_t sph;
  bounds_t b_sep, b_vel, b_mass_a, b_mass_b;

  string halo_a_str, halo_b_str, pair_id_str, temp;
  int i,j, pair_count=0, pair_id;

/*
 * sphere[theta][phi]
 * Theta has a range of 0 to pi.
 * Phi has a range of 0 to 2pi.
 * Since phi covers twice the interval, we do ANGULAR_RES*2.
 * This array stores all the viewing angles that fulfil the search criterion.
 * Printing this array is the same as taking the surface of a sphere and flattening and stretching it into a squre.
 * Angular resolution determines the number of "pixels" on this sphere.
 */
  char sphere[ANGULAR_RES][ANGULAR_RES*2];



  b_sep = get_range_input("separation");
  b_vel = get_range_input("velocity");
  b_mass_a = get_range_input("mass_a");
  b_mass_b = get_range_input("mass_b");

  cout << "------------------------------------------" << endl;

  ifstream f_halo_data;
  f_halo_data.open("/home/jsnguyen/Desktop/DSS_Data/reduced_halo_pairs_full_data.txt");

  if (f_halo_data.is_open()){

    // Skip header lines
    for(i = 0; i < N_HEADER_LINES; i++){
      getline(f_halo_data,temp);
    }

    while(1){

      // Reset the sphere array
      for( i = 0; i<ANGULAR_RES; i++){
        for( j = 0; j<ANGULAR_RES*2; j++){
          sphere[i][j] = 'o';
        }
      }

      getline(f_halo_data,pair_id_str); //halo pair id
      getline(f_halo_data,halo_a_str); // halo a data
      getline(f_halo_data,halo_b_str); // halo b data

      if(f_halo_data.eof()){
        break;
      }

      pair_id = atoi(pair_id_str.c_str());
      halo_a = halo_t_parser(halo_a_str); // Parses halo_a data into halo_t retainer
      halo_b = halo_t_parser(halo_b_str); // Parses halo_b data into halo_t retainer

      for(i = 0; i < ANGULAR_RES; i++){ //theta
        for(j = 0; j < ANGULAR_RES*2; j++){ //phi, must be ANGULAR_RES*2 to make sure both steps in angle are the same.

          obs = sph_to_cart(sph); // Convert spherical coordinates to cartesian

          rel_v = get_rel_v(halo_a,halo_b); // Calculate relative velocity
          rel_p = get_rel_p(halo_a,halo_b); // Calculate relative position

          obs_vel = projection(rel_v,obs); // Calculate observed velocity
          obs_sep = sep_projection(rel_p,obs); // Calculate observed separation

          sph.phi = (2*PI)/ANGULAR_RES * j; // Range for phi is 2pi

          // Mass check
          if( ( ((halo_a.mvir > b_mass_a.low) && (halo_a.mvir <  b_mass_a.up))    &&
                ((halo_b.mvir > b_mass_b.low) && (halo_b.mvir <  b_mass_b.up)) )  ||
              ( ((halo_a.mvir > b_mass_b.low) && (halo_a.mvir <  b_mass_b.up))    &&
                ((halo_b.mvir > b_mass_a.low) && (halo_b.mvir <  b_mass_a.up)) )  ){

            // Observed Velocity check
            if(magnitude(obs_vel) > b_vel.low && magnitude(obs_vel) < b_vel.up){

              // Observed Separation check
              if(magnitude(obs_sep) > b_sep.low && magnitude(obs_sep) < b_sep.up){
                sphere[i][j] = '_'; // Mark where on the sphere the criterion is fulfilled
              }
            }
          }
        }
        sph.theta = PI/ANGULAR_RES * i; // Range for theta is pi
      }

      for( i = 0; i<ANGULAR_RES; i++){
        for( j = 0; j<ANGULAR_RES*2; j++){

          // Check if there is at least one angle for which the pair can be an analog
          if(sphere[i][j] != 'o'){
            pair_count++;

            cout << pair_id << endl;
            print_halo(halo_a);
            print_halo(halo_b);
            cout << "------------------------------------------" << endl;

            i = ANGULAR_RES;
            j = ANGULAR_RES*2;
            /*
            for( i = 0; i<ANGULAR_RES; i++){
              for( j = 0; j<ANGULAR_RES*2; j++){
                cout << sphere[i][j];
              }
              cout << endl;
            }
            */
          }
        }
      }
    }
  }

  else {
    cout << "Error: Cannot open file." << endl;
  }

  cout << "Total Pairs: " << pair_count << endl << endl;

  cout << "(id)                  pair_id" << endl;
  cout << "(halo a attributes)   ax ay az avx avy avz amvir ar200b" << endl;
  cout << "(halo b attributes)   bx by bz bvx bvy bvz bmvir br200b" << endl;

  f_halo_data.close();
  return 0;
}
