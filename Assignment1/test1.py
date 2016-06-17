#!/usr/bin/python
import csv

if __name__ == "__main__":

	f=open('output.csv','rb')
	reader= csv.reader(f)
	
	for row in reader:
		print row
