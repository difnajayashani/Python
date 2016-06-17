#!/user/bin/python
import csv
from random import randint

#----------------------------------------------------------------------------
def csv_writer(data, path):
	"""
	Write data to a csv file path
	"""
	with open(path, "wb") as csv_file:
		writer= csv.writer(csv_file, delimiter=',')
		writer.writerows(data)

#-------------------------------------------------------------------------------
if __name__ == "__main__":

	#obtain the number of rows
	rows=int(input('Enter the number of rows:'))

	#obtain the number of columns
	columns=int(input('Enter the number of columns:'))

	myArray=[]
	for r in range(0,rows):
		myArray.append([])
		for c in range(0,columns):
			myArray[r].append(randint(0,99))
		
	print myArray

	csv_writer(myArray,"output3.csv")
