from sys import argv

script, filename = argv

file = open(filename, 'w')

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

file.write(line1 + '\n')
file.write(line2 + '\n')
file.write(line3 + '\n')

file.close()

#NOTE:  using "file.write" instead of "target.write" saves the input text!!≈
