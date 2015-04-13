Cysdihedrals = "phi psi chi1 chi2 chi3 chi2p chi1 phip psip"  ## This is a string, not a list

BothCysAngles = Cysdihedrals.split()   # This turns the string into a list of strings.
print "These are both sets of Cys dihedrals: %s" % BothCysAngles     ## prints out list of strings in the format chosen as an argument above.
 
while len(BothCysAngles) >= 5:     
    next_one = BothCysAngles.pop()   ## pop changes the list in place
    print "Deleting: ", next_one    
    print "Now there are %d dihedrals." % len(BothCysAngles) #activates while-loop

