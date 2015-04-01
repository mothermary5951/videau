class Grad:
    "Common records for all grad students"
    studentCount = 0

    def __init__(self, name, school):
        self.name = name
        self.school = school
        Grad.studentCount += 1

    def displayCount(self):
        print "Total Grad %d" % Grad.studentCount

    def displayGrad(self):
        print "Name : ", self.name, ", School: ", self.school

"This would create first object of Grad class"
student1 = Grad("Christopher", "Case Western")
"This would create second object of Grad class"
student2 = Grad("Swati", "Columbia University")
student1.displayGrad()
student2.displayGrad()
print "Total students graduating: %d" % Grad.studentCount
 
