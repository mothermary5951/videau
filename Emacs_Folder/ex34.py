
#  animals = ('bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus')
#  ordinals = ('1st', '2nd', '3rd', '4th', '5th', '6th')

#  print "Which animal is at the %r position?" % raw_input()


animals = ('bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus')
ordinals = ('1st', '2nd', '3rd', '4th', '5th', '6th') 

for animal in animals:
    print "This animal is a: %s" % animal

for sequence in ordinals:
    print "They're in this order: %s" % sequence

dict = {'1st' : 'bear', '2nd' : 'python', '3rd' : 'peacock', '4th' : 'kangaroo', '5th' : 'whale', '6th' : 'platypus'}

print "Who's where?"
print "The %r is at this position." % dict[raw_input()]

#  So, this little script works in One direction - postion to animal - but I don't yet know how to make it run in either direction.


# print animals[1]
# print animals[2]
# print animals[0]
# print animals[3]
# print animals[4]
# print animals[5]
# print animals[2]
# print animals[4]

# animals = ('bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus')                                                                    
#ordinals = ('1st', '2nd', '3rd', '4th', '5th', '6th')                      

#print map(animals, ordinals)
#    answer = []
#    for elem in ordinals:
#        answer.append(animals)
#    return answer
#
# 
#ordinal  = raw_input("Which animal is at the %s position? ")
#print "It's the %s!" % 
#




    
