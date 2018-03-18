from random import randint 
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')
x , y = [] , []
def get():
	for i in range(10):
		x.append(i)
		y.append(randint(0,20))
	return(x,y)
fig=plt.figure()

## plotting just 1*1 plot
ax1=fig.add_subplot(1,1,1)
x,y=get()
ax1.plot(x,y)
plt.show()


## creating 2  graphs of dimensions 2*1 

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
x,y = [],[]
x,y = get()
ax1.plot(x,y)
x,y = [],[]
x,y = get()
ax2.plot(x,y)
plt.show()

## simlarly creating the graphs for dimensions of 2*1 and two of 2*2
fig=plt.figure()
## fig.add_subplot(x,y,z) 
## where x means tall , y means wide and z is plot number
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,1,2)
x,y = [],[]
x,y = get()
ax1.plot(x,y)
x,y = [],[]
x,y = get()
ax2.plot(x,y)
x,y = [],[]
x,y = get()
ax3.plot(x,y)

plt.show()

## using plt.subplot2grid for subplots

## simple graph of shape (1*1) starting from (0,0)

## divides the plot into 6 parts  and if we use rowspan , colspan
ax1 = plt.subplot2grid((6,6),(0,0),rowspan=4,colspan=6)
x,y = [],[]
x,y = get()
ax1.plot(x,y)
plt.show()

ax1 = plt.subplot2grid((6,6),(0,0),rowspan=2,colspan=6)
x,y = [],[]
x,y = get()
ax1.plot(x,y)
ax2 = plt.subplot2grid((6,6),(4,0),rowspan=3,colspan=6)
x,y = [],[]
x,y = get()
ax2.plot(x,y)
plt.show()

ax1 = plt.subplot2grid((9,6),(0,0), rowspan=2 , colspan=6)
x,y = [],[]
x,y = get()
ax1.plot(x,y)

ax2 = plt.subplot2grid((9,6),(4,0) , rowspan=2 , colspan=6)
x,y = [],[]
x,y = get()
ax2.plot(x,y)

ax3 = plt.subplot2grid((9,6),(7,0) , rowspan=4, colspan=6)
x,y = [],[]
x,y = get()
ax3.plot(x,y)

plt.show()



