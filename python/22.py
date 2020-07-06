"""
Solution to Project Euler Problem 22
"""
import time

start = time.time()
total = 0
namesList = []


def alphabeticScore(name, listPosition):
    """Function that calculates an alphabetic score for a name based on
       ascii value and list position.
    """
    alphabeticScore = 0
    for character in name:
        alphabeticScore += (ord(character) - 64)
    return alphabeticScore * (listPosition + 1)


with open('names.txt', 'r') as namesFile:
    data = namesFile.read()

# remove all the formatting surrounding the names
data = data.replace(',', ' ')
data = data.replace('"', '')

for name in data.split():
    namesList.append(name)
namesList.sort()

for i in range(len(namesList)):
    total += alphabeticScore(namesList[i], i)
print(total)

print ("Time =", time.time()-start, "s")
