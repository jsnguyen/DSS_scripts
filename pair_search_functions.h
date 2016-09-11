#ifndef PAIR_SEARCH_FUNCTIONS_H
#define PAIR_SEARCH_FUNCTIONS_H

#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <string>

#define N_HEADER_LINES 4
#define HUBBLE_CONST 0.7
#define N_HALO_ATTR 9 //number of attributes for a single halo
#define N_PAIR_ATTR 3 //number of pair (shared) attributes
#define N_BOUNDS 4 //number of bounds on alpha
#define ANGULAR_RES 100 //Number of iterations to check over, angular resolution
#define PI 3.14159265359

struct cart_t{
  double x;
  double y;
  double z;
};

struct sph_t{
  double theta; // polar angle
  double phi; // azimuthal angle
  double rho; // radius
};

struct halo_t{
  cart_t pos,vel;
  long long index;
  double mvir;
  double r200b;
};

cart_t midpoint(halo_t halo_a, halo_t halo_b);
double magnitude(cart_t cart);
cart_t projection(cart_t a, cart_t b);
cart_t sep_projection(cart_t a, cart_t b);
cart_t sph_to_cart(sph_t sph);
sph_t cart_to_sph(cart_t cart);
cart_t get_rel_v(halo_t halo_a, halo_t halo_b);
cart_t get_rel_p(halo_t halo_a, halo_t halo_b);
halo_t halo_t_parser(std::string str_input);

#endif
