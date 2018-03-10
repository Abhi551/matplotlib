import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import csv 
import datetime
import numpy as np



def plot():
	Open = []
	Date = []
	U_date = []
	## referencing the graph by fig

	
	fig=plt.figure()
	## now we use ax1.plot for plotting not plt.plot
	ax1=plt.subplot2grid((1,1),(0,0))

	with open('html.csv','r',newline = "") as fobj:
		csv_reader = csv.DictReader(fobj)
		for line in csv_reader:
			conv_date=line['Date'].split('-')
			conv_date=tuple([int(i) for i in conv_date])
			Date.append(conv_date)
			Open.append(float(line['Open']))
		## converting the date time in unix time
		for i in range(len(Date)):
			U_date.append((datetime.datetime(Date[i][0],Date[i][1],Date[i][2]).timestamp()))

	d=np.vectorize(datetime.datetime.fromtimestamp)
	new_date=d(U_date)

	ax1.plot_date(new_date,Open,'-',label="Unix Time Graph",color='c')
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	
	plt.xlabel(" Date")
	plt.ylabel("Open")
	plt.legend()
	plt.title("Unix Time Graph")
	plt.show()


if __name__=="__main__":
	plot()
