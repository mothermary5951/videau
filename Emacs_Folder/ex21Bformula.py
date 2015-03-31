def add(a, b):
    sum = a + b
    print "Adding %d + %d" % (a, b)
    return a + b

def divide(d, e):
    quotient = d / e
    print "Dividing %d / %d" % (d, e)
    return d / e

def multiply(f, c):     # f = d / e, which is IQ divided by mood
    f = d / e
    product  = f * c   #product = IQ divided by mood, then multiplied by weight
    print "Multiplying %d * %d" % (f, c)
    return f * c

def subtract(h, g):
    h = sum
    g = product
    answer = h - g
    print "Subtracting %d - %d" % (h - g)
    return h - g
    
a = 35
b = 74    
c = 180
d = 50
e = 2

age = a
height = b
weight = c
IQ = d
mood = e
    

print "Age: %d, Height: %d, Weight: %d, IQ %d, Mood %d" % (a, b, c, d, e) 

print "Now let's see what happens: Age + Height - ((IQ / Mood) * Weight)"

what = a + b - ((d / e) * c)

print "That becomes: ", what, "Did I do it right?"

 
