import csv
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.dates as mdates 
from matplotlib.finance import candlestick_ohlc


'''
read this for understanding the candlestick graphs and how to interpret them
http://forextraininggroup.com/learn-read-forex-candlestick-charts-like-pro/

'''


def plot():
	Open = []
	High = []
	Low = []
	Date = []
	Close =[]
	Vol = []
	ohlc=[]


	
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
			Open.append(float(line['Open']))
			Low.append(float(line['Low']))
			Close.append(float(line['Close']))
			High.append(float(line['High']))
			Vol.append(float(line['Volume']))
	

	Open = np.asarray(Open)
	High = np.asarray(High)
	Low = np.asarray(Low)
	Close = np.asarray(Close)
	Vol = np.asarray(Vol)

	for i in range(50):
		collect=(Date[i],Open[i],High[i],Low[i],Close[i])
		ohlc.append(collect)

	## candlestick accepts 5 or more values to unpack
	## ax1 is the subplot on which this graph is depicted
	## the first argument goes as the x-axis
	candlestick_ohlc(ax1,ohlc,colorup='g',colordown='r')

	for labels in ax1.xaxis.get_ticklabels():
		labels.set_rotation(45)

	## dates are represented in number format of 700 thousand 
	## to convert them into date format 
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	

	plt.subplots_adjust(bottom=.16)
	plt.xlabel('Dates')
	plt.ylabel('Price')
	plt.title("OHLC Finance Graph")
	ax1.plot([],[],label="My Graph",color='r')
	plt.legend()
	plt.show()


if __name__=="__main__":
	plot()




















