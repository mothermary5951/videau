from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read();out_file = open(to_file, 'w');out_file.write(indata)
#Now I should try to trim this script down even farther!
