import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import csv 
import numpy as np


##	"Everything in matplotlib is customisable just need to find the following arguments or function "

def plot():
	Open = []
	Date = []

	
	## referencing the graph by fig

	fig=plt.figure()
	## multiple plots using subplot2grid
	ax1=plt.subplot2grid((1,1) , (0,0))
	## making grid visible
	ax1.grid(True)


	with open('html.csv','r',newline = "") as fobj:
		csv_reader = csv.DictReader(fobj)
		for line in csv_reader:
			num_date = mdates.datestr2num(line['Date'])
			Date.append(num_date)
			Open.append(float(line['Open']))
	## converting the list to numpy array as they are much better in handling in operation
	Open=np.asarray(Open)
	## plotting the subplots
	ax1.plot_date(Date,Open,'-',color='c',label="Price Graph")

	## rotating the graph
	for labels in ax1.xaxis.get_ticklabels():
		labels.set_rotation(45)

	## setting the color for labels in x-axis and y-axis
	ax1.xaxis.label.set_color('g')
	ax1.yaxis.label.set_color('r')

	## we can set the values we want to see on either of the axis
	ax1.set_yticks(list(range(0,800,50)))

	## filling the graph with color
	## ax1.fill_between(x,y) have 2 necessary arguments in it 
	## ax1.fill_between(Date,Open,Open[0],color='c')
	## we can also fill the color of our choice for every curve below or above a point
	
	ax1.fill_between(Date,Open,Open[0],where=(Open>Open[0]),color='g')
	ax1.fill_between(Date,Open,Open[0],where=(Open<Open[0]),color='r')
	
	## we can't have legends for above or below plots so we use fake plotting
	ax1.plot([],[],label="gain",color='g')
	ax1.plot([],[],label="loss",color="r")
	plt.xlabel("Date")
	plt.ylabel("Open Price")
	plt.subplots_adjust(bottom=.16)
	plt.legend()
	plt.show()




if __name__=="__main__":
	plot()
