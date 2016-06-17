#!/user/bin/python
import csv


#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
	in_file= 'OPTPF.csv'
	out_file='filtered.csv'
	#read from file
	rfile=open(in_file,'rb')
	reader= csv.reader(rfile,delimiter='|')

	#open the file to write 
	writer =csv.writer(open(out_file,'wb'))

	my_list=[]
	for row in reader:
		my_list = [row[0],row[1],row[3],row[8]]
		print my_list
		writer.writerow(my_list)
	rfile.close()		
#--------------------------------------------------------------------------------------------  
 
