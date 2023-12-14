f = open('2023/dec13.txt', 'r')
lines = f.readlines()

expected = 0
for n in range(100, 500):
    expected += n

actual = 0
for line in lines:
    ns = line.split(", ")
    for n in ns:
        actual += int(n)

missing = expected - actual
print(missing)