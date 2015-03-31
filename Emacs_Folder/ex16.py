from sys import argv

script, filename = argv

print "Erase %r." % filename
print "If not, hit CTRL-C (^C)."
print "If yes, hit RETURN."

raw_input("?")

print "Opening the file.."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now make up three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Write these lines to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And then we close the file because that's important."
target.close()
