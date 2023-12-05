
f = open('2023/dec05.txt', 'r')
lines = f.readlines()

number = 0
for line in lines:
   coins = line.split(", ")
   sum = 192 * int(coins[0]) + 24 * int(coins[1]) + 8 * int(coins[2]) + int(coins[3])
   if sum >= 1000:
      number += 1

print(number)