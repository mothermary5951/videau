people = 30
cars = 40
trucks = 15

if cars >= people and trucks < cars:
    print  "Do we have more cars than trucks?"
if cars >= people and trucks <= cars:
    print "Do we have more people than trucks?"
if cars >= people and trucks != cars:
    print "What happens now?"

if cars != people and trucks <= people:
    print "We can take either cars or trucks on this trip."
else:
    print "Let's not go."

