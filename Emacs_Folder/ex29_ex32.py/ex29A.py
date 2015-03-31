people = 20
cats = 30
dogs = 15

if not(people < cats and cats < dogs):
    print "True!"

if (people != cats or people == dogs):
    print "True!"

if not((dogs + cats == 0)  and  (people - dogs <= cats)):
    print "True!"

