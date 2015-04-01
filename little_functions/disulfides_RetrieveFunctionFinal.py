import os

def retrieve(path):  # This function takes one argument, which is a string containing a path to a PDB file.              
                             #Output is a list of strings consisting of different atom lines          
    os.system('grep " SG " ' + path + ' | grep -e "^ATOM" >temp.txt')

    str = open("temp.txt", "r").read()

    SGdata = str.splitlines()

    return SGdata

path = "/Users/videau/Desktop/1zkr_copy/molprobity/coordinates/1zkrFH_reg.pdb"

print retrieve(path)


# strings = open("temp.txt", "r")

#str = strings.read()

# SGdata = str.splitlines()

# return SGdata



#   grep " SG " 1jltFH_reg.pdb | grep -e "^ATOM" >temp.txt  # <- WRITE output to that.  DON'T LET ANYTHING HAPPEN TO THIS!!!!!

 

#  def retrieve(filename):  # This function takes one argument, which is a string containing a path to a PDB file.
                             #Output is a list of strings consisting of different atom lines


# FINAL VERSION OF RETRIEVE
