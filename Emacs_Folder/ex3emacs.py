# escape sequences ("\\", "\'", "\n", "\t", etc.) are ways to change python's
          # default behavior.
# formatters are just that: they format output.  """ print it all the way it
# it is entered, %s prettier output, %r output exactly like the input, %d used for numbers

# correct output for print "%r" %x and print "%r" %y:
#'\nSteven\nBradley\nJane\nSwati\\Nt* {Gary}\nChristopher\\Nt* {Jeff}'
#'\nAll none-indented names are still here.\nAll indented names are elsewhere.
#\nWho will stay?\nWho will go?\n'

#correct output for print "%s" %x and print "%s" %y (see below):
Steven
Bradley
Jane
Swati
* Gary
Christopher
* Jeff

All none-indented names are still here.
All indented names are elsewhere.
Who will stay?
Who will go?


x = "\nSteven\nBradley\nJane\nSwati\n\t* Gary\nChristopher\n\t* Jeff"
y = """
All none-indented names are still here.
All indented names are elsewhere.
Who will stay?
Who will go?
"""

print "%s" %x
print "%s" %y



 




 

