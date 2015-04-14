class Appliance:
    "Pricing, power source, and store location for all household appliances"                                                                                              
    def __init__(self, name, price, energy, store):
        self.name = name
        self.price = price
        self.energy = energy
        self.store = store


    def displayAppliance(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store

class Appliances:
    "List object to put list objects in"
    electricCount = 0
    items = []

    def condense(self, name, price, energy, store):
        purchase = Appliance(name, price, energy, store)

        self.items.append(purchase)    

        if energy == "electric":
            self.electricCount += 1

        elif energy == "electric or gas":
            self.electricCount += 1

        else:
            self.electricCount += 0

    def displayCount(self):
        print "Total electric appliances available: %d" % Appliances.electricCount

    def displayAppliances(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store

installs = Appliances()

installs.condense("stove", "$650", "gas", "Wright Appliance")
installs.condense("refrigerator", "$825", "electric", "Home Depot")
installs.condense("washer", "$500", "electric", "Sears")
installs.condense("dryer", "$425", "electric or gas", "Sears")
installs.condense("water heater", "$490", "gas", "Lowe's")
installs.condense("air conditioner", "$1100", "electric", "Wright Appliance")
installs.condense("oil heater", "$200", "electric", "Lowe's")

print  "Here are the %d appliances common in households:" % installs.electricCount

for name in installs:

    name.displayAppliance()
