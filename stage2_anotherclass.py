class Appliance:
    "Pricing, power source, and store location for all household appliances"                                                                                              
    def __init__(self, name, price, energy, store):
        self.name = name
        self.price = price
        self.energy = energy
        self.store = store


    def displayAppliance(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store

    def displayName(self):
        print "Item: %s" % self.name

class Appliances:
    "List object to put list objects in"
    electricCount = 0
    items = []          ##  the objects in 'items' are all the appliances listed below but not specifically listed here for humans. 

    def condense(self, name, price, energy, store):
        purchase = Appliance(name, price, energy, store)

        self.items.append(purchase)    ## Note the 'self.' before 'items;  becomes very important in the for-loop below.

        if energy == "electric":
            self.electricCount += 1

        elif energy == "electric or gas":
            self.electricCount += 1

        else:
            self.electricCount += 0

    def displayCount(self):
        print "Total electric appliances available: %d" % self.electricCount  ##KEEP TRYING TO FIX THIS TOMORR

    def displayAppliances(self):

        for each_Appliance in self.items:
            each_Appliance.displayAppliance()


    def displayNames(self):      ##  DisplayNames should iterate through the 'items' list and call 'DisplayName' on each appliance object.
                                     ## two lines of code
        for each_Appliance in self.items:
            each_Appliance.displayName()

installs = Appliances()

installs.condense("stove", "$650", "gas", "Wright Appliance")
installs.condense("refrigerator", "$825", "electric", "Home Depot")
installs.condense("washer", "$500", "electric", "Sears")
installs.condense("dryer", "$425", "electric or gas", "Sears")
installs.condense("water heater", "$490", "gas", "Lowe's")
installs.condense("air conditioner", "$1100", "electric", "Wright Appliance")
installs.condense("oil heater", "$200", "electric", "Lowe's")



installs.displayNames()
installs.displayAppliances()
installs.displayCount()


