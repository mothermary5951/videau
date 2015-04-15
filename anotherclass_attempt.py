class Appliances:
    "Pricing, power source, and store location for all household appliances"
    electricCount = 0

    def __init__(self, name, price, energy, store):
        self.name = name
        self.price = price
        self.energy = energy
        self.store = store
        Appliances.electricCount += 1 

    def displayCount(self):
        print "Total electric appliances available: %d" % Appliances.electricCount

    def displayAppliances(self):
        print "Item: ", self.name, "Price: ", self.price, "Energy Source: ", self.energy, "Store: ", self.store


items = []

items.append(Appliances("stove", "$650", "electric or gas", "Wright Appliance"))
items.append(Appliances("refrigerator", "$825", "electric", "Home Depot"))
items.append(Appliances("washer", "$500", "electric", "Sears"))
items.append(Appliances("dryer", "$425", "electric or gas", "Sears"))
items.append(Appliances("water heater", "$490", "electric or gas", "Lowe's"))
items.append(Appliances("air conditioner", "$1100", "electric", "Wright Appliance"))
items.append(Appliances("oil heater", "$200", "electric", "Lowe's"))

print "Here is the household appliance information for %d electric products:" % Appliances.electricCount 

for e in items:
    
    e.displayAppliances()
    
## appliances = "stove,refrigerator,washer,dryer,water heater,air conditioner,heater"



item1 = Appliances("stove", "$650", "electric or gas", "Wright Appliance")
item2 = Appliances("refrigerator", "$825", "electric", "Home Depot")
item3 = Appliances("washer", "$500", "electric", "Sears")
item4 = Appliances("dryer", "$425", "electric or gas", "Sears")
item5 = Appliances("water heater", "$490", "electric or gas", "Lowe's")
item6 = Appliances("air conditioner", "$1100", "electric", "Wright Appliance")
item7 = Appliances("oil heater", "$200", "electric", "Lowe's")

appliances = "stove,refrigerator,washer,dryer,water heater,air conditioner,heater"

 

