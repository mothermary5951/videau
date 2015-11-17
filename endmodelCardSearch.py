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

##  sys.argv[1] will return a string that is the 1st command line argument


import sys

f = open(sys.argv[1], "r")

presentModel = False
presentEndMdl = False
Var1 = "MODEL"  ## Need location of "MODEL"
Var2 = "ENDMDL"

for line in f:
     if Var1 in line:
          presentModel = True
     if Var2 in line:
          presentEndMdl = True

if presentModel and presentEndMdl:
     print "Both Model and EndCard are present."
if not presentModel and not presentEndMdl:
     print "No useable data. Try again please."
if presentModel and not presentEndMdl:
     print "Model present, but Endcard missing."
if presentEndMdl and not presentModel:
     print "EndCard present, but Model missing."
else:
     print "Something went wrong.  Try again please."


