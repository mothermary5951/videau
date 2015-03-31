i = 0     # Initiate a new variable in a for-loop;  for-loops go through a list, no matter
numbers = []   # what.  while-loops apply 1 or more conditions,
product = 0 * 2    # and provide a varible condition (usually), rather than a list
n = 0  # this is a total cludge.  You can intitate as many variables as you want, 
                 #even though they have the same value.


print "What is the endpoint?"
end_point = int(raw_input())

for i in range(0,100):   #for-loops generally need an actual list, because they start a start
    print "At the top i is %d" % n     # and go til the end.  while-loop can use a vaguer
    numbers.append(n)        # 'containe'.r

    
    print "How much is the increase this time?"
    y = raw_input()
    
    n = n + int(y)
    print "Numbers now: ", numbers
    print "At the bottom n is %d" % n
    print "And times 2 is %d" % (n * 2)

    if n >= end_point:   #this is a cludge to stop the for-loop from acting like a for-loop
        break            # and going all the way through its 0-100 list.


print "The numbers:"

for num in numbers:
    print num


#  The most important thing about this exercise was learning what while-loops and for-loops 
#  are good for:  for-loops run for a set distance nad run All the way through unless you make
#  a break.  while loops are set up to work through a set of conditions until the conditions  #   are no longer true, no matter how long that takes.
    
#  The output from this program is super=close to the original while-loop function named
#   incremental_Var in the while_loops directory.  Very nice.
    
