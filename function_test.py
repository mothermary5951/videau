testlist = [2, -4.15, 17, 2.3904, -19.245]  # defintion of list in SQUARE brackets.
print testlist  # Look it over

testlist.insert(0, 36.5)  ## insert 36.5 in list position before o index position.
print testlist  # look at insert

testlist.sort(reverse=True)  ## change from default sort,  most negative to most positive
print testlist


i = len(testlist)  # provides length of list, with new insertion
print i


## The order in which the two methods are run determines whether 'sort' works, or whether it
## returns "none" as its default.


