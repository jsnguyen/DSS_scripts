#ifndef CARTESIANCOORD_H
#define CARTESIANCOORD_H

#include "sphericalCoord.h"
#include <math.h>
#include <iostream>

#define PI 3.1459

struct halo_t;
class sphericalCoord;

class cartesianCoord{
  public:
    cartesianCoord();
    cartesianCoord(double,double,double);

    double magnitude() const;

    cartesianCoord operator+ (const cartesianCoord);
    cartesianCoord operator- (const cartesianCoord);
    cartesianCoord operator* (double);

    void set_x(double);
    void set_y(double);
    void set_z(double);

    double get_x();
    double get_y();
    double get_z();

    friend std::ostream &operator<< (std::ostream &out, const cartesianCoord &a);
    double dotProd(cartesianCoord) const;

    cartesianCoord projection(cartesianCoord b) const;
    cartesianCoord sep_projection(cartesianCoord b) const;

    sphericalCoord cart_to_sph() const;

  private:
    double x,y,z;
};

#endif
