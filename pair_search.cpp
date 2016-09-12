#include "pair_search_functions.h"

using namespace std;

int main(){

  halo_t halo_a, halo_b;
  cart_t sys_midpoint, obs, obs_sep, obs_vel, rel_v, rel_p;
  sph_t sph;
  string halo_a_str, halo_b_str, pair_attr_str, pair_attr_working, temp, temp_working[N_PAIR_ATTR], pair_id_str;
  int i,j, pair_count=0, pair_id;

  char sphere[ANGULAR_RES][ANGULAR_RES*2];

  bounds_t b_sep, b_vel, b_mass_a, b_mass_b;


  b_sep = get_range_input("separation");
  b_vel = get_range_input("velocity");
  b_mass_a = get_range_input("mass_a");
  b_mass_b = get_range_input("mass_b");

  cout << "------------------------------------------" << endl;

  ifstream f_halo_data;
  f_halo_data.open("/home/jsnguyen/Desktop/DSS_Data/reduced_halo_pairs_full_data.txt");

  if (f_halo_data.is_open()){

    for(i = 0; i < N_HEADER_LINES; i++){
      getline(f_halo_data,temp); //skip header lines
    }

    while(1){

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
      halo_a = halo_t_parser(halo_a_str);
      halo_b = halo_t_parser(halo_b_str);

      sys_midpoint = midpoint(halo_a,halo_b);

      sph.theta = 0;
      sph.phi = 0;


      for(i = 0; i < ANGULAR_RES; i++){ //theta
        for(j = 0; j < ANGULAR_RES*2; j++){ //phi
          obs = sph_to_cart(sph);

          rel_v = get_rel_v(halo_a,halo_b);
          rel_p = get_rel_p(halo_a,halo_b);

          obs_sep = sep_projection(rel_p,obs);
          obs_vel = projection(rel_v,obs);

          sph.phi = (2*PI)/ANGULAR_RES * j;

          if( ( ((halo_a.mvir > b_mass_a.low) && (halo_a.mvir <  b_mass_a.up))    &&
                ((halo_b.mvir > b_mass_b.low) && (halo_b.mvir <  b_mass_b.up)) )  ||
              ( ((halo_a.mvir > b_mass_b.low) && (halo_a.mvir <  b_mass_b.up))    &&
                ((halo_b.mvir > b_mass_a.low) && (halo_b.mvir <  b_mass_a.up)) )  ){

            if(magnitude(obs_vel) > b_vel.low && magnitude(obs_vel) < b_vel.up){
              if(magnitude(obs_sep) > b_sep.low && magnitude(obs_sep) < b_sep.up){

                sphere[i][j] = '_';

              }
            }
          }

        }

        sph.theta = PI/ANGULAR_RES * i;

      }

      for( i = 0; i<ANGULAR_RES; i++){
        for( j = 0; j<ANGULAR_RES*2; j++){

          if(sphere[i][j] != 'o'){
            pair_count++;

            cout << pair_id << endl;
            cout << halo_a.pos.x << " " << halo_a.pos.y << " " << halo_a.pos.z << " " << halo_a.vel.x << " " << halo_a.vel.y << " " << halo_a.vel.z << " " << halo_a.mvir << " " << halo_a.r200b  << endl;
            cout << halo_b.pos.x << " " << halo_b.pos.y << " " << halo_b.pos.z << " " << halo_b.vel.x << " " << halo_b.vel.y << " " << halo_b.vel.z << " " << halo_b.mvir << " " << halo_b.r200b  << endl;

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
