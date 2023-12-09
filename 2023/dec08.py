
f = open('2023/dec08.txt', 'r')
lines = f.readlines()

prev = 0
for line in lines:
    rooms = line.split(", ")
    balls = 0
    for room in rooms: 
        balls += int(room)
    if (balls < prev):
        print(prev)
        break
    prev = balls
