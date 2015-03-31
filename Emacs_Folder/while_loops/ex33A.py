i = 0
numbers = []

print "What is the endpoint? "

x = raw_input()  #The int function can also wrap: int(raw-input())


while i < int(x):  #If the int function wraps raw_input(), then x is left x
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num




 
