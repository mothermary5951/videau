def add(a, b):
    sum = a + b
    print "%d + %d" % (a, b)
    return a + b

def subtract(a, b):
    remainder = a - b
    print "%d - %d" % (a, b)
    return a - b

def multiply(a, b):
    product = a * b
    print "%d * %d" % (a, b)
    return a * b

def divide(a, b):
    quotient = a / b
    print "%d / %d" % (a, b)
    return a / b

age = add(60, 3)
height = subtract(72, 10)
weight = multiply(20, 6)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here's a puzzle:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Did I do it right?"
 
