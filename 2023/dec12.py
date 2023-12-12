
def getNum(line):
    id = ""
    for c in line:
        cs = "" + c
        if not cs.isdigit:
            id += cs
    return id

f = open('2023/dec12.txt', 'r')
lines = f.readlines()

map = {}
for line in lines:
    id = getNum(line.strip())
    if id in map:
        org = map.pop(id)
    else:
        map[id] = line.strip()

for key in map:
    print(key, map[key])
