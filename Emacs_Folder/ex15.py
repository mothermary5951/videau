from sys import argv    # imported the argv package into the script  #THIS is a python command

script, filename = argv   #provided the two arguments shown #filename = argv is a python command
filename = raw_input('> ')
txt = open(filename)     # fetches and opens the file given as an argument (# txt = open('ex15_sample.txt')
                                                                          #is a python command 
                                                        #  THE FILENAME IS A STRING!!

print "Here's your file %r:" % filename  #pulls the file name out of the command line, arg #2;
print txt.read()           # txt identifies the open file, the '.' gives a command, and read is
                             # a function & the command that prints out the actual text in the doc.
                             # print txt.read() is a python command
txt.close()

#print "Type the filename again:"
#file_again = raw_input("> ")       #variable to generate user info  #  THE FILENAME IS A STRING!!

#txt_again = open(file_again)       #variable to open a user-designated file

#print txt_again.read()         # using the variable to call the read function again to print out 
                                # the file contents

