"""
Solution to Project Euler Problem 22
"""
import time

start = time.time()
TOTAL = 0
namesList = []


def alphabetic_score(name, list_position):
    """Function that calculates an alphabetic score for a name based on
       ascii value and list position.
    """
    score = 0
    for character in name:
        score += ord(character) - 64
    return score * (list_position + 1)


with open("names.txt", "r") as namesFile:
    data = namesFile.read()

# remove all the formatting surrounding the names
data = data.replace(",", " ")
data = data.replace('"', "")

for single_name in data.split():
    namesList.append(single_name)
namesList.sort()

for index, value in enumerate(namesList):
    TOTAL += alphabetic_score(value, index)
print(TOTAL)

print("Time =", time.time() - start, "s")
