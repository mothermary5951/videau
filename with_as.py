with open ('playfile.txt') as file: #uses file to refer to the file object.
                                     # Read is the default; write Can overwrite                                     #whatever is in the file already.
    data = file.read()  #file.close() is called automatically

print data







