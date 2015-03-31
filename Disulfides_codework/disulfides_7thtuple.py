import math

def replace(line):  # This function takes exactly one string as an argument.    
                      # The string is an atom line from the PDB.                
                   # What the statement will return is a 3-tuple of floating    
                          #  point coordinates.                                 

    x = float(line[30:38].strip())  # Non-line-specific x-coordinate PDB column location, space stripped with a floating point
    y = float(line[38:46].strip())  # Same for y-coordinate PDB column location  
    z = float(line[46:54].strip())  # Same for z-coordinate PDB column location

    return (x, y, z)  #  holds xyz coordinates for future use

def distance(t1,t2):   #This function takes two arguments, each in the form of a 3-member tuple corresponding to 1 of 2 sets of xyz coords.
    x1 = t1[0]
    y1 = t1[1]
    z1 = t1[2]

    x2 = t2[0]
    y2 = t2[1]
    z2 = t2[2]

    distance  = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)) # algebraic distance formula using ordered tuple members

    return distance   #  holds distance in Å for future use


PDBid1 = "ATOM    333  SG  CYS A  44      18.599   4.631  39.932  1.00 10.09           S "   # string for use as the replace argument
PDBid2 = "ATOM    723  SG  CYS A 105      20.694   5.034  39.760  1.00 10.97           S "   #  another one

t1 = replace(PDBid1)  
t2 = replace(PDBid2)

print "The Sg to Sg distance is: ", distance(t1,t2)


# print "The xyz coords of PDBid1 are: ", replace(PDBid1)
# print "The xyz coords of PDBid2 are: ", replace(PDBid2)


