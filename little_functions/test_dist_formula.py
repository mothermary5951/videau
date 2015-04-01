import math  # math is module(word?) native to python

def SG_dist(t1, t2):  # my function is named SG_dist and has two arguments, 
                       # which I will make as tuples to maintain their
                        #  members' positions
    x1 = t1[0]  #  This tuple position descriptions cannot be enclosed as tuples becausetuples cannot be changed
    y1 = t1[1]  #   That's why the parens are not proper tuple parens
    z1 = t1[2]

    x2 = t2[0]
    y2 = t2[1]
    z2 = t2[2]

    distance = math.sqrt(((x2 - x1) **2) + ((y2 - y1) **2) + ((z2 - z1) **2)) # I didn't remember exactly where 
                                                                               #   to put math.sqrt    
    return distance

t1 = (18.599, 4.631, 39.932)
t2 = (20.694, 5.034, 39.760)

print "The distance between SG44 and SG105: ", SG_dist(t1, t2)

