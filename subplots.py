import matplotlib.pyplot as plt 


## using add_subplots 
fig=plt.figure()
income = [3.2, 4.1, 5.0 ,5.6];
outgo = [2.5, 4.0, 3.35 ,4.9];
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.plot(list(range(4)),income)
ax2.plot(list(range(4)),outgo)
plt.show()

x = list(range(1,6))
y = [i**2 for i in range(1,6)]
fig = plt.figure()

## making multiple subplots using add_subplot()

## add_subplot(2,2,1) means a 2*2 grid and First subplot 
## simlarly we can have (2,2,2) , (2,2,3) , (2,2,4) and second , third ,fourth plot
## 2*2 grid

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

## this gives symmetrical result in terms of graph
## plotting multiple graphs

ax1.plot(x,y,'-',color='c')
ax2.scatter(x,y,color='r')
ax3.bar(x,y)
ax4.hist(y,x,histtype='bar')

plt.show()

fig=plt.figure()
## to make unsymmetrical graphs 
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,4)
ax1.plot(x,y,'-')
ax2.scatter(x,y,color='c')
ax3.bar(x,y,color='r')

plt.show()

