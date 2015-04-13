class chi4280:
    "Arg chi4 tpt rotamers in the 280 degree group"
    rotamerCount = 0

    def __init__(self, pdbid, chain, residue):    ### important to spell init, not "inti"  ahem.
        self.pdbid = pdbid
        self.chain = chain
        self.residue = residue
        chi4280.rotamerCount += 1     ##  This could also read self.rotamerCount

    def displayCount(self):
        print "Total rotamer %d" % chi4280.rotamerCount

    def displaychi4280(self):
        print "PDBid: ", self.pdbid, ", Chain: ", self.chain, ",Residue: ", self.residue

rotamers = []   ## The empty list enables the running of a for-loop.


rotamers.append(chi4280("1a7s", "A", "210"))   ## calls append on the variable (emptylist) rotamers to fill the list 
rotamers.append(chi4280("1jiw", "P", "171"))
rotamers.append(chi4280("1k2x", "C", "111"))
rotamers.append(chi4280("1p1j", "A", "222"))
rotamers.append(chi4280("1p1j", "A", "225"))
rotamers.append(chi4280("1q0r", "A", "46"))
rotamers.append(chi4280("1rkd", "A", "298"))
rotamers.append(chi4280("1y0h", "A", "23"))
rotamers.append(chi4280("1y0h", "A", "62"))

print "Here are %d selected instances of Arg tpt280 rotamers:  " % chi4280.rotamerCount

for e in rotamers:             # Easy little for-loop;  Use 'i' for numbers and 'e' for elements.
    e.displaychi4280()         ## Calls the defined function 'displaychi4280' on the 'elements' in list 'rotamers'.
    


  



