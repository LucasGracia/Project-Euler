import time

#Variables
start = time.time()
amicableNumbers = []

#A function to produce the sum of the factors of a number
def factorsSum(number):
    factorList = []
    for i in range(1,int((number+1)/2)):
        if number % i == 0:
            #i is a factor of number
            factorList.append(i)
    return sum(factorList)

def isAmicablePair(x,y):
    if factorsSum(x) == y and factorsSum(y) == x:
        return True
    else:
        return False

for i in range(2,10000+1):
    for j in range(2, 10000+1):
        if i != j:
            if isAmicablePair(i, j) == True:
                amicableNumbers.append(i)
                amicableNumbers.append(j)

print(sum(set(amicableNumbers)))
print ("Time =", time.time()-start, "s")
