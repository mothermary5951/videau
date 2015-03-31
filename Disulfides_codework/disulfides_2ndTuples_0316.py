import math

def distance(t1,t2):
    
    x1 = t1[0]
    y1 = t1[1]
    z1 = t1[2]

    x2 = t2[0]
    y2 = t2[1]
    z2 = t2[2]

    distance  = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2))

    return distance

atom1 = (1, 2, 3)
atom2 = (2, 4, 6)
atom3 = (5, 6, 7)
atom4 = (10, 12, 14)
Cys44sg = (-3.835, 25.597, 31.445)
Cys105sg = (-3.940, 27.576, 32.237)


print distance(atom1, atom2)
print distance(atom3, atom4)
print distance(Cys44sg, Cys105sg)    
