from sys import argv

script, shoe, size, color = argv

#x = raw_input("size")
#y = raw_input("color")

print "What is your shoe size?",
size = raw_input()
print "What color are your shoes?",
color = raw_input()

print "The script is called:", script
print "Your first variable is:", shoe
#print "Your second variable is:", size
print "So your shoe is size %r." % (size) 
#print "Your third variable is:", color
print "So your shoes are %r." % (color)

#Output:
#16:08:15 c3po ~/Desktop/mystuff/Emacs_Folder> python ex9emacs.py shoe size color 
#What is your shoe size? 8
#What color are your shoes? blue
#The script is called: ex9emacs.py
#Your first variable is: shoe
#So your shoe is size '8'.
#So your shoes are 'blue'.






