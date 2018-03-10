import csv
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.dates as mdates 
from matplotlib.finance import candlestick_ohlc
from matplotlib import style

'''
read this for understanding the candlestick graphs and how to interpret them
http://forextraininggroup.com/learn-read-forex-candlestick-charts-like-pro/

'''


def plot():

	style.use('fivethirtyeight')

	Open = []
	High = []
	Low = []
	Date = []
	Close = []
	Vol = []
	ohlc = []



	fig=plt.figure()
	##defining the subplots
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

	for i in range(30):
		collect=(Date[i],Open[i],High[i],Low[i],Close[i])
		ohlc.append(collect)


	## candlestick accepts 5 or more values to unpack
	## ax1 is the subplot on which this graph is depicted
	## the first argument goes as the x-axis
	candlestick_ohlc(ax1,ohlc,colorup='g',colordown='r')

	for labels in ax1.xaxis.get_ticklabels():
		labels.set_rotation(45)

	## this is used to set the text Price and its size to be 30
	## in the graph
	## ax1.text(x,y,text="",fontdict)
	## we can also edit the font style of the text using fontdict
	## fontdict(family,stylem,size,color)
	font_dict={'style' : 'italic' ,'size' : 25 , 'color' : 'grey' , 'family' : 'serif'}
	ax1.text(Date[10],High[10],"Price",fontdict=font_dict)

	## dates are represented in number format of 700 thousand 
	## to convert them into date format 
	## annotate(text , (coordinates where to point) , (coordinates to text),textcoords=type,arrowprops)
	ax1.annotate("This",(Date[20],High[20]),xytext=(.6 , .7) ,
					textcoords=('axes fraction'),arrowprops=dict(facecolor='grey',color='grey'))

	#ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	

	## anotating the last price in ohlc graph
	## we sometimes need to show the last price in our graph so
	
	## we generally use Close[-1] and Date[-1] for last entry but here this doesn't work so we find out the 
	## last price and date after that plotted them on graph

	## defining the property of box here
	bbox_props={'boxstyle':'larrow','facecolor':'grey','edgecolor':'grey','linewidth':1}
	ax1.annotate(str(Close[0]),(Date[0],Close[0]),xytext=(Date[0]+5,Close[0]),
				bbox=bbox_props)




	plt.subplots_adjust(left=.11,bottom=.16,right=.9)
	plt.xlabel('Dates')
	plt.ylabel('Price')
	plt.title("OHLC Finance Graph")
	ax1.plot([],[],label="My Graph",color='r')
	plt.legend()
	plt.show()


if __name__=="__main__":
	plot()


