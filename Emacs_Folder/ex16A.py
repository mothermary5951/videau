from sys import argv

script, filename = argv

print "We're going to read %r." % filename
print "If you dont' want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file.."
target = open(filename, "r")  #opens the file
print target.read()           #PRINTS the file out sothat the user can see it

target.close()




