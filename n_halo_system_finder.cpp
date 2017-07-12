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
#define MAX_SEPARATION 5 //Units: Mpc
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
  string to_write;
  bool halo_found=false;

  vector<coord> data(N_TOTAL_MASS_HALOS); //this array is HUGE, requires ~1.3 Gb of RAM

  string save_directory = "/home/jsnguyen/DSS_data/";
  string mass_fn = "mass_filter_1e14.txt";
  string reduced_pair_fn = "reduced_halo_pairs_1e14_5Mpc_c.txt";

  ifstream f_mass_filter;
  ofstream f_pairs;

  f_mass_filter.open((save_directory+mass_fn).c_str());

  if (f_mass_filter.is_open()){

    for (i=0; i<N_TOTAL_MASS_HALOS; i++){
      getline(f_mass_filter,working_coord_str);

      while (working_coord_str.at(0) == '#'){
        getline(f_mass_filter,working_coord_str);
        cout << "skipped a line" << endl;
      }

      working_coord = coord_parser(working_coord_str);
      data[i] = working_coord;

      if (i%100000 == 0){
        cout << "Processing... " <<  double(i)/double(N_TOTAL_MASS_HALOS)*100 << '%' << endl;
      }
    }

    cout << "Processing... 100%\nComplete."<< endl;
    f_mass_filter.close();
  }

  f_pairs.open((save_directory+reduced_pair_fn).c_str());
  f_pairs << "# halo_a halo_b" << endl; //header

  for( i=0; i < int(data.size())-1; i++ ){
    to_write = "#### SYSTEM START ####\n";
    to_write += to_string(data[i].index)+'\n';

    for(j=i+1; j < int(data.size()); j++){
      dist = distance(data[i],data[j]);

      if (dist < MAX_SEPARATION){
        cout << "pair found: " << data[i].index << " " << data[j].index << endl;
        cout << "separation: " << dist << endl;
        halo_found = true;
        to_write += to_string(data[j].index)+'\n';
        data.erase(data.begin()+j);
        j--;
      }

      if(abs(data[i].index-data[j].index) > 10000){
        j = int(data.size())-i; // 99% likelyhood we will find pairs within 10000 indicies
      }
    }

    to_write += "#### SYSTEM END ####\n";

    if(halo_found){
      f_pairs << to_write;
    }

    halo_found = false;
  }
  f_pairs.close();

  return 0;
}
