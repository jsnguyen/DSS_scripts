import math

c = 3e5 #km/s
za1 = input("Enter lcl1: ")
za2 = input("Enter ucl1: ")

zb1 = input("Enter lcl2: ")
zb2 = input("Enter ucl2: ")

up = (c * ( abs(za1-zb1) ) ) /( 1+ ((za1+zb1)/2))
down =  (c * ( abs(za2-zb2) ) ) /( 1+ ((za2+zb2)/2))

print "Average:",(up+down) / 2
print "Range:", abs(up-((up+down)/2))
