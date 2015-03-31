from sys import argv

script, user_name = argv
prompt = '> '

print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
All right, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

#output:
#16:24:19 c3po ~/Desktop/mystuff/Emacs_Folder> python ex10emacs.py lizbeth
#Hi, lizbeth, I'm the ex10emacs.py script.
#I'd like to ask you a few questions.
#Do you like me lizbeth?
#> sure I do.
#Where do you live lizbeth?
#> durham
#What kind of computer do you have?
#> mac

#All right, so you said 'sure I do.' about liking me.
#You live in 'durham'.  Not sure where that is.
#And you have a 'mac' computer.  Nice.

 
