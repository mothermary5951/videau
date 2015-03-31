from sys import argv

script, filename = argv

target = open(filename, 'w')

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

target.write(line1+'\n'+line2+'\n'+line3+'\n')

target.close()










