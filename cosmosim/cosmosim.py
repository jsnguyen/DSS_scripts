import csv
import math
from collections import defaultdict

class vector(object):
    def __init__(self,x=None,y=None,z=None):
        if x is not None and y is not None and z is not None:
            self._x = float(x)
            self._y = float(y)
            self._z = float(z)
        else:
            self._x = x
            self._y = y
            self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def __add__(self,v):
        new = vector()
        new._x = self._x+v._x
        new._y = self._y+v._y
        new._z = self._z+v._z
        return new

    def __sub__(self,v):
        new = vector()
        new._x = self._x-v._x
        new._y = self._y-v._y
        new._z = self._z-v._z
        return new

    def __str__(self):
        return '('+str(self._x)+','+str(self._y)+','+str(self._z)+')'

    def __mul__(self,v):
        if isinstance(v,vector):
            return self._x*v._x + self._y*v._y + self._z*v._z
        else:
            new = vector()
            new._x = self._x*v
            new._y = self._y*v
            new._z = self._z*v
            return new

    def magnitude(self):
        return math.sqrt((self._x*self._x)+(self._y*self._y)+(self._z*self._z))

    def angle(self,v):
        return math.degrees(math.acos((self*v) / (self.magnitude()*v.magnitude())))

    def rotate(self,axis,angle):
        new_p = vector()

        if axis=='y':
            new_p._x = self._x*math.cos(math.radians(angle)) + self._z*math.sin(math.radians(angle))
            new_p._y = self._y
            new_p._z = -self._x*math.sin(math.radians(angle)) + self._z*math.cos(math.radians(angle))

        return new_p

class halo(object):
    def __init__(self,params):
        self.rockstar_id = params[0]
        self.pos = vector(params[1],params[2],params[3])
        self.vel = vector(params[4],params[5],params[6])
        self.ang_mom = vector(params[7],params[8],params[9])
        self.ellipsoid = vector(params[10],params[11],params[12])
        self.m_vir = params[13]
        self.r_vir = params[14]
        self.spin = params[15]
        self.t_u = params[16]
        self.snapnum = params[17]

    def __str__(self):
        return ("rockstar_id: "+str(self.rockstar_id)+'\n'+
        "pos: "+str(self.pos)+'\n'+
        "vel: "+str(self.vel)+'\n'+
        "ang_mom: "+str(self.ang_mom)+'\n'+
        "ellipsoid: "+str(self.ellipsoid)+'\n'+
        "m_vir: "+str(self.m_vir)+'\n'+
        "r_vir: "+str(self.r_vir)+'\n'+
        "spin: "+str(self.spin)+'\n'+
        "t_u: "+str(self.t_u)+'\n'+
        "snapnum: "+str(self.snapnum))

if __name__ == '__main__':
    filename = '/home/jsnguyen/DSS_scripts/cosmosim/name_list.txt'
    names=[]
    with open(filename, 'r') as f:
        for line in f:
            names.append('/home/jsnguyen/DSS_scripts/cosmosim/'+line.strip()+'.csv')
            break

    systems=[]
    progenitors=[]
    for fn in names:
        print 'loading:',fn
        with open(fn, 'r') as f:
            f_csv = csv.reader(f, delimiter=',')
            f_csv.next()
            for line in f_csv:
                temp_halo = halo(line[1:])
                progenitors.append(temp_halo)

    snaps=defaultdict(list)
    for i in range(len(progenitors)):
        if progenitors[i].snapnum >= 100:
            snaps[progenitors[i].snapnum].append(progenitors[i])

    mass={}
    for key in snaps.keys():
        for i in range(len(snaps[key])):
            mass['rockstar_id'] = snaps[key][i].mass
