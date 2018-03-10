import matplotlib.pyplot as plt 
from matplotlib import style 
## using live graph using animation
import csv
import matplotlib.animation as animation
import matplotlib.pyplot as plt 

style.use('fivethirtyeight')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
def get(i):
	x = []
	y = []
	with open('new.txt','r',newline="") as fobj:
		csv_reader=csv.DictReader(fobj,delimiter=",",fieldnames=['a','b'])
		for line in csv_reader:
			if len(line)>1:		##checking for empty lines
				x.append(line['a'])
				y.append(line['b'])

	x = x[1:]
	y = y[1:]
	ax1.plot(x,y)
## animation function for showing dynamic changes in graph and interval in given in milliseconds
## fig is the reference to figure and get is the function which plots the graph	
animate_graph=animation.FuncAnimation(fig,get,interval=1000)
## any changes that are made in txt file will be displayed in graph
plt.show()
