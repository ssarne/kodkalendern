
a = 1
b = 1

for i in range (1, 101):
    a *= i

for i in range (2, 165, 2):
    b *= i

c = a / b

print (round(c))