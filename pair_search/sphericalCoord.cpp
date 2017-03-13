#include "sphericalCoord.h"

//by default a unit vector pointing in positive-z axis
sphericalCoord::sphericalCoord():
rho(1), theta(0), phi(0)
{
}

sphericalCoord::sphericalCoord(double a, double b, double c):
rho(a), theta(b), phi(c)
{
}

cartesianCoord sphericalCoord::sph_to_cart() const{

  double x = rho*sin(theta)*cos(phi);
  double y = rho*sin(theta)*sin(phi);
  double z = rho*cos(theta);

  cartesianCoord cart(x,y,z);
  return cart;
}

void sphericalCoord::set(double a, double b, double c){
  rho = a;
  theta = b;
  phi = c;
  return;
}

void sphericalCoord::set_rho(double new_rho){
  rho = new_rho;
  return;
}
void sphericalCoord::set_theta(double new_theta){
  theta = new_theta;
  return;
}
void sphericalCoord::set_phi(double new_phi){
  phi = new_phi;
  return;
}

double sphericalCoord::get_rho(){
  return rho;
}

double sphericalCoord::get_theta(){
  return theta;
}

double sphericalCoord::get_phi(){
  return phi;
}


sphericalCoord sphericalCoord::operator+ (const sphericalCoord b){
  return sphericalCoord(rho+b.rho,theta+b.theta,phi+b.phi);
}

sphericalCoord sphericalCoord::operator- (const sphericalCoord b){
  return sphericalCoord(rho-b.rho,theta-b.theta,phi-b.phi);
}

std::ostream &operator<< (std::ostream &out, const sphericalCoord &a){
    out << '(' <<a.rho << ',' << a.theta << ',' << a.phi<< ')';
    return out;
}
