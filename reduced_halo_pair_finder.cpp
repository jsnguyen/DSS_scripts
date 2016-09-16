/*
 * Finds pairs based only on separation
 *  In: mass_filter.txt
 * Out: reduced_halo_pairs.txt
 */

#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>

#define N_TOTAL_MASS_HALOS 4378742
#define N_HEADER_LINES 3
#define MAX_SEPARATION 1.5 //Units: Mpc
using namespace std;

struct coord{
  long long index;
  double x;
  double y;
  double z;
};

double distance(coord a, coord b){

  double distance;
  distance = sqrt( ((a.x-b.x)*(a.x-b.x)) + ((a.y-b.y)*(a.y-b.y)) + ((a.z-b.z)*(a.z-b.z)) );

  return distance;
}

coord coord_parser(string str_input){
  int i;
  coord coordinate;
  string str_working[4];

  stringstream str_stream(str_input);
  if (str_stream.good()){

    for( i=0; i<4; i++){
      str_stream >> str_working[i];
    }

  }

  coordinate.index = stoll(str_working[0].c_str());
  coordinate.x = atof(str_working[1].c_str());
  coordinate.y = atof(str_working[2].c_str());
  coordinate.z = atof(str_working[3].c_str());

  return coordinate;
}

int main(){

  coord working_coord_a,working_coord_b;
  string coord_a,coord_b;
  int i,j,n_halos;
  double dist;

  string save_directory = "/home/jsnguyen/Desktop/";

  ifstream f_mass_filter;
  ofstream f_pairs;
  f_mass_filter.open(save_directory+"mass_filter.txt");
  f_pairs.open(save_directory+"reduced_halo_pairs.txt");

  n_halos = N_TOTAL_MASS_HALOS;

  if (f_mass_filter.is_open()){

    for( i=0; i<n_halos; i++ ){

      f_mass_filter.clear();
      f_mass_filter.seekg(0, ios::beg);

      for( j=0; j< N_HEADER_LINES+i; j++ ){
        getline(f_mass_filter,coord_a); //skip first 3 header lines
      }

      getline(f_mass_filter,coord_a);
      working_coord_b = coord_parser(coord_a);

      for( j=i+1; j<n_halos; j++ ){
        getline(f_mass_filter,coord_b);
        working_coord_a = coord_parser(coord_b);

        dist = distance(working_coord_a,working_coord_b);
        //cout << dist << endl;

        if(j-i > 10000){
          j = n_halos;
          continue;
        }

        if (dist < MAX_SEPARATION){
          cout << "pair found: " << working_coord_a.index << " " << working_coord_b.index << endl;
          cout << "separation: " << dist << endl;
          f_pairs << working_coord_a.index << " " << working_coord_b.index << endl;
        }

      }

    }

  }

  else {
    cout << "Error: Cannot open file." << endl;
  }

  f_mass_filter.close();
  f_pairs.close();
  return 0;
}
