##  This part is Not In the module MyStuff.py

mystuff = {'apple': 'I am apples!'}   ## dictionary-format key:value list of strings
print mystuff['apple']  # print the value mapped to the key 'apple' which is listed in the dictionary mystuff

## This all goes in the module MyStuff.py 

def apple():       # defines a function 'apple' which has one argument
    print 'I am apples!' # the function prints 'I am apples!' without quotes

import MyStuff   # imports the whole module/script   

MyStuff.apple()   # calls the function 'apple' which does nothing but print out the sentence.
print MyStuff.tangerine   # calls module on the variable tangerine under the function 'apple' to print out its little sentence

##  mystuff['apple']  # get the key 'apple' from a dictionary and return its attached value
## MyStuff.apple      # get the function 'apple' from a module and return its designated output value
## MyStuff.tangerine  # get the function 'apple' from a module and return its specified variable's output value

## In the case of the dictionary, the key is a string and the syntax is [key]. In the case of the module, the key is an identifier, and
## the syntax is .key. Other than that they are nearly the same thing.  An identifier, or name, is made up of letters, digits, and 
## underscores, can be any length, and Case MAtters.



