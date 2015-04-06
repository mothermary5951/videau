a=[1,2,3]
a.remove(2)  # remove removes the first matching value, not an index!
print a

b=[4,5,6]    # indices are numbered 0,1,2,, etc.
del b[1]    # del removes a selected index, in this case '4', index #1.
print b

c= [7,8,9]
print c.pop(0)  # pop returns only a selected index, here '7', index #0.
print c

d = [0,3,3,5,6]  #remove deals with values, not indices!
d.remove(3)  #  values have to use parens not square brackets.
print d

e = [6,5,3,3,0]
del e[1]     # del removes a selected index, in this case '5', index #1.
print e

f = [7,8,9,10]
print f.pop(1)  #pop returns only the selected index
print f        # this is a way to see the list without the popped list member.



