class chi4280:
    "Arg chi4 tpt rotamers in the 280 degree group"
    rotamerCount = 0

    def __init__(self, pdbid, chain, residue):
        self.pdbid = pdbid
        self.chain = chain
        self.residue = residue
        self.rotamerCount += 1

    def displayCount(self):
        print "Total rotamer %d" % self.rotamerCount

    def displaychi4280(self):
        print "PDBid: ", self.pdbid, ", Chain: ", self.chain, ",Residue: ", self.residue

rotamer1 = chi4280("1a7s", "A", "210")
rotamer2 = chi4280("1jiw", "P", "171")
rotamer3 = chi4280("1k2x", "C", "111")
rotamer4 = chi4280("1p1j", "A", "222")
rotamer5 = chi4280("1p1j", "A", "225")
rotamer6 = chi4280("1q0r", "A", "46")
rotamer7 = chi4280("1rkd", "A", "298")
rotamer8 = chi4280("1y0h", "A", "23")
rotamer9 = chi4280("1y0h", "A", "62")

results = chi4280.displaychi4280()

## results = displaychi4280(["rotamer1", "rotamer2", "rotamer3", "rotamer4", "rotamer5", "rotamer6", "rotamer7", "rotamer8", "rotamer9"])
## print "Here are selected instances of Arg tpt280 rotamers: %s" % results                                                    

print "Here are selected instances of Arg tpt280 rotamers: %s" % results

  



