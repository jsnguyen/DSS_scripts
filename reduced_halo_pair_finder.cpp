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
#include <limits>
#include <vector>

#define N_TOTAL_MASS_HALOS 46037858
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

  coord working_coord;
  string working_coord_str;
  int i,j;
  double dist;

  vector<coord> data(N_TOTAL_MASS_HALOS);

  string save_directory = "/home/jsnguyen/Desktop/";

  ifstream f_mass_filter;
  ofstream f_pairs;
  f_mass_filter.open(save_directory+"mass_filter.txt");

  if (f_mass_filter.is_open()){

    for( i=0; i<N_TOTAL_MASS_HALOS; i++){

      getline(f_mass_filter,working_coord_str);
      working_coord = coord_parser(working_coord_str);
      data[i] = working_coord;

      if (i%100000 == 0){
        cout << "Processing " <<  i << " of " << N_TOTAL_MASS_HALOS << endl;
      }

    }

    for( i=0; i<N_TOTAL_MASS_HALOS-1; i++ ){
      for(j=i+1; j< N_TOTAL_MASS_HALOS; j++){

        dist = distance(data[i],data[j]);

      if (dist < MAX_SEPARATION){

          cout << "pair found: " << data[i].index << " " << data[j].index << endl;
          cout << "separation: " << dist << endl;

          f_pairs.open(save_directory+"reduced_halo_pairs.txt",ios_base::app);
          f_pairs << data[i].index << " " << data[j].index << endl;
          f_pairs.close();
        }

        if(abs(data[i].index-data[j].index) > 10000){
          j = N_TOTAL_MASS_HALOS;
        }

      }
    }


  }

  else {
    cout << "Error: Cannot open file." << endl;
  }

  f_mass_filter.close();

  return 0;
}
