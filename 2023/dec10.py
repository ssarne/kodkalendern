
f = open('2023/dec10.txt', 'r')
lines = f.readlines()

for line in lines:
    address = line.split(" ")
    if len(address) == 2 and len(address[0]) == 8:
        print(address[0])
