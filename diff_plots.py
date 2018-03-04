import matplotlib.pyplot as plt
from random import randint
##Entering the label for each graph

## linegraph

plt.plot([1,2,3],[7,5,10],label="first",color='r')
plt.plot([1,2,3],[4,5,6],label="second",color='c')

##plotting the label for axis
plt.xlabel("x-axis")
plt.ylabel('y-axis')

plt.legend()

##naming the title of graph
plt.title("graph\nHey")

plt.show()



##plotting the bar graphs

## bar graph 1
y=[randint(1,20) for i in range(10)]
x=range(10)
plt.bar(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("A bar graph")
plt.show()

## bar graph 2
y=[randint(1,130) for i in range(40)]
x=range(len(y))
#x=[y.count(i) for i in y]
print (y)
print (x)
plt.xlabel("ids")
plt.ylabel("ages")
plt.bar(x,y)
plt.title("age bar graph")
plt.show()



## histogram
values=[randint(1,130) for i in range(50)]
bins=list(range(0,140,10))
print (values)
print (bins)
plt.xlabel("bins")
plt.ylabel("ages")
plt.hist(values,bins,histtype="bar",label="histo",rwidth=.6,color='c')
plt.legend()
plt.show()


## scatter plots
y_values=[randint(1,30) for i in range(10)]
x_values=list(range(10))

print (x_values,y_values)
plt.scatter(x_values,y_values,label="marker",s=200,marker='o',color='c')
plt.xlabel("x axis")
plt.ylabel('y axis')
plt.title("Scatter plots")
plt.legend()
plt.show()


## stack plots

days=list(range(7))
print (days)
pct_work=[randint(10,50) for i in range(7)]
pct_eat=[randint(10,20) for i in range(7)]
pct_play=[randint(15,30) for i in range(7)]
pct_sleep=[100-pct_work[i]-pct_play[i]-pct_eat[i] for i in range(7)]
print (pct_work,pct_eat,pct_play,pct_sleep)
plt.plot([],[],label='pct_work',color='r',linewidth=2.0)
plt.plot([],[],label='pct_sleep',color='c',linewidth=2.0)
plt.plot([],[],label='pct_play',color='g',linewidth=2.0)
plt.plot([],[],label='pct_eat',color='b',linewidth=2.0)
plt.legend()
plt.stackplot(days,pct_work,pct_sleep,pct_play,pct_eat,colors=['r','c','g','b'])
plt.xlabel("days")
plt.ylabel("distribution in %")
plt.title("My stackplot")
plt.show()


## pie charts

pct_work=randint(25,40)
pct_play=randint(10,20)
pct_eat=randint(10,15)
pct_sleep=100-pct_eat-pct_work-pct_play
plt.pie([pct_sleep,pct_eat,pct_work,pct_play],
        labels=['sleep','eat','work','play'],
        colors=['c','m','r','g'],
        startangle=90,
        shadow=True,
        explode=[0,.1,0,0],autopct="%1.1f%%")
plt.show()