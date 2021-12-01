
sum = 0
for i in range(10000, 100001):
    if (i % 3767 == 0):
        sum += i

print(len(str(sum)))