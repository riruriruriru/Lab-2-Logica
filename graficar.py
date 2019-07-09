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


def graficarGrid(x1,x2,x3,x4,y1,y2,y3,y4,names,xlabel,ylabel,title):
	f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
	cont = 0
	for variableLinguistica in y1:
		ax1.plot(x1, y1[cont], label=names[cont])
		cont = cont + 1
	cont = 0
	ax1.set_ylabel(ylabel[0])
	ax1.set_xlabel(xlabel[0])
	for variableLinguistica in y2:
		ax2.plot(x2, y2[cont], label=names[cont])
		cont = cont + 1
	cont = 0
	ax2.set_ylabel(ylabel[1])
	ax2.set_xlabel(xlabel[1])
	for variableLinguistica in y3:
		ax3.plot(x3, y3[cont], label=names[cont])
		cont = cont + 1
	cont = 0
	ax3.set_ylabel(ylabel[2])
	ax3.set_xlabel(xlabel[2])
	for variableLinguistica in y4:
		ax4.plot(x4, y4[cont], label=names[cont])
		cont = cont + 1
	cont = 0
	ax4.set_ylabel(ylabel[3])
	ax4.set_xlabel(xlabel[3])
	ax1.legend(numpoints=1)
	#ax1.ylabel(ylabel[0])
	#ax1.xlabel(xlabel[0])
	
	ax2.legend(numpoints=1)
	#ax2.ylabel(ylabel[1])
	#ax2.xlabel(xlabel[1])
	
	ax3.legend(numpoints=1)
	#ax3.ylabel(ylabel[2])
	#ax3.xlabel(xlabel[2])
	
	ax4.legend(numpoints=1)
	#ax4.ylabel(ylabel[3])
	#ax4.xlabel(xlabel[3])
	ax1.set_title("Cantidad de Agua vs Pertenencia")
	ax2.set_title("Cantidad de Cafe vs Pertenencia")
	ax3.set_title("Cantidad de Leche vs Pertenencia")
	ax4.set_title("Cantidad de Chocolate vs Pertenencia")
	plt.show()
	return
