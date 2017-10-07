## IMPORTS GO HERE
from math import pi
## END OF IMPORTS 


#### CODE FOR get_area GOES HERE ####
def get_area(radius):
    area= pi * pow(radius, 2)
    return area
#### End OF MARKER


#### CODE FOR output_parameter GOES HERE ####
def output_parameter(radius):
    parameter = 2 * pi * radius
    print "The parameter of the circle with radius", (radius), "is", parameter,
#### End OF MARKER  
