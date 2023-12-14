f = open('2023/dec14.txt', 'r')
lines = f.readlines()

for i in range(0, len(lines) - 1):
    prev = lines[i].strip()
    next = lines[i+1].strip()
    outer = int(prev[0]) + int(prev[-1])
    pos = int(len(next) / 2)
    inner = int(next[pos])
    if inner != outer:
        print(i)