import time
import datetime

#Variables
start = time.time()
startYear = 1901
endYear = 2000
count = 0

for i in range(startYear, endYear):
    print (i)
    for x in range(1,12+1):
        if datetime.date(i,x,1).weekday() == 0:
            count += 1

print(count)
print ("Time =", time.time()-start, "s")
