ten_things = "Apples Oranges Crows Telephone Light Sugar" # This variable is a string and a list.

print "Wait there are not 10 things in that list.  Let's fix that."  

stuff = ten_things.split(' ') #split(' ') separates string members w/ single parens and with commas
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # new list for
                                    # adding members to first incomplete list.
while len(stuff) != 10:  # len() is function to output length of something, here the 'stuff' list.
    next_one = more_stuff.pop() #pop()-function to isolate list members singly in order designated
    print "Adding: ", next_one   # identifies popped list member to be added to another list.
    stuff.append(next_one)   # append(next_one) function adds popped member to orig. list 
    print "There are %d items now." % len(stuff) # function counts members in 'stuff' list

print "There we go: ", stuff  # prints current version of stuff list with new popped member

print "Let's do some things with stuff."

print stuff[1]   # Square brackets mark LISTS!  Which can be changed, or 'appended' to.
print stuff[-1]  #  whoa!  fancy  # prints only the last member of the list
print stuff.pop()  # pop() empty parens go to the end of the list; a number will be an index
print ' '.join(stuff) #  what? cool!   # prints stuff list cleanly, with no punctuation at all
print '#'.join(stuff[3:7])  # super stellar! # prints a range of list members separated by only #.

## NOTE: TUPLES ARE IN PARENS, AND CANNOT BE CHANGED or APPENDED TO!!!!!
  

