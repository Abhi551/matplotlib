import matplotlib.pyplot as plt 
import numpy as np 
import csv 
from random import randint


## 1. using csv module

## creating a file in csv format with 50 random values in it

with open("plot.csv",'w',newline="") as fobj:
	fields=['x','y']
	csv_writer=csv.DictWriter(fobj,delimiter=",",fieldnames=fields)
	csv_writer.writeheader()
	for i in range(50):
		csv_writer.writerow({'x':randint(1,50),'y':randint(1,50)})
fobj.close()

## reading theses values and appending them into a list

x,y=[],[]
with open("plot.csv",'r',newline="") as fobj:
	csv_reader=csv.DictReader(fobj,delimiter=",")
	for line in csv_reader:
		x.append(int(line['x']))
		y.append(int(line['y']))
fobj.close()


plt.scatter(x,y,color="r",label="simple")
plt.xlabel("x-points")
plt.ylabel("y-points")
plt.title("My scatter plot")
plt.legend()
plt.show()


# using numpy to extract the values from file
import numpy as np

## values inside the file to be read should be integers only

## skiprows to skip the number rows in the begining
## usecols uses the columns with index as specified that too in order
try :
	x,y=np.loadtxt('int_plot.csv',delimiter=",",usecols=(0,1),unpack=True,skiprows=1)
except Exception as e:
	print (e)

print (x,y)
plt.plot(x,y,color='g',label="using numpy")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

try:
	x,y=np.loadtxt("int_plot.csv",delimiter=",",unpack=True,usecols=(1,0),skiprows=1)
except Exception as e:
	print (e)
print (x,y)
plt.plot(x,y,color="r",label="Change cols")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
## more about np.loadtxt
 
from io import StringIO
c=StringIO("0,1\n2,3")
x,y=np.loadtxt(c,unpack=True,delimiter=",",usecols=(1,0))
print (x,y)