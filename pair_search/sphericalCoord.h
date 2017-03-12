#ifndef SPHERICALCOORD_H
#define SPHERICALCOORD_H

#include "cartesianCoord.h"
#include <math.h>
#include <iostream>

#define PI 3.1459

class cartesianCoord;

class sphericalCoord{
  public:
    sphericalCoord();
    sphericalCoord(double, double, double);
    cartesianCoord sph_to_cart() const;

    void set_rho(double);
    void set_theta(double);
    void set_phi(double);

    double get_rho();
    double get_theta();
    double get_phi();

    sphericalCoord operator+ (const sphericalCoord);
    sphericalCoord operator- (const sphericalCoord);

    friend std::ostream &operator<< (std::ostream &out, const sphericalCoord &a);


  private:
    double rho; // radius, this isn't really used
    double theta; // polar angle
    double phi; // azimuthal angle
};



#endif
