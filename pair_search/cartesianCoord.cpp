#include "cartesianCoord.h"

cartesianCoord::cartesianCoord(): x(0), y(0), z(0)
{
}

cartesianCoord::cartesianCoord(double a, double b, double c): x(a), y(b), z(c)
{
}

double cartesianCoord::magnitude() const{
  double mag;
  mag = sqrt(x*x + y*y + z*z);
  return mag;
}

cartesianCoord cartesianCoord::operator+ (const cartesianCoord b){
  return cartesianCoord(x+b.x, y+b.y, z+b.z);
}

cartesianCoord cartesianCoord::operator- (const cartesianCoord b){
  return cartesianCoord(x-b.x, y-b.y, z-b.z);
}

double cartesianCoord::dotProd(cartesianCoord b) const{
  return  x*b.x + y*b.y + z*b.z;
}

cartesianCoord cartesianCoord::operator* (const double b){
  return cartesianCoord(x*b, y*b, z*b);
}

void cartesianCoord::set_x(double new_x){
  x = new_x;
  return;
}
void cartesianCoord::set_y(double new_y){
 y = new_y;
  return;
}
void cartesianCoord::set_z(double new_z){
  z = new_z;
  return;
}

double cartesianCoord::get_x(){
  return x;
}

double cartesianCoord::get_y(){
  return y;
}
double cartesianCoord::get_z(){
  return z;
}

std::ostream &operator<< (std::ostream &out, const cartesianCoord &a){
    out << '(' <<a.x << ',' << a.y << ',' << a.z<< ')';
    return out;
}

cartesianCoord cartesianCoord::projection(cartesianCoord b) const{
  // projection of a onto b
  cartesianCoord proj;
  const cartesianCoord a(x,y,z);

  double scalar = a.dotProd(b) / ( b.magnitude()*b.magnitude() );
  proj =  b*scalar;

  return proj;
}

cartesianCoord cartesianCoord::sep_projection(cartesianCoord b) const{
  cartesianCoord p_sep, norm_comp;
  cartesianCoord a(x,y,z);

  norm_comp = a.projection(b);
  p_sep = a-norm_comp;

  return p_sep;
}

sphericalCoord cartesianCoord::cart_to_sph() const{

  const cartesianCoord a(x,y,z);

  double rho = a.magnitude();
  double theta = acos(z/rho);
  double phi = atan2(y,x);

  if (rho < 0){
    rho += 2.0*PI;
  }
  if (theta < 0){
    theta += 2.0*PI;
  }
  if (phi < 0){
    phi += 2.0*PI;
  }

  sphericalCoord sph(rho,theta,phi);
  return sph;
}
