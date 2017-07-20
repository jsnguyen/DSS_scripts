#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <limits>
#include <vector>

#define N_HEADER_LINES 3
using namespace std;

const int MAX_SEPARATION = 5; //Units: Mpc

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

  vector<coord> data; //this array is HUGE, requires ~1.3 Gb of RAM

  string save_directory = "/home/jsnguyen/DSS_data/";
  string fn_mass_filter = "mass_filter_subhalos_1e+14.txt";
  string fn_n_halo = "n_subhalo_reduced_"+to_string(MAX_SEPARATION)+"Mpc_"+fn_mass_filter;

  ifstream f_mass_filter;
  ofstream f_pairs;

  f_mass_filter.open((save_directory+fn_mass_filter).c_str());

  if (f_mass_filter.is_open()){

    i=0;
    while(getline(f_mass_filter,working_coord_str)){

      while (working_coord_str.at(0) == '#'){
        getline(f_mass_filter,working_coord_str);
        cout << "skipped a header line" << endl;
      }

      i++;
      working_coord = coord_parser(working_coord_str);
      data.push_back(working_coord);

      if (i%1000000 == 0){
        cout << "Processing... " << endl;
      }
    }

    cout << "Total Number of mass filtered halos: "<< data.size() << endl;
    cout << "Processing... 100% complete."<< endl;

    f_mass_filter.close();
  }

  f_pairs.open((save_directory+fn_n_halo).c_str());
  f_pairs << "# halo_a halo_b" << endl; //header

  for( i=0; i < int(data.size())-1; i++ ){
    to_write = "#### SYSTEM START ####\n";
    to_write += to_string(data[i].index)+'\n';

    for(j=i+1; j < int(data.size()); j++){
      if(data[i].x == data[j].x && data[i].y == data[j].y &&  data[i].z == data[j].z && i+1 == j){
        continue;
      }
      dist = distance(data[i],data[j]);

      if (dist < MAX_SEPARATION){
        cout << "nearby halo found: " << data[i].index << " " << data[j].index << endl;
        cout << "separation: " << dist << endl;
        halo_found = true;
        to_write += to_string(data[j].index)+'\n';
        data.erase(data.begin()+j);
        j--; //erase a halo, so we push back one
      }

      if(abs(data[i].index-data[j].index) > 10000){
        j = int(data.size()); // 99% likelyhood we will find pairs within 10000 indicies
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
