#include "pair_search_functions.h"

void halo_t::halo_t_parser(std::string str_input){
  int i;
  std::string str_working[9];

  std::stringstream str_stream(str_input);

  if (str_stream.good()){
    for( i=0; i<N_HALO_ATTR; i++){
      str_stream >> str_working[i];
    }
  }

  index = std::stoll(str_working[0].c_str());
  pos.set_x( atof(str_working[1].c_str()) );
  pos.set_y( atof(str_working[2].c_str()) );
  pos.set_z( atof(str_working[3].c_str()) );
  vel.set_x( atof(str_working[4].c_str()) );
  vel.set_y( atof(str_working[5].c_str()) );
  vel.set_z(atof(str_working[6].c_str()) );
  mvir = atof(str_working[7].c_str());
  r200b = atof(str_working[8].c_str());

  return;
}

void halo_t::print_halo(){
  std::cout << index << " " << pos.get_x() << " " << pos.get_y() << " " << pos.get_z() << " " << vel.get_x() << " " << vel.get_y() << " " << vel.get_z() << " " << mvir << " " << r200b  << std::endl;
  return;
}

void halo_t::save_halo(std::ofstream& data){

  data << index << " " << pos.get_x() << " " << pos.get_y() << " " << pos.get_z() << " " << vel.get_x() << " " << vel.get_y() << " " << vel.get_z() << " " << mvir << " " << r200b  << std::endl;
  return;
}

void bounds_t::get_range_input(std::string type){

  double input, range;

  std::string units;

  if(type=="separation"){
    units = "(Mpc)";
  }

  if(type=="velocity"){
    units = "(km/s)";
  }

  if(type=="mass_a" || type=="mass_b"){
    units = "(Msun)";
  }

  std::cout << "Input projected " << type << " " << units <<": ";
  std::cin >> input;

  std::cout << "Input projected range " << type << " " << units <<": ";
  std::cin >> range;

  up = input + range;
  low = input - range;

  return;
}
