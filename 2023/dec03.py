
f = open('2023/dec03.txt', 'r')
lines = f.readlines()

sum = 0
for line in lines:
   sum += int(line)
avg = sum / len(lines)

m = 0
for line in lines:
    if int(line) == avg:
        m += 1

print(m)
