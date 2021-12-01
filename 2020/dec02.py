import sys

f = open("dec02.txt", "r")
line = f.readline()
floor = 0
for c in line:
    if c == 'u':
        floor += 1
    elif c == 'n':
        floor -= 1
    else:
        print(c)

print(floor)