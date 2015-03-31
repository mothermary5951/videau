pound = 0.4534  # number of pounds per kilogram
inch = 2.54		# number of inches per centimetre

print "My bowling ball weighs %d kilos." % (pound * 8)
print "My umbrella is %d centimetres long." % (inch * 18)

#python returned:
#My bowling ball weighs 3 kilos.
#My umbrella is 45 centimetres long.



kilo = 2.2 # number of pounds per kilo
centimetre = 0.3937 # number centimetres per inch

print "How many kilos do I weigh?"
print "I weigh %d kilos." % (134 / kilo)
print "I am %d centimetres tall." % (51.5 / centimetre)

#Python returned:
#How many kilos do I weigh?
#I weigh 60 kilos.
#I am 130 centimetres tall.


print "How many kilos per pound?", 1 / 2.2 
print "How many centimetres per inch?", 1 / 2.54

#Python returned:
#How many kilos per pound? 0.454545454545
#How many centimetres per inch? 0.393700787402


print 1 / 2.2 #figuring how many kilos per pound
print 1 / 2.54 #figuring how many centimetres per inch

#Python returned:
#0.454545454545
#0.393700787402


PYTHON FORMATTERS:
'd'	Signed integer decimal.	 
'i'	Signed integer decimal.	 
'o'	Signed octal value.	(1)
'u'	Obsolete type – it is identical to 'd'.	(7)
'x'	Signed hexadecimal (lowercase).	(2)
'X'	Signed hexadecimal (uppercase).	(2)
'e'	Floating point exponential format (lowercase).	(3)
'E'	Floating point exponential format (uppercase).	(3)
'f'	Floating point decimal format.	(3)
'F'	Floating point decimal format.	(3)
'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 
		or not less than precision, decimal format otherwise.	(4)
'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 
		or not less than precision, decimal format otherwise.	(4)
'c'	Single character (accepts integer or single character string).	 
'r'	String (converts any Python object using repr()).	(5)
's'	String (converts any Python object using str()).	(6)
'%'	No argument is converted, results in a '%' character in the result.	 


Notes:

1.) The alternate form causes a leading zero ('0') to be inserted between left-hand padding 
		and the formatting of the number if the leading character of the result is not 
		already a zero.

2.) The alternate form causes a leading '0x' or '0X' (depending on whether the 'x' or 'X' format 
		was used) to be inserted between left-hand padding and the formatting of the number 
		if the leading character of the result is not already a zero.

3.) The alternate form causes the result to always contain a decimal point, even if no digits 
		follow it.
	 The precision determines the number of digits after the decimal point and defaults to 6.

4.) The alternate form causes the result to always contain a decimal point, and trailing zeroes 
		are not removed as they would otherwise be.
	 The precision determines the number of significant digits before and after the decimal 
		point and defaults to 6.

5.) The %r conversion was added in Python 2.0.
	The precision determines the maximal number of characters used.

6.) If the object or format provided is a unicode string, the resulting string will also be unicode.
	The precision determines the maximal number of characters used.

 


