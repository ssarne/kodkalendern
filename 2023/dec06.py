
f = open('2023/dec06.txt', 'r')
lines = f.readlines()

presents = 0
for line in lines:
   presents += int(line.split(" ")[1])

print(presents)