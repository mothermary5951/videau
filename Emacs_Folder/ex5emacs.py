print "Sorted MolProbity Bug Reports"

choice = raw_input ('Enter error type [1-3] : ')
choice = int(choice)


if choice == 1:
    print ("element type")
elif choice == 2:
    print ("endmodl")
elif choice == 3:
    print ("too many cubicles")
else:
    print ("uncommon bug")

#output is:
#Sorted MolProbity Bug Reports
#Enter error type [1-4] : 2
#endmodl

#AND:
#Sorted MolProbity Bug Reports
#Enter error type [1-4] : 0
#uncommon bug


              
