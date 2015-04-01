import os

import math

def retrieve(path):  # This function takes one argument, which is a string containing a path to a PDB file.                          
                             #Output is a list of strings consisting of different atom lines                                         
    os.system('grep " SG " ' + path + ' | grep -e "^ATOM" >temp.txt')

    str = open("temp.txt", "r").read()

    SGdata = str.splitlines()

    return SGdata

def replace(SGdata):  # changed line to SGdata

    x = float(SGdata[30:38].strip()) #  changed line to SGdata
    y = float(SGdata[38:46].strip()) #   same as above?
    z = float(SGdata[46:54].strip()) #  Same as above?

    return (x, y, z)

def distance(t1,t2):

    x1 = t1[0]
    y1 = t1[1]
    z1 = t1[2]

    x2 = t2[0]
    y2 = t2[1]
    z2 = t2[2]

    distance  = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))

    return distance  #and/or print out somewhere for checking?

path = "/Users/videau/Desktop/1zkr_copy/molprobity/coordinates/1zkrFH_reg.pdb"

stringList = retrieve(path)


for line1 in stringList:
    print replace(line1)

#  Figure way to iterate through the output from the above using n= and including only the lines higher than the last one used.










#Need to print out the PDBid and the Cys residue # attached to each SG
#need to sift out all SG->SG distances above or below a certain distance
#Flag for alt conformations
