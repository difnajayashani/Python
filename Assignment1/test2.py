#!/usr/bin/python
import csv
import sys


if __name__ == "__main__":

	f = open(sys.argv[1],'rb')

	try:
		reader=csv.reader(f)
		for row in reader:
			print row

	finally:
		f.close

