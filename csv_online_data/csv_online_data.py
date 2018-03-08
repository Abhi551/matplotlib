import matplotlib.pyplot as plt 
import matplotlib
import numpy as np 
from urllib.request import Request 
from urllib.request import urlopen
import matplotlib.dates as mdates
import csv



def str_date2num(dates):
	return(mdates.datestr2num(dates))

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'


def plot_graph(converted_dates,choice_value,type_graph):
		##plt.plot(converted_dates,choice_value)
		## for plotting date we have different graph named 
		## plot_graph

	## by default graph is plotted in scatter format but to convert in line graph

	plt.plot_date(converted_dates,choice_value,'-',color='r',label="graph with dates")
	
	#print (choice_value[0],converted_dates[0])
	
	plt.xlabel("Dates")
	plt.ylabel(str(type_graph))
	plt.legend()
	#plt.show()
	plt.savefig("my_plot")

	## saving the plot

def func():
	## sending request
	req=Request(stock_price_url)
	try:
		client=urlopen(req)
		client=client.read()
		stock_price_data=client.decode()
	except Exception as e:
		print (e)

	#data=stock_price_data[0:100]
	#print (data.split("\n"))

	stock_price_data=stock_price_data.split("\n")
	print (stock_price_data[1])
	split_line=[]
	for line in stock_price_data:
		split_line.append(line.split(","))
	
	#print (type(split_line[1]))
	#print (split_line[1][2],split_line[1][0])


	#print (split_line)
	with open ('html.csv','w',newline="") as fobj:
		fieldnames=split_line[0]
		csv_writer=csv.DictWriter(fobj,delimiter=",",fieldnames=fieldnames)
		csv_writer.writeheader()
		for i in range(1,len(split_line)):
			csv_writer.writerow({'Date':split_line[i][0],'Open':split_line[i][1],'High':split_line[i][2],
			'Low':split_line[i][3],'Close':split_line[i][4],'Adjusted_close':split_line[i][5],'Volume':split_line[i][6]})
	

	converted_dates=[]
	choice_value=[]


	with open('html.csv','r',newline="") as fobj:
		csv_reader=csv.DictReader(fobj,delimiter=",")
		type_graph=input("Enter your choice of graph from \n1.Open\n2.High\n3.Low\n4.Close\n5.Adjusted_close\n6.Volume\n")
		for row in csv_reader:

			## x-values are rows
			x=(row['Date'])
			## y-values are user provided
			y=float(row[type_graph])
		
			#checking type for a specific value in file 
			#print (type(row[type_graph]))
			# break

			converted_dates.append(str_date2num(x))			## calling str_date2num for converting dates in plot format 
			choice_value.append(y)
			#print (converted_dates)
			#print (y)
			#print (type(y)

			## plotting the graph by calling function plot_graph()

		plot_graph(converted_dates,choice_value,type_graph)






if __name__=="__main__":
	func()
		