## csv files can also  be read by pandas module

import pandas as pd 
import numpy as np 



## use read_csv to read the csv_file
## we can specify the delimiter the csv_file as well

df=pd.read_csv('stock.csv',delimiter=",")
print (df)


## csv with no headers
## by default headers are used in the dataframe


df=pd.read_csv('stock.csv',delimiter=",",header=None)
print (df)



## removing the 1st row of csv 
## using skiprows skips the 1st row and now we read from 2nd row
## but we dont have header of your own choice 
## to include the headers of our own choice use 
df=pd.read_csv('stock.csv',delimiter=",",skiprows=1
	,header=None,names=list('abcde'))
print (df)




## we can set index column as one of the column of data 
## using index_col

## single index column
df=pd.read_csv('stock.csv',delimiter=",",skiprows=None,index_col='people')
print (df)

##multiple index columns
df=pd.read_csv('stock.csv',delimiter=",",skiprows=None,index_col=['people','tickers'])
print (df)




## passing the header of our own choice in csv files
df=pd.read_csv('stock.csv',delimiter=",",header=None,
	names=['a','b','c','d','e'],index_col=None)
print (df)



## Dealing with n.a. values in pandas

df=pd.read_csv('stock.csv',delimiter=",",skiprows=None,na_values=['n.a.',"not available"])
print (df)

## if we want to change values that are absurbd column wisr pass using them as dictionary

df=pd.read_csv('stock.csv',delimiter=",",skiprows=None,na_values={
	'people':['n.a.',"not available"],
	'eps':['n.a.','not available'],
	'revenue':['n.a.','not available',-1]
	},index_col='tickers')

print (df)



## parsing dataframne in csv file
## use to_csv 
df=pd.read_csv('stock.csv',delimiter=",")


## writting a new csv file
#df.to_csv("new_stock.csv",delimiter=",")

## file with no header
df.to_csv("new_stock.csv",delimiter=",",header=None) 

print (df.columns)
## skiping the columns while parsing
df.to_csv("new_stock.csv",delimiter=",",columns= ['tickers','eps'])