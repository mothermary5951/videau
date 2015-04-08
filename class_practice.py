class protein:
    amino_acids = 0
    helix_number = 0
    chainid = []

    def fold(self):
        print "This protein has %d aminos" % self.amino_acids

    def count_helix(self):
        print "This protein has %d helices" % self.helix_number

    def printguts(self):
        self.fold()
        self.count_helix()

class subunit(protein):
    def domain(self):
        print "%s is chain id" % self.chainid


    def printguts(self):
        self.fold()
        self.count_helix()
        self.domain()


betasheet = subunit()
betasheet.amino_acids = 28
betasheet.helix_number = 0
betasheet.chainid = ['D']
## betasheet.fold()
##betasheet.count_helix()
##betasheet.domain()
betasheet.printguts()

    
ricin = protein()
ricin.amino_acids = 267
ricin.helix_number = 5
##ricin.fold()
##ricin.count_helix()
ricin.printguts()

hemoglobin = protein()
hemoglobin.amino_acids = 102
hemoglobin.helix_number = 3
##hemoglobin.fold()
##hemoglobin.count_helix()
hemoglobin.printguts()

