def add(a, b):      # This calls a function and gives 2 arguments
    sum = a + b     # Defines sum as a variable equal to the arguments
    print sum       # Use as debugging tool: does the function work as expected
    return sum      # makes sum available if the function is called again

age = add(40, 1)    # uses the function

print "sum = %d" % (age)  # uses the "return" command
