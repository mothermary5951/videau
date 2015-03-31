from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#DING! c3po ~/Desktop/mystuff/Emacs_Folder> python ex8emacs.py first 2nd 3rd
# note the command line entry - you don't just enter the file name!!
#The script is called: ex8emacs.py
#Your first variable is: first
#Your second variable is: 2nd
#Your third variable is: 3rd

#15:07:50 c3po ~/Desktop/mystuff/Emacs_Folder> python ex8emacs.py yours mine ours 
#The only place the arguments are changed is in the command line
#The script is called: ex8emacs.py
#Your first variable is: yours
#Your second variable is: mine
#Your third variable is: ours


