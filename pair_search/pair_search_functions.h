#ifndef PAIR_SEARCH_FUNCTIONS_H
#define PAIR_SEARCH_FUNCTIONS_H

#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <ostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <string>

#include "cartesianCoord.h"

#define N_HEADER_LINES 3
#define HUBBLE_CONST 0.688062
#define N_HALO_ATTR 9
#define ANGULAR_RES 100 //Number of iterations to check over, angular resolution
#define N_PAIRS 395902

class cartesianCoord;

struct halo_t{
  cartesianCoord pos, vel;
  long long index;
  double mvir;
  double r200b;

  void halo_t_parser(std::string str_input);
  void print_halo();
  void save_halo(std::ofstream& data);
};

struct bounds_t{
  double up;
  double low;

  void get_range_input(std::string type);
};

struct pair_t{
  int id;
  halo_t a;
  halo_t b;
  double prob; //probability
};

#endif
