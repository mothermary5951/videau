from sys import argv

script, filename1, filename2 = argv

txt1 = open(filename1)
txt2 = open(filename2)

print "Here are your files %r and %r:" % (filename1, filename2)
print txt1.read()
print txt2.read()


