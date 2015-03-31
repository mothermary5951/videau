def add(a, b):
    sum = a + b
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(c, d):
    remainder = c - d
    print "SUBTRACTING %d - %d" % (c, d)
    return c - d

def multiply(e, f):
    product = e * f
    print "MULTIPLYING %d * %d" % (e, f)
    return e * f

def divide(g, h):
    quotient = g / h
    print "DIVIDING %d / %d" % (g, h)
    return g / h

what = subtract(add(90,9), (subtract(30,40), (divide(divide(4, 2), divide(1, 1)), multiply(3, 3))))


print what
