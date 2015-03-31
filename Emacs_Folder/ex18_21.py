ex18.py

# this one is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#Ok, that *args is actually pointless; we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again ("Zed", "Shaw")
print_one("First!")
print_none()


ex19.py

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


ex19A.py

def rotamer_category(secondary_structure, dihedral_angle, res_num):
    print "The rotamer is in %s structure." % secondary_structure
    print "The dihedral angle is %d degrees." % dihedral_angle
    print "The amino acid sequence number is %d." % res_num
    print "What a lovely little function this is!\n"
 
print "We can just give the function info directly:"
rotamer_category('beta', 32, 127)

print "OR, we can use variables from our script:"
helix_sheet = 'alpha'
N_CA_C_N = 40
seq_num = 215

rotamer_category(helix_sheet, N_CA_C_N, seq_num)

print "We can even do math inside!"
rotamer_category('none', 360 - 32.0 / 15, 428 - 19 + 12)

print "We can use user input for the arguments:"
print "What is the secondary structure environment?",
secondary_structure = raw_input()
print "What is the dihedral angle?",
dihedral_angle = raw_input()
print "What is the sequence number?",
res_num = raw_input()
print "So, the secondary structure is %d, the dihedral is %d, and the residue number is %d." % (secondary_structure, dihedral_angle, res_num)
