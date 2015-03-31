#  def sub(a, b):
  #  remainder = |a - b|
  #  print remainder
  #  return remainder

#  a = raw_input("x1: ", "y1: ", "z1: ")
#  b = raw_input("x2: ", "y2: ", "z2: ")

# print "distance = %d" % (distance)


import math
math.sqrt((((2.0 - 1.0) ** 2) + ((4.0 - 2.0) ** 2) + ((6.0 - 3.0) ** 2)))

 
#  i  = (((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)) 

a = (((2.0 - 1.0) ** 2) + ((4.0 - 2.0) ** 2) + ((6.0 - 3.0) ** 2))
b = (((10.0 - 5.0) ** 2) + ((12.0 - 6.0) ** 2) + ((14.0 - 7.0) ** 2))
c = ((((-3.490) - (-3.835)) ** 2) + ((27.576 - 25.597) ** 2) + ((32.237 - 31.445) ** 2))

distance1 = math.sqrt(a)
print "1st set atom distance: %d" % distance1

distance2 = math.sqrt(b)
print "2nd set atom distance: %d" % distance2

distance3 = math.sqrt(c)
print "Actual 1jlt Cys44 to Cys105 Sg distance: ", distance3
 


# 1st set of points: x = (1, 2, 3) and y = (2, 4, 6)
# 2nd set of points: x = (5, 6, 7) and y = (10, 12, 14)
# actual 1jlt points: x(Sg Cys44) = (-3.835, 25.597, 31.445) and y(Sg Cys105) = (-3.940, 27.576, 32.237)


# distance = 
# a - b = |"%d "| % distance
# print "%d"





#  from sys import argv

#  script, distance = argv

#  (x1, y1, z1) = (1, 2, 3)
#  (x2, y2, z2) = (2, 4, 6)


#  atompt1 = (x1, y1, z1)
#  atompt2 = (x2, y2, z2)

# distance = (atompt1, atompt2)

#  print "Location of atom1: %d" % atompt1
#  print "Location of atom2: %d" % atompt2

#  sub
