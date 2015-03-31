import math  #  The 'math' package is not part of the 'sys';  it's its own thing

def distance(t1, t2):  #  the distance needs two arguments made up of the 6 coordinates

    x1 =  t1[0]  # Each item in the tuple must be defined in turns of Location! 0, 1, 2, 3
    y1 =  t1[1]
    z1 =  t1[2]
 
    x2 =  t2[0]  # Each item in the tuple must be defined in turns of Location! 0, 1, 2, 3 
    y2 =  t2[1]
    z2 =  t2[2]
 
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)) # This is
                                         # the function's definition.
    return distance     #Save this answer to the function's query.

mike = (1, 2, 3)     # new name and real coordinates for argument #1, t1 above
joe = (2, 4, 6)      # new name and real coordinates for argument #2, t2 above

print distance(mike, joe)  # This calls the function and passes it the real data from 2 tuples
