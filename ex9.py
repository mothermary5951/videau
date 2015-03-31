x = "There are %d types of people." % 10   # x = code for text with %d number formatter; number to be inserted is added at the end.
binary = "binary"  # for insertion wherever
do_not = "don't"   # for insertion wherever
y = "Those who know %s and those who %s." % (binary, do_not)  # code for the punch line

print x   #code of joke
print y   #code for punchline

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

#Python returned:
#There are 10 types of people.
#Those who know binary and those who don't.
#I said: 'There are 10 types of people.'.
#I also said: 'Those who know binary and those who don't.'.
#Isn't that joke so funny?! False
#This is the left side of...a string with a right side.


print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?"

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens;  it bumps the "Burger" word to the next line!
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#Python returns this:
#Mary had a little lamb.
#Its fleece was white as snow.
#And everywhere that Mary went.
#..........
#Cheese Burger

#Python returns this without a comma:
#Mary had a little lamb.
#Its fleece was white as snow.
#And everywhere that Mary went.
#..........
#Cheese
#Burger


print end1 + end2 + end3 + end2 + end1 + end4,
print end7 + end8 + end9 + end10 + end11 + end12

#Python returned:
#ChehCe Burger


