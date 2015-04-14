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

    def condense(name, price, energy, store):
        purchase = Appliance(name, price, energy, store)

        items.append(purchase)    

        if energy == "electric":
            electricCount += 1

        elif energy == "electric or gas":
            electricCount += 1

        else:
            electricCount += 0

    def displayCount(self):
        print "Total electric appliances available: %d" % Appliances.electricCount

    def displayAppliances(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store

items.condense("stove", "$650", "gas", "Wright Appliance")
        items.condense("refrigerator", "$825", "electric", "Home Depot")
        items.condense("washer", "$500", "electric", "Sears")
        items.condense("dryer", "$425", "electric or gas", "Sears")
        items.condense("water heater", "$490", "gas", "Lowe's")
        items.condense("air conditioner", "$1100", "electric", "Wright Appliance")
        items.condense("oil heater", "$200", "electric", "Lowe's")

       print  "Here are the %d appliances common in households:" % Appliances.electricCount

        for name in items:

            name.displayAppliance()
