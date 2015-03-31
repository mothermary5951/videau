the_count = [1, 2, 3, 4, 5]   #list of integers
fruits = ['apples', 'oranges', 'pears', 'apricots'] # list of strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # list of both integers and 
                                                        #strings

for number in the_count:  # the items in the_count are named 'number'
    print "%d" % number    

for fruit in fruits:      # the items in fruits are named 'fruit'
    print "Fruit is %s" % fruit

for i in change:           # the items in change are name "i", so the
    print "I got %r." % i  # formatter has to be 'print everything', or  %r

elements = []  # making an empty list

for i in range(0, 6):  # the items in the elements list are named 'i'.
    print "Add %d to the empty list of elements." % i
    elements.append(i) # 'append' is a function that lists know what to do with
                          # 'i' is the range of list items to be added, or 
                          #  appended

for i in elements:
    print "New item in the 'elements' list is %d" % i
