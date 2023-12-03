
f = open('2023/dec02.txt', 'r')
lines = f.readlines()

n = 0
for line in lines:
    uns = int(line)
    grams = uns * 28
    if (grams >= 2000 and grams <= 3000):
        n += 1

print(n)