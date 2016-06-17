#!/user/bin/python
import csv

#read from file
rfile=open('input.csv','rb')
reader= csv.reader(rfile)


wfile=open('output.csv','wb')
writer=csv.writer(wfile,delimiter=',', quoting=csv.QUOTE_ALL)

for row in reader:
	writer.writerow(row)

rfile.close()
wfile.close()

