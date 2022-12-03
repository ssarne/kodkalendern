
import sys

bilder = str(24 * 60 * 83)
filmer = open("2022/dec03.txt", "r").readlines()
id = 0

for film in filmer:
    if film.strip() == bilder:
        break
    id += 1

print(id)