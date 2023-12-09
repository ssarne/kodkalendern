f = open('2023/dec07.txt', 'r')
lines = f.readlines()

years = {}
for line in lines:
   year = int(line.split(", ")[1])
   number = years.get(year, 0) + 1
   print(year, " = ", number)
   years[year] = number

maxYear = 0
maxNumber = 0
for year in years.keys():
   number = years[year]
   print(year, number)
   if number > maxNumber:
      maxYear = year
      maxNumber = number

print(maxYear, maxNumber)