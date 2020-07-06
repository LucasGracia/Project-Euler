#A program to calculate the alphabetical value of a list of names multiplied
#by it's position in the list.
import time

#Variables
start = time.time()
total = 0
namesList = []

#Function that calculates an alphabetic score for a name
#based on ascii value and list position
def alphabeticScore(name, listPosition):
    alphabeticScore = 0
    for character in name:
        alphabeticScore += (ord(character) - 64)
    return alphabeticScore * (listPosition + 1)

#Read the contents of the name file into data variable
with open('names.txt', 'r') as namesFile:
    data = namesFile.read()

#remove all the formatting surrounding the names
data = data.replace(',',' ')
data = data.replace('"','')
#add each name into a list
for name in data.split():
    namesList.append(name)
#sort the names alphabetically
namesList.sort()
#calclate the alphabetic score for each name and add it to the total
for i in range(len(namesList)):
    total += alphabeticScore(namesList[i], i)
print(total)

print ("Time =", time.time()-start, "s")
