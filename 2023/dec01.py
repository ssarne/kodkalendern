# 
# Vad är tomtens telefonnummer?
# Beräkna summan av alla tal mellan 127 och 267 (inklusive både 127 och 267) 
# adderat med summan av alla tal mellan 1110 och 1378 (inklusive både 1110 och 1378) 
# adderat med summan av alla tal mellan 3239293 och 3239330 (inklusive både 3239293 och 3239330).
# 

sum = 0

for i in range(127, 267+1):
    sum += i

for i in range(1110, 1378+1):
    sum += i

for i in range(3239293, 3239330+1):
    sum += i

print(sum)