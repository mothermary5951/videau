cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = carpool_capacity / passengers


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Python gave this result:
#There are 100 cars available.
#There are only 30 drivers available.
#There will be 70 empty cars today.
#We can transport 120.0 people today.
#We have 90 to carpool today.
#We need to put about 1.33333333333 in each car.   #NOTE:  Python returned a floating
#point number as an answer here because the same variable was assigned a floating point
# ("passengers = 4.0") in the original value assignments.
