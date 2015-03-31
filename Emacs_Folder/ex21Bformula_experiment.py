def add(a, b):
    sum = a + b
    print "Adding %d + %d" % (a, b)
    return a + b

def divide(c, d):
    quotient = c / d
    print "Dividing %d / %d" % (c, d)
    return c / d

def multiply(e, f):     # e = c / d, which is IQ divided by mood               
    product  = e * f   #product = IQ divided by mood, then multiplied by weight
    print "Multiplying %d * %d" % (e, f)
    return e * f

def subtract(g, h):
    h = a + b
    g = e * f
    answer = g - h
    print "Subtracting %d - %d" % (g - h)
    return g - h

t = add(30, 5)
w = subtract(78, 4)
x = multiply(90, 2)
y = divide(100, 2)
z = multiply(2, 1)

age = t
height = w
weight = x
IQ = y
mood = z


print "Age: %d, Height: %d, Weight: %d, IQ %d, Mood %d" % (t, w, x, y, z)

print "Now let's see what happens: Age + Height - ((IQ / Mood) * Weight)"

what = t + w - ((y / z) * x)

print "That becomes: ", what, "Did I do it right?"
