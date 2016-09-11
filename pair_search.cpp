#include "pair_search_functions.h"

using namespace std;

int main(){

  halo_t halo_a, halo_b;
  cart_t sys_midpoint, obs, obs_sep, obs_vel, rel_v, rel_p;
  sph_t sph;
  double in_p_sep = 0.5, in_p_vel = 2000, in_mass_lower_a = 0, in_mass_upper_a = 10e14, in_mass_lower_b = 0, in_mass_upper_b = 10e14; //in in_p_sep in units of Mpc
  double in_p_sep_range, in_p_vel_range;
  double sep, mag_rel_v, scal_proj; //sep units Mpc, mag_rel_v units km/s
  string halo_a_str, halo_b_str, pair_attr_str, pair_attr_working, temp, temp_working[N_PAIR_ATTR], pair_id_str, sep_str, mag_rel_v_str, scal_proj_str;
  int i,j, pair_id;

  cout << "Input projected separation (Mpc): ";
  cin >> in_p_sep;
  cout << "Input projected separation range (Mpc): ";
  cin >> in_p_sep_range;
  cout << "Input projected velocity (km/s): ";
  cin >> in_p_vel;
  cout << "Input projected velocity range (km/s): ";
  cin >> in_p_vel_range;



  cout << "Input lower mass bound for halo a (Msun): ";
  cin >> in_mass_lower_a;
  cout << "Input upper mass bound for halo a (Msun): ";
  cin >> in_mass_upper_a;

  cout << "Input lower mass bound for halo b (Msun): ";
  cin >> in_mass_lower_b;
  cout << "Input upper mass bound for halo b (Msun): ";
  cin >> in_mass_upper_b;

  cout << "------------------------------------------" << endl;


  ifstream f_halo_data;
  f_halo_data.open("/home/jsnguyen/Desktop/DSS_Data/reduced_halo_pairs_full_data.txt");

  if (f_halo_data.is_open()){

    for(i = 0; i < N_HEADER_LINES; i++){
      getline(f_halo_data,temp); //skip header lines
    }
    while(1){

      getline(f_halo_data,pair_id_str); //halo pair id
      getline(f_halo_data,halo_a_str); // halo a data
      getline(f_halo_data,halo_b_str); // halo b data
      getline(f_halo_data,pair_attr_str); //pair attributes

      stringstream pair_attr_stream(temp);
      for(i = 0; i < N_PAIR_ATTR; i++){
        pair_attr_stream >> pair_attr_working[i];
      }

      sep_str = pair_attr_working[0];
      mag_rel_v_str = pair_attr_working[1];
      scal_proj_str = pair_attr_working[2];

      if(f_halo_data.eof()){
        break;
      }

      pair_id = atoi(pair_id_str.c_str());
      halo_a = halo_t_parser(halo_a_str);
      halo_b = halo_t_parser(halo_b_str);
      sep = atof(sep_str.c_str())/HUBBLE_CONST; //convert Mpc/h to Mpc
      mag_rel_v = atof(mag_rel_v_str.c_str());
      scal_proj = atof(scal_proj_str.c_str());

      sys_midpoint = midpoint(halo_a,halo_b);

      for(i = 0; i < ANGULAR_RES; i++){
        for(j = 0; j < ANGULAR_RES; j++){
          sph.theta = 0;
          sph.phi = 0;

          obs = sph_to_cart(sph);

          rel_v = get_rel_v(halo_a,halo_b);
          rel_p = get_rel_p(halo_a,halo_b);

          obs_sep = sep_projection(rel_p,obs);
          obs_vel = projection(rel_v,obs);

          sph.phi = PI/ANGULAR_RES * j;

          //IF STATEMENTS TO CHECK FOR ANALOGS HERE

        }

        sph.theta = PI/ANGULAR_RES * i;

      }
    }
  }

  else {
    cout << "Error: Cannot open file." << endl;
  }

  cout << "Total Pairs: " << i << endl << endl;

  cout << "(id)                  pair_id" << endl;
  //cout << "(halo a attributes)   ax ay az avx avy avz amvir ar200b" << endl;
  //cout << "(halo b attributes)   bx by bz bvx bvy bvz bmvir br200b" << endl;
  cout << "(pair attributes)     separation mag_rel_v scalar_proj" << endl;

  f_halo_data.close();
  return 0;
}
