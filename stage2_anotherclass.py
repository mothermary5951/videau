class Appliance:      ## creates class 'Appliance' - a 'class' is NOT a container
    "Name, pricing, power source, and store location for one unspecified household appliance"  ## attributes of class listed for user reminders                                                                                              
    def __init__(self, name, price, energy, store):  ##initiating the class REQUIRES 'self' as an argument in python
        self.name = name       ## 'self' is then applied to all attributes to associate all the things to the class.
        self.price = price     ##  These are where the attributes are actually defined
        self.energy = energy
        self.store = store


    def displayAppliance(self):    ##  This is a function written to display the general attributes of a class member
        print "Item:", self.name, "Price:", self.price, "Energy Source:", self.energy, "Store:", self.store   ## format for function result returned 

    def displayName(self):      ##  This is a function written to display only the name of a class member 
        print "%s"% self.name  ##  format for function result returned

class Appliances:   ## creates class Appliances as a list object to put the list of objects in
    "List object to put list objects in"
    electricCount = 0           ##  Creates a variable to be changed by the if-elif below
    items = []          ##  the objects in 'items' are all the class members listed below but not specifically described here for humans. 

    def condense(self, name, price, energy, store):  ## This is a function called to integrate the details of 'Appliances' class into 'Appliance' class
        purchase = Appliance(name, price, energy, store)   ## Variable using the generalness of class 'Appliance'

        self.items.append(purchase)    ## Note the 'self.' before 'items;  becomes very important in the for-loop below. 'Append' is called on 'purchase'
                                       ##     general object to fill list 'items' with 'Appliances' class members shown below.
        if energy == "electric":       ## 'if' condition set to count members available as electric only
            self.electricCount += 1

        elif energy == "electric or gas":  ##  'elif' condition set to include members in count available in either electri or gas
            self.electricCount += 1

        else:
            self.electricCount += 0    ## 'else' condition set to exclude members available in gas only

    def displayCount(self):  ## Function written to count all members available as electric
        print "Total electric appliances available: %d" % self.electricCount   ##  Returns the function's result

    def displayAppliances(self):  ## Function written to display member details

        for each_Appliance in self.items:    ## for-loop to iterate through'items' list and gather definition of each member, one at a time.
            each_Appliance.displayAppliance()  ##  calls displayAppliance on each object 


    def displayNames(self):      ##  function written to iterate through the 'items' list and call 'DisplayName' on each appliance object.
                                     ## two lines of code
        for each_Appliance in self.items:
            each_Appliance.displayName()

installs = Appliances()  ## variable outside of classes coding with one argument, default 'self'

installs.condense("stove", "$650", "gas", "Wright Appliance")   # calls the 'condense' function on list 'items' under Appliances
installs.condense("refrigerator", "$825", "electric", "Home Depot")
installs.condense("washer", "$500", "electric", "Sears")
installs.condense("dryer", "$425", "electric or gas", "Sears")
installs.condense("water heater", "$490", "gas", "Lowe's")
installs.condense("air conditioner", "$1100", "electric", "Wright Appliance")
installs.condense("oil heater", "$200", "electric", "Lowe's")



installs.displayNames()  ## calls the 'displayNames' function on list 'items' under Appliances - result is returned by function called in for-loop
installs.displayAppliances()  ## calls the 'displayAppliances' function on list 'items' under Appliances - result is returned by function called in for-loop
installs.displayCount()  ## calls the 'displayCount' function on list 'items' under Appliances - result is returned by function called in for-loop


