#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>

#define N_HEADER_LINES 4
#define HUBBLE_CONST 0.7
#define N_HALO_ATTR 9 //number of attributes for a single halo
#define N_PAIR_ATTR 3 //number of pair (shared) attributes

using namespace std;

struct halo_t{
  long long index;
  double x;
  double y;
  double z;
  double vx;
  double vy;
  double vz;
  double mvir;
  double r200b;
};

halo_t halo_t_parser(string str_input){
  int i;
  halo_t halo;
  string str_working[9];

  stringstream str_stream(str_input);

  if (str_stream.good()){
    for( i=0; i<N_HALO_ATTR; i++){
      str_stream >> str_working[i];
    }
  }

  halo.index = stoll(str_working[0].c_str());
  halo.x = atof(str_working[1].c_str());
  halo.y = atof(str_working[2].c_str());
  halo.z = atof(str_working[3].c_str());
  halo.vx = atof(str_working[4].c_str());
  halo.vy = atof(str_working[5].c_str());
  halo.vz = atof(str_working[6].c_str());
  halo.mvir = atof(str_working[7].c_str())/HUBBLE_CONST;
  halo.r200b = atof(str_working[8].c_str());

  return halo;
}

int main(){

  halo_t halo_a, halo_b;
  double in_p_sep = 0.5, in_v_los = 2000, in_mass_lower_a = 0, in_mass_upper_a = 10e14, in_mass_lower_b = 0, in_mass_upper_b = 10e14; //in in_p_sep in units of Mpc
  double in_p_sep_range, in_v_los_range, alpha_lower_d, alpha_upper_d, alpha_lower_v, alpha_upper_v;
  double sep, mag_rel_v, scal_proj; //sep units Mpc, mag_rel_v units km/s
  string halo_a_str, halo_b_str, temp, temp_working[N_PAIR_ATTR], pair_id_str, sep_str, mag_rel_v_str, scal_proj_str;
  int i,j, pair_id;

  cout << "Input projected separation (Mpc): ";
  cin >> in_p_sep;
  cout << "Input projected separation range (Mpc): ";
  cin >> in_p_sep_range;
  cout << "Input projected velocity (km/s): ";
  cin >> in_v_los;
  cout << "Input projected velocity range (km/s): ";
  cin >> in_v_los_range;



  cout << "Input lower mass bound for halo a (Msun): ";
  cin >> in_mass_lower_a;
  cout << "Input upper mass bound for halo a (Msun): ";
  cin >> in_mass_upper_a;

  cout << "Input lower mass bound for halo b (Msun): ";
  cin >> in_mass_lower_b;
  cout << "Input upper mass bound for halo b (Msun): ";
  cin >> in_mass_upper_b;


  ifstream f_halo_data;
  f_halo_data.open("../reduced_halo_pairs_full_data.txt");

  if (f_halo_data.is_open()){

    for( j=0; j<N_HEADER_LINES; j++ ){
      getline(f_halo_data,temp); //skip header lines
    }

    i=0;
    while(1){

      getline(f_halo_data,pair_id_str); //halo pair id
      getline(f_halo_data,halo_a_str); // halo a data
      getline(f_halo_data,halo_b_str); //halo b data
      getline(f_halo_data,temp); //pair attributes

      stringstream temp_stream(temp);
      for( j = 0; j < N_PAIR_ATTR; j++){
        temp_stream >> temp_working[j];
      }

      sep_str = temp_working[0];
      mag_rel_v_str = temp_working[1];
      scal_proj_str = temp_working[2];

      if(f_halo_data.eof()){
        break;
      }

      pair_id = atoi(pair_id_str.c_str());
      halo_a = halo_t_parser(halo_a_str);
      halo_b = halo_t_parser(halo_b_str);
      sep = atof(sep_str.c_str())/HUBBLE_CONST; //convert Mpc/h to Mpc
      mag_rel_v = atof(mag_rel_v_str.c_str());
      scal_proj = atof(scal_proj_str.c_str());

      alpha_lower_d = acos((in_p_sep+in_p_sep_range)/sep); //smaller angle
      alpha_upper_d =  acos((in_p_sep-in_p_sep_range)/sep); //larger angle

      //note that the larger the numerator the smaller the angle for cosine but larger the angle for sine.

      alpha_lower_v = asin((in_v_los-in_v_los_range)/mag_rel_v); //smaller angle
      alpha_upper_v = asin((in_v_los+in_v_los_range)/mag_rel_v); // larger angle

      if (sep > in_p_sep){
        if (mag_rel_v > in_v_los){
          //check if halo_a satisfies the first criterion, check if halo_b satisfies the second criterion
          //if they dont satisfy the first and second criterion, check the inverse
          //check if halo_a satisfies the second criterion, check if halo_b satisfies the first criterion
          if ( ((in_mass_lower_a < halo_a.mvir && in_mass_upper_a > halo_a.mvir) && (in_mass_lower_b < halo_b.mvir && in_mass_upper_b > halo_b.mvir)) || ((in_mass_lower_b < halo_a.mvir && in_mass_upper_b > halo_a.mvir) && (in_mass_lower_a < halo_b.mvir && in_mass_upper_a > halo_b.mvir)) ){
              //check for valid alpha range
              if(alpha_lower_d < alpha_lower_v && alpha_upper_d > alpha_lower_v && alpha_lower_d < alpha_upper_v && alpha_upper_d > alpha_upper_v){
                i++; // start at 1
                cout << pair_id << endl;
                cout << halo_a.x << " " << halo_a.y << " " << halo_a.z << " " << halo_a.vx << " " << halo_a.vy << " " << halo_a.vz << " " << halo_a.mvir << " " << halo_a.r200b  << endl;
                cout << halo_b.x << " " << halo_b.y << " " << halo_b.z << " " << halo_b.vx << " " << halo_b.vy << " " << halo_b.vz << " " << halo_b.mvir << " " << halo_b.r200b  << endl;
                cout << sep << " " << mag_rel_v << " " << scal_proj << endl;

                if(scal_proj > 0){
                  cout << "Halos are returning." << endl;
                }
                else{
                  cout << "Halos are outbound." << endl;
                }

                //cout << "alpha_lower_d: " << alpha_lower_d << endl;
                //cout << "alpha_upper_d: " << alpha_upper_d << endl;
                //cout << "alpha_lower_v: " << alpha_lower_v << endl;
                //cout << "alpha_upper_v: " << alpha_upper_v << endl;
                cout << "------------------------------------------" << endl;
              }
            }

          }
        }

      }
    }

  else {
    cout << "Error: Cannot open file." << endl;
  }

  cout << "Total Pairs: " << i << endl << endl;

  cout << "(id)                  pair_id" << endl;
  cout << "(halo a attributes)   ax ay az avx avy avz amvir ar200b" << endl;
  cout << "(halo b attributes)   bx by bz bvx bvy bvz bmvir br200b" << endl;
  cout << "(pair attributes)     separation mag_rel_v scalar_proj" << endl;

  f_halo_data.close();
  return 0;
}
