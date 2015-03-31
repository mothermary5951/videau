#  str = ['line1', 'line2', 'line3', 'line4']

#  str.splitlines( num=string.count('\n'))

# l = ATOM this going to 333.44 555.66 be astring SG

#  print str(l)

# with open ("textmess.txt", "r") as myfile:
#    data=myfile.readlines()

# print data

myfile = open("textmess.txt", "r")                                    

str = myfile.read()

data = str.splitlines()   

print data

