from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
 
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
 
print "And finally, we close it."
target.close()
   

#Here's a way to just open that file I made, entitled 'Special.txt":
from sys import argv

script, filename = argv

print "We're going to read %r." % filename
target = open(filename)
#

#And another way to open the same file directly from the command line:
#15:34:32 c3po ~/Desktop/mystuff/Emacs_Folder>  python
>>> txt = open("special.txt")
>>> txt.read()
He had tan shoes and pink shoelaces.
He had a pink panama with a purple hat band.
Those are words to an old song.
>>> txt.close()
#
