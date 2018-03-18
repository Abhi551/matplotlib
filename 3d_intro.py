from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def func():

	fig = plt.figure()

	ax1 = fig.add_subplot(111 , projection = '3d')

	x = list(range(10))
	y = [i**2 for i in x]
	z = [i**3 for i in x]
	print (x,y,z)

	ax1.plot_wireframe(x,y,z , label="3D")

	## setring labels for axis is bit differ
	ax1.set_xlabel('x-axis')
	ax1.set_ylabel('y-axis')
	ax1.set_zlabel('z-axis')

	plt.legend()
	plt.show()



## 3D scatter plots


from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

def func1():

	style.use('ggplot')
	fig = plt.figure()

	ax2 = fig.add_subplot(111 , projection = '3d')

	x = list(range(10))
	y = [i**2 for i in x]
	z = [i**3 for i in x]

	ax2.plot_wireframe(x,y,z , color = 'r' , label ="-")

	x = list(range(10))
	y = [i**2*2+5 for i in x]
	z = [i*3+9for i in x]
	ax2.scatter(x,y,z , color ='g' , label = '+')

	x = [-i for i in x]
	y = [i*3-9 for i in y]
	z = [-i*5+5 for i in z]

	ax2.set_xlabel('x-axis')
	ax2.set_ylabel('y-axis')
	ax2.set_zlabel('z-axis')
	ax2.scatter(x,y,z , color='r' , label = '-')

	plt.legend()
	plt.show()

func()
func1()

