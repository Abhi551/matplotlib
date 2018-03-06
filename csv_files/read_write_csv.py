## reading and writting the csv files using csv module
## comma separated values  

import csv

## while reading or writting csv Files it better to include newline='' in file object , since csv module does 
## its own newline handling if not specified  , newlines embeded inside quoted fields will not be interpreted correctly

#file_name=input("enter the file name : ")
try:
	with open('new.csv','r',newline='') as fobj:
		csv_reader=csv.reader(fobj,delimiter="\t")
		## to skip the first values i.e. header
		for line in csv_reader:
			print (line[0])
	fobj.close()
except Exception as e:
	print (e)
with open('new.csv','r',newline='') as f:
	csv_read=csv.reader(f,delimiter=',')
	with open('write.txt','w',newline="") as fobj:
		## new csv file created have quotes(" ") around some values , which have "-" in them
		## so as to differ in between delimiter ("-") and string ("-")
		csv_write=csv.writer(fobj,delimiter='-')
		for line in csv_read:
			csv_write.writerow(line)
	fobj.close()
f.close()
## using another delimiter
with open('new.csv','r',newline="") as fobj:
	csv_reader=csv.reader(fobj,delimiter=',')
	with open('new.txt','w',newline="") as f:
		csv_write=csv.writer(f,delimiter='\t')
		for line in csv_reader:
			csv_write.writerow(line)
	f.close()
fobj.close()

## to read the new file created "new.txt" we now change the delmiter from default to '\t'

with open("new.txt",'r',newline='') as fobj:
	#csv_reader=csv.reader(fobj,delimiter=',')
	csv_reader=csv.reader(fobj,delimiter='\t')
	for line in csv_reader:
		print (line)

fobj.close()
## a more subtle way to handle csv files
## using DictReader and DictWriter


## DictReader returns an ordered dictionary 
with open("new.txt",'r',newline="") as fobj:
	csv_reader=csv.DictReader(fobj,delimiter="\t")
	for line in csv_reader:
		print (line)
		## we can access any record using key-value pair

fobj.close()


## DictWriter  to write the file in ordered dict format

with open('new.txt','r',newline="") as fobj:
	csv_reader=csv.DictReader(fobj,delimiter="\t")
	with open("New_dict.txt",'w',newline="") as f:

		## specifying the header of file
		fieldnames=["first_name","last_name"]
		csv_writer=csv.DictWriter(f,delimiter=",",fieldnames=fieldnames)

		## writes the header of file 
		csv_writer.writeheader()
		for line in csv_reader:
			## removing the email column from the file
			del(line["email"])
			csv_writer.writerow(line)
	f.close()
fobj.close()

