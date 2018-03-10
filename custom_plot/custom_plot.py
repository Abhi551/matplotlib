import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import csv 


##	"Everything in matplotlib is customisable just need to find the following arguments or function "

def plot():
	Open = []
	High = []
	Low = []
	Date = []
	Close =[]

	
	## referencing the graph by fig

	fig=plt.figure()
	##defining the subplots
	## there are other ways to plots subplots other subplot2grid
	## subplot2grid(shape,location,rowspan,colspan,fig)
	ax1=plt.subplot2grid((1,1) , (0,0))
	
	## multiple plots using subplot2grid

	#ax2 = plt.subplot2grid((1,1) , (0,0))
	#ax3 = plt.subplot2grid((1,1) , (0,0))
	#ax4 = plt.subplot2grid((1,1) , (0,0))

	## now we use ax1.plot for plotting not plt.plot

	with open('html.csv','r',newline = "") as fobj:
		csv_reader = csv.DictReader(fobj)
		for line in csv_reader:
			num_date = mdates.datestr2num(line['Date'])
			Date.append(num_date)
			Open.append(float(line['Open']))
			Low.append(float(line['Low']))
			Close.append(float(line['Close']))
			High.append(float(line['High']))
	
	## plotting the graph
	ax1.plot_date(Date,Open,'-',color='c',label="Subplot")	
	## rotating the xaxis labels 
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	## using the grid for better visualisation
	ax1.grid(color='r',linestyle='-',lw=2)

	
	plt.legend()
	plt.title("This is subplot")
	plt.xlabel("Dates")
	plt.ylabel("Open")
	## to adjust the subplots in figure
	plt.subplots_adjust(left=.08,bottom=0.15,right=.9,wspace=.2,hspace=.2	)
	plt.show()


if __name__=="__main__":
	plot()
