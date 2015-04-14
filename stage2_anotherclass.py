class Appliance:
    "Pricing, power source, and store location for all household appliances"
  ##  electricCount = 0                                                                                              

    def __init__(self, name, price, energy, store):
        self.name = name
        self.price = price
        self.energy = energy
        self.store = store


    def displayAppliance(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store

items = []

items.append(Appliance("stove", "$650", "electric or gas", "Wright Appliance"))
items.append(Appliance("refrigerator", "$825", "electric", "Home Depot"))
items.append(Appliance("washer", "$500", "electric", "Sears"))
items.append(Appliance("dryer", "$425", "electric or gas", "Sears"))
items.append(Appliance("water heater", "$490", "electric or gas", "Lowe's"))
items.append(Appliance("air conditioner", "$1100", "electric", "Wright Appliance"))
items.append(Appliance("oil heater", "$200", "electric", "Lowe's"))


class Appliances:
    "List object to put list objects in"
    electricCount = 0

    def __init__(self, Appliance):
        
        returns ['name']

    def displayCount(self):
        print "Total electric appliances available: %d" % Appliances.electricCount


    def displayAppliances(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store
 
## items = []

## items.append(Appliance("stove", "$650", "electric or gas", "Wright Appliance"))
## items.append(Appliance("refrigerator", "$825", "electric", "Home Depot"))
## items.append(Appliance("washer", "$500", "electric", "Sears"))
## items.append(Appliance("dryer", "$425", "electric or gas", "Sears"))
## items.append(Appliance("water heater", "$490", "electric or gas", "Lowe's"))
## items.append(Appliance("air conditioner", "$1100", "electric", "Wright Appliance"))
## items.append(Appliance("oil heater", "$200", "electric", "Lowe's"))

print "Here are the %d appliances common in households:" % Appliances.electricCount

for name in items:

    name.displayAppliance()


## appliances = "stove,refrigerator,washer,dryer,water heater,air conditioner,heater" 
