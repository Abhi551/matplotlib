import matplotlib.pyplot as plt 
import numpy as np 
import csv 
import matplotlib.dates as mdates
from matplotlib import style




## using different style in matplotlib

def plot():
	Low = []
	High = []
	Date = []

	## give the names  styles we have
	print (style.available)
	## we can use any of the style using style.use
	## we have the option of creating the plot of our own customization
	style.use('ggplot')
	#style.use('bmh')
	#style.use('fivethirtyeight')
	
	## referencing the graph by fig

	fig=plt.figure()
	##defining the subplots
	## there are other ways to plots subplots other subplot2grid
	## subplot2grid(shape,location,rowspan,colspan,fig)
	ax1=plt.subplot2grid((1,1) , (0,0))


	## now we use ax1.plot for plotting not plt.plot

	with open('html.csv','r',newline = "") as fobj:
		csv_reader = csv.DictReader(fobj)
		for line in csv_reader:
			num_date = mdates.datestr2num(line['Date'])
			Date.append(num_date)
			High.append(float(line['High']))
			Low.append(float(line['Low']))

	
	## plotting the graph
	ax1.plot_date(Date,Low,'-',label="Low")
	ax1.plot_date(Date,High,'-',label="High")	
	## rotating the xaxis labels 
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	## using the grid for better visualisation
	#ax1.grid(color='r',linestyle='-',lw=2)

	
	plt.legend()
	plt.title("This is subplot")
	plt.xlabel("Dates")
	plt.ylabel("Open")
	## to adjust the subplots in figure
	plt.subplots_adjust(left=.08,bottom=0.15,right=.9,wspace=.2,hspace=.2	)
	plt.show()


if __name__=="__main__":
	plot()
