from random import randint
import csv

myArray=[]

#generate a list of lists
for r in range(0,3):
	myArray.append([])
	for c in range(0,4):
		#print(randint(0,9))
		myArray[r].append(randint(0,99))
print myArray

with open("output2.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(myArray)
		
