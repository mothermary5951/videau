def rotamer_category(secondary_structure, dihedral_angle, res_num):
    print "The rotamer is in %s structure." % secondary_structure
    print "The dihedral angle is %d degrees." % dihedral_angle
    print "The amino acid sequence number is %d." % res_num
    print "What a lovely little function this is!\n"
 
print "We can just give the function info directly:"
rotamer_category('beta', 32, 127)

print "OR, we can use variables from our script:"
helix_sheet = 'alpha'
N_CA_C_N = 40
seq_num = 215

rotamer_category(helix_sheet, N_CA_C_N, seq_num)

print "We can even do math inside!"
rotamer_category('none', 360 - 32.0 / 15, 428 - 19 + 12)

print "We can use user input for the arguments:"
print "What is the secondary structure environment?",
secondary_structure = raw_input()
print "What is the dihedral angle?",
dihedral_angle = raw_input()
print "What is the sequence number?",
res_num = raw_input()
print "So, the secondary structure is %d, the dihedral is %d, and the residue number is %d." % (secondary_structure, dihedral_angle, res_num)


 
