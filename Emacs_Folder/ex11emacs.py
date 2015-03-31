from sys import argv

script, job, user_surname = argv
prompt = '*->*'

print "Hi %s, I'm the %s script." % (user_surname, script)
print "Do you like me %s" % (user_surname)
likes = raw_input(prompt)

print "Tell me %s, what is your work as a %s?" % (user_surname, job)
work = raw_input(prompt)

print "Will being a %s make you rich?" % (job)
rich = raw_input(prompt)

print """
Well then, you've said %r about liking me.
You do %r in your work. Sounds like a fun job.
And here's what you think about your work making you rich: %r
Nice.""" % (likes, work, rich)

 
