#cheese_and_crackers is a function defined by 'def' as the # of cheeses and the # of boxes of crackers

def cheese_and_crackers(cheese_count, boxes_of_crackers):  #These are arguments
# This line provides a line of print with a formatter identifying the # of cheeses.
    print "You have %d cheeses!" % cheese_count
#  This line provides a line of print with a formatter identifying the # of boxes of crackers.
    print "You have %d boxes of crackers!" % boxes_of_crackers
# This line is shown above as a part of the function cheese_and_crackers
    print "Man, that's enough for a party!" 
#This line is also part of the function &  provides a hard return at the end of the function.
    print "Get a blanket.\n"

# We can require the amounts in the function to remain fixed:
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# We can alter the arguments within the script to include name changes and amounts
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we can input various amounts for the two catgories and manipulate them arithmetically
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# we can change the arguments within a script and do math on fixed values
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
 
