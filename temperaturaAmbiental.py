import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def temperaturaAmbiental():
	temperatura = np.arange(-5,45)
	frio = funcionFrio(temperatura)
	templado = funcionTemplado(temperatura)
	calor = funcionCalor(temperatura)
	plt.plot(temperatura,frio)
	plt.show()
	print(frio)
	print(templado)
	print(calor)
	return

def funcionFrio(temperatura,):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	frio = fuzz.smf(temperatura,20,28)
	for i in range(len(frio)):
		frio[i] = 1-frio[i]

	return frio

def funcionTemplado(temperatura):
	#gaussmf(valores,promedio,desviacion estandar)
	templado = fuzz.gaussmf(temperatura,20,10)
	return templado

def funcionCalor(temperatura):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	calor = fuzz.smf(temperatura,20,28)
	return calor

temperaturaAmbiental()