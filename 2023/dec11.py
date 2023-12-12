
qwerty = "qwertyuiopåasdfghjklöäzxcvbnm"
length = len(qwerty)

def encode(text, shift):
    result = ""
    for c in text:
        pos1 = qwerty.find(c)
        pos2 = (pos1 + shift) % length
        result += qwerty[pos2]
    return result

def decode(text, shift):
    result = ""
    for c in text:
        pos1 = qwerty.find(c)
        pos2 = (pos1 - shift) % length
        result += qwerty[pos2]
    return result

f = open('2023/dec11.txt', 'r')
lines = f.readlines()
antal = 0

for line in lines:
    wish = line.split(", ")
    shift = int(wish[2])
    text = decode(wish[1], shift)

    if (text == 'cykel'):
        antal += 1

print(antal)
