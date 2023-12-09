
f = open('2023/dec09.txt', 'r')
sky = f.readline()

sky = sky.replace("/*", "")
sky = sky.replace("€", "")
sky = sky.replace("*U", "")
sky = sky.replace("-", "")
print(len(sky))