## recordings = "jazz, boogie, classical, opera, 33.3, 78, saxophone, piano"

## print recordings

artists = "Basie Calloway Shumann Pavarotti grandmother Presley Wood Chopin"  #  variable is a string

print artists

artists_div = artists.split(' ')  # artists calls split to reformat list as artists_div
print artists_div   #prints out 'artists' with added single quotes and commas
more_artists = ["Warwick", "Holliday", "Plant", "Collins"]  ## list of additional artist list members

while len(artists_div) != 11:  # while-loop that calls len function on artists_div list to measure length
    one_more = more_artists.pop()  ##  variable one_more calls function pop, off the end of list more_artists
    print "Add: ", one_more  ## returns result of popped-off member of list more_artists 
    artists_div.append(one_more) ## calls function append to add popped off member to artists_div list
    print "Now there are %d artists shown." % len(artists_div) # calls len function for final attainment
                                                              # of 11-member list goal in while-loop
print "Here's a new group: ", artists_div  ##  prints out final 11-member list



