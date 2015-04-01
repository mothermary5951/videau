import math    # still native python

def column_data(line):  # my name for my function that pulls the 3 coordinates out of an ATOM line

    x1 = float(PDBid[30:38].strip())    # I didn't remember where the parens went and had to look up the column nums.
    y1 = float(PDBid[38:46].strip())
    z1 = float(PDBid[46:54].strip())

    return (x1, y1, z1)

PDBid = "ATOM    339  SG  CYS A  45      13.513   8.338  39.105  1.00 10.11           S"

print "xyz coords for SG44: ", column_data(PDBid)




    
