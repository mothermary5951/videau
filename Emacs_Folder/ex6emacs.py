#! /usr/bin/python

print "What is your name?",
name = raw_input()
print "What are your goals?",
goals = raw_input(""" """)
print "Do you like to eat? Enter yes or no",
eat = raw_input()
#print name
#print goals
#print eat

# True =  "yes"
# False = "no"
# if True
# print "Do you want a job?"
# if False
# print "Thanks so much! Bye!"

if eat == "yes":
    print "Do you want a job?"
elif eat == "no":
    print "Thanks so much! Bye!"
else:
    print "Thanks for nothing!  Bye!"


