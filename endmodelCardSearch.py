#import os   #from RetrieveFunctionFinal.py

#def retrieve(path):

   # os.system('grep " END " ' + path + ' | grep -e "^ATOM" >temp.txt')

#class CompleteModel(object):
    #pass

#class HasAtoms(CompleteModel):
    #def _init_(self, ATOM):
        #self.name = 
    


#ATOM = True
#END = True

#for ATOM + END:
     #print "Model and EndCard both present."

#if ATOM, not END:
    #print "No EndCard present."

#if END, not ATOM:
    #print "No model present."

#elif:
    #print "No useful input available. Try again please."


## Pseudo-code:
#Access a pdbid text file - use a retrieve function & path
#Search the text file for the words "MODEL" and "ENDMDL" to be sure files are 
# readable.
#Stop the search after something or nothing is found

#from sys import argv

#script, filename = argv
#filename = "1UBQ.pdb"
#script = endmodelCardSearch.py

#print "Opening the file..."
#target = open(filename, 'w')

##  sys.argv[1] will return a string that is the 1st command line argument, like this:
## python endmodelCardSearch.py 1UBQnone.pdb  [enter] perates on the file designated


import sys  # import sys = accessing the system parameters and functions

f = open(sys.argv[1], "r")    ##Variable to open a file from the command line if you are in the Desktop directory
                              ##   and the file is, too.  sys.argv is the list of command line arguments passed to a  
presentModel = False          ##  Python script - first is the script name, then the file to be opened, then what to do
presentEndMdl = False         ##  with the file = "read"
Var1 = "MODEL"  
Var2 = "ENDMDL"               #Set the search item variables up as "False" to start
                              #Name the variables.In PDB files, they're all-cap strings.
for line in f:                #Set up a for-loop.  "line" is an object Python knows;  "f" is defined variable above.
    #print line[0:5]            #Debugging test to see whether Python was finding what I wanted it to find.
     if Var1 == line[0:5]:       #Tells Python where to look for a variable;  == is "Equal", "Equivalent", not just true.
          presentModel = True  #Changes the condition flag on the search variable;  Not "Equal", just True
     if Var2 == line[0:6]:       # Python counts string characters weird : start at "0" &  end 1 Past the string length
          presentEndMdl = True  #Changes the condotion flag on the other search variable
          
if presentModel and presentEndMdl:
     print "Both Model and EndCard are present."
elif (not presentModel) and (not presentEndMdl):
     print "No useable data. Try again please."
elif presentModel and not presentEndMdl:
     print "Model present, but Endcard missing."
elif presentEndMdl and not presentModel:
     print "EndCard present, but Model missing."
     
else:
     print "Something went wrong.  Try again please."


