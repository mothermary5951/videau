print 
x = int(raw_input("> "))
y = int(raw_input("> "))
try:  result = x / y  ## or w/o raw_input() as int, you need int(x) / int(y)
except ZeroDivisionError:
    print "Division by zero!"
else:
    print "result is", result
finally:
    print "executing finally clause"

while True:
    try:               # the variable x = can go on the same line as 'try:'
        x = int(raw_input("Please enter a number: ")) #or indented on the next.
        break  #  without this break, an open loop is set up!!!!
    except ValueError:
        print "Not a valid number.  Try again, please."

try:  result = int(x) / int(y) # This script produces no output w/o raw_input()
except ZeroDivisionError:
    print "Division by zero!"
else:
    print "result is", result
finally:
    print "executing finally clause"



## NOTE:  raw_input() is ALWAYS ALWAYS ALWAYS A STRING!!!!! 
##  Unless int(raw_input("Please enter a number: "))
