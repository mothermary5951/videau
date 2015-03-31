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

PDBid1 = "ATOM    333  SG  CYS A  44      18.599   4.631  39.932  1.00 10.09           S "
PDBid2 = "ATOM    723  SG  CYS A 105      20.694   5.034  39.760  1.00 10.97           S "



print PDBid1[12:60]
print PDBid2[12:60]

x1 = float(PDBid1[30:38].strip())
y1 = float(PDBid1[38:46].strip())
z1 = float(PDBid1[46:54].strip())

x2 = float(PDBid2[30:38].strip())
y2 = float(PDBid2[38:46].strip())
z2 = float(PDBid2[46:54].strip())

t1 = (x1, y1, z1)
t2 = (x2, y2, z2)

print "The Sg to Sg distance is: ", distance(t1,t2)

 

# record:  ATOM                                                                                       
#  atom name = 12-16                                                                                  #  residue name = 17-20                                                                               # chain = 22 √                                                                                        
# residue sequence number = 23-26 31:38                                                              
#  x coordinates  =  30-38                       
#  y coordinates  =  38-46                                                                            #  z coordinates  =  46-54                                                                            
#  occupancy  =  54-60                                                                                #  These match a hand-count done on 1jlt 03162015, minus 1 at the start of the chunk to reflect            # python's start of everthing at 0.  (Thus, the numbers in the RCSB column listings are 13-16,
     # 18-20, 24-26, etc.)

 #   x1 = PDBid1[30:38]
 #   y1 = PDBid1[38:46]
 #   z1 = PDBid1[46:54]

 #   x2 = PDBid2[30:38]
 #   y2 = PDBid2[38:46]
 #   z2 = PDBid2[46:54]
    

# t1 = pdb1[4:7]
# x1 = pdb1[4]
# y1 = pdb1[5]
# z1 = pdb1[6]
# print "Here are xyz coords: ", t1


#  PDBid1 = ("61-65")
#  if "HEADER" = ("1-6"):
#    print "PDB ID is: ", PDBid
