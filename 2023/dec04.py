
f = open('2023/dec04.txt', 'r')
lines = f.readlines()

target = 106023
bestPos = 0
bestDist = target

for line in lines:
   pos = int(line)
   dist = abs(pos - target)
   
   if dist < bestDist:
      dist = abs(pos - target)
      bestPos = pos
      bestDist = dist

print(bestPos)

