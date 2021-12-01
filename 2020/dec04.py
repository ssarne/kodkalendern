
import sys

line = open("dec04.txt", "r").readline()
zips = line.split()
zips.sort()
print(zips[476])