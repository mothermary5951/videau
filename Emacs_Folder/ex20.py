from sys import argv #calls a portion of the sys package for use.

script, input_file = argv  #specifies items that the arguments will operate on

def print_all(f): #defines the 1st function as 'print the whole file: 
                  # f = variable name for 'file'
    print f.read() # print out all that is readable 

def rewind(f):    # defines the 2nd function as go back to the file's start
    f.seek(0)     # Command to go back and find the file's 1st byte.

def print_a_line(line_count, f): #  3rd function is defined as printing single
                                  # lines of the ones the function counts 
                                  # in the file
    print line_count, f.readline()   # prints out each line numbered with a                                      
    								#hard return at the end of each line as
                                     # read in the file

current_file = open(input_file)     #defines which file is 'current': the one
                                          # in the command line
print "First, let's print the whole file:\n"

print_all(current_file)           #prints the whole file with no spaces between
                                    #the lines

print "Now let's rewind, kind of like a tape."

rewind(current_file)              #moves the read head to the file 0 byte

print "Let's print three lines:"  

current_line = 1                  #defines where to begin
print_a_line(current_line, current_file)  #what to do and where to do it to
                                 # print_a_line knows how many lines are in
                                 # the file; Current_line has to be defined each
                                 # time print_a_line is called.
current_line += current_line       # moves read head to the next endline \n
print_a_line(current_line, current_file)   #Tells what to DO next

current_line += current_line      #defines what is next
print_a_line(current_line, current_file)     #Tells what to DO next

