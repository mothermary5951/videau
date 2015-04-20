##  create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',  ## The state name is the key, and the abbreviation is the value.
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

##  create a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',  ## The abbreviation is the key, and the city is the value
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

##  add some more cities
cities['NY'] = 'New York'  ## These are additions to the Dict 'cities'
cities['OR'] = 'Portland'

## print out some cities
print '-' * 10
print "NY State has", cities['NY'] ## calls the key in dict 'cities'
print "OR State has", cities['OR']

##  print some states
print '-' * 10
print "Michigan's abbreviation is", states['Michigan'] ## calls the key in dict 'states'
print "Florida's abbreviation is", states['Florida']

##  do it by using the 'states' then 'cities' dicts
print '-' * 10
print "Michigan has", cities[states['Michigan']] ## maps 'states' to state to abbreviation
print "Florida has", cities[states['Florida']]    ## then abbreviation to city

## print every state abbreviation
print '-' * 10
for state, abbrev in states.items():   ## for-loop iterates through each item & returns abbrev.
    print "%s state is abbreviated %s" % (state, abbrev)  ## you can use 'e' instead of 'state'
                                            ## here and in line 38
## print every city in state                                                                  
print '-' * 10
for abbrev, city in cities.items():  ## for-loop iterates through each object and returns city
    print "%s has the city %s" % (abbrev, city)

## now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has %s" % (state, abbrev, cities[abbrev])

print '-' * 10
## safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

## get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is %s" % city





