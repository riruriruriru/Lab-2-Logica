import matplotlib.pyplot as plt

def graficar(x,y,names,xlabel,ylabel,title):
	cont = 0
	for variableLinguistica in y:
		plt.plot(x, y[cont], label=names[cont])
		cont = cont + 1
	plt.legend(numpoints=1)
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.title(title)
	plt.show()
	return
