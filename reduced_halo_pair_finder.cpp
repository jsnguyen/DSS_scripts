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

  coord working_coord;
  string working_coord_str;
  int i,j;
  double dist;

  vector<coord> data(N_TOTAL_MASS_HALOS); //this array is HUGE, requires ~1.3 Gb of RAM

  string save_directory = "/home/jsnguyen/Desktop/";

  ifstream f_mass_filter;
  ofstream f_pairs;

  f_mass_filter.open(save_directory+"mass_filter.txt");

  if (f_mass_filter.is_open()){

    //skip the header lines
    for( i=0; i<N_HEADER_LINES; i++){
      getline(f_mass_filter,working_coord_str);
    }

    for( i=0; i<N_TOTAL_MASS_HALOS; i++){
      getline(f_mass_filter,working_coord_str);
      working_coord = coord_parser(working_coord_str);
      data[i] = working_coord;

      if (i%100000 == 0){
        cout << "Processing... " <<  double(i)/double(N_TOTAL_MASS_HALOS)*100 << '%' << endl;
      }
    }

    f_mass_filter.close();
    f_pairs.open(save_directory+"reduced_halo_pairs.txt");

    for( i=0; i<N_TOTAL_MASS_HALOS-1; i++ ){
      for(j=i+1; j< N_TOTAL_MASS_HALOS; j++){
        dist = distance(data[i],data[j]);

        if (dist < MAX_SEPARATION){
          cout << "pair found: " << data[i].index << " " << data[j].index << endl;
          cout << "separation: " << dist << endl;
          f_pairs << data[i].index << " " << data[j].index << endl;
        }

        if(abs(data[i].index-data[j].index) > 10000){
          j = N_TOTAL_MASS_HALOS; // 99% likelyhood we will find pairs within 10000 indicies
        }
      }
    }

    f_pairs.close();

  }

  else {
    cout << "Error: Cannot open file." << endl;
  }



  return 0;
}
