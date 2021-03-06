
import hashmap

##  create a mapping of state to abbreviation                                                       
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')  ## The state name is the key, and the abbreviation is the value.              
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')


##  create a basic set of states and some cities in them                                            
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')  ## The abbreviation is the key, and the city is the value              
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')


##  add some more cities                                                                            
hashmap.set(cities, 'NY', 'New York')  ## These are additions to the Dict 'cities'                              
hashmap.set(cities, 'OR', 'Portland')

## print out some cities                                                                            
print '-' * 10
print "NY State has %s" % hashmap.get(cities, 'NY')    ## calls the key in dict 'cities'                                
print "OR State has %s" % hashmap.get(cities, 'OR')

##  print some states                                                                               
print '-' * 10
print "Michigan's abbreviation is %s" % hashmap.get(states, 'Michigan') ## calls the key in dict 'states'            
print "Florida's abbreviation is %s" % hashmap.get(states, 'Florida')

##  do it by using the 'states' then 'cities' dicts                                                 
print '-' * 10
print "Michigan has %s" % hashmap.get(cities, hashmap.get(states, 'Michigan')) ## maps 'states' to state to abbreviation          
print "Florida has %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))    ## then abbreviation to city                      

## print every state abbreviation                                                                   
print '-' * 10
hashmap.list(states)
              
## print every city in state                                                                        
print '-' * 10
hashmap.list(cities)

print '-' * 10                                      
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."

## default values using ||= with the nil result
## can you do this on one line?                                                                  
    city = hashmap.get(cities, 'TX','Does not exist')
print "The city for the state 'TX' is %s" % city

