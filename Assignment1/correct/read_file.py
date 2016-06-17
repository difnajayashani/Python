#!/user/bin/python
import csv

# --------------------------------------------------------------------------
def csv_writer(myList, out_file):
	#write to a file the processed data
	wfile = open(out_file, 'wb')
	writer = csv.writer(wfile, delimiter=',')
	writer.writerows(myList)
	wfile.close()


#-------------------------------------------------------------------------------
def csv_reader(in_file):
	#read from file
	rfile = open(in_file, 'rb')
	reader = csv.reader(rfile)
	return reader



#------------------------------------------------------------------------------
if __name__ == "__main__":

	in_file = "output.csv"
	out_file = "processed.csv"

	#read the output.csv file
	reader = csv_reader(in_file)

	myArray = []
	i = 0
	for row in reader:
		res = map(int, row)
		print res
		myList = [i, sum(res), min(res), max(res)]
		print myList
		i = i + 1
		myArray.append(myList)
	print myArray

	#write the result to the processd.csv file
	csv_writer(myArray, out_file)

