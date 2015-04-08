class protein:
    amino_acids = 0
    helix_number = 0

    def fold(self):
        print "This protein has %d aminos" % self.amino_acids

    def count_helix(self):
        print "This protein has %d helices" % self.helix_number


    
ricin = protein()
ricin.amino_acids = 267
ricin.helix_number = 5
ricin.fold()
ricin.count_helix()

hemoglobin = protein()
hemoglobin.amino__acids = 102
hemoglobin.helix_number = 3
hemoglobin.fold()
hemoglobin.count_helix()
