titles = 'PDBid,resolution,protein type,Cys pair resnums,rotamer types,Ca-Ca distance'

headers = titles.split(',') 
print "Here are the proposed header titles:"
for e in headers:

    print e

protein_info = titles.split(',')[:3]  ## The 'split' format Must be done again, and the indices can be stacked behind. 0 start point
print "Here are the protein-related headers:"            ## can justbe left off, so instead of [0:3] we can use [:3].
for e in protein_info:              ## indices can also follow 'protein_info' here, instead of above, but above is cleaner.

    print e

disulfide_info = titles.split(',')[3:]  # Same as above, but leaving off the 6 will make it go to the end.
print "Here are the disulfide-related headers:"
for e in disulfide_info:
    
    print e





