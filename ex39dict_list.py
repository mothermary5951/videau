xpeople = ['shirley', 'fred', 'patrick', 'sam'] ## list of strings
print people[1]  ## returns result by the index, which is 'fred'

people[2] = 'Steven' ## YOU MUST USE the index number to change list members #######
print people[2]  ## returns result by the index number 2, which has been changed to 'Steven'

print people  ## returns revised list as string ['shirley', 'fred', 'Steven', 'sam']

##  NOTES ON DICTs:  ANYTHING can go in a dictionary. A dictionary is a container. YOU CANNOT USE an index number in a dictionary!! #####
##  I used the round builtin because I couldn't figure out where to use the %.2f two-decimal float rounder.

first_dict = {'car' : '1969 Volks', 'lodging' : 'apartment', 'job' : 'programmer', 'height' : round(185 / 2.54 + 4)}
print first_dict['lodging']  # calling the dict key returns the key object, in this case 'apartment'
print first_dict['car']
print first_dict['height']

first_dict['job'] = 'bottle washer'  ##  objects in dictionaries are really easy to add, but the order is known
print first_dict['job']                ## only to python - and NOT by cardinal numbers, not by indices the way lists do it.

first_dict['city'] = 'New York City'  ##  adding a new key and its corresponding value in whatever order python picks, somewhere in the

first_dict[0] = 'start point'    ## using integers for keys and text strings for values
first_dict[3] = 'strong'

print first_dict[0]          ## This will return 'start point'
print first_dict[3]          ## This returns 'strong'

print first_dict  ## This returns {0: 'start point', 'city': 'New York City', 3: 'strong', 'car': '1969 Volks', 'height': 77.0, 'job': 'bottle washer', 'lodging': 'apartment'}

del first_dict['city']  ## This is one way to remove an object from a dictionary
first_dict.pop('car')   ## This is another way to remove an item, but it won't remove automatically from the end;  you have to specify which item to remove.
## rm first_dict(0)     ##  This Does Not work to remove objects

print first_dict






