import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import graficar as graficar

#Entrada: entero entre -5 y 45
#Salida: "frio" si e frio, "templado" si es templado, "calor" si es calor
#def getTemperaturaAmbiental(x):
#	temperatura = np.arange(-5,45)
#	frio = funcionFrio(temperatura)
#	templado = funcionTemplado(temperatura)
#	calor = funcionCalor(temperatura)
#	xFrio = frio[x+5]
#	xTemplado = templado[x+5]
#	xCalor = calor[x+5]
#	mayor = max([xFrio,xTemplado,xCalor])
#	print("frio ",xFrio)
#	print("templado ",xTemplado)
#	print("calor ",xCalor)
#	print("max ",mayor)
#	if xFrio == mayor:
#		print("frio")
#		return "frio"
#	elif xTemplado == mayor:
#		print("templado")
#		return "templado"
#	else:
#		print("calor")
#		return "calor"

def temperaturaAmbiental():
	temperatura = np.arange(-5,45)
	frio = funcionFrio(temperatura)
	templado = funcionTemplado(temperatura)
	calor = funcionCalor(temperatura)
	graficar.graficar(temperatura,[frio,templado,calor],["Frío","Templado","Calor"],"Temperatura en °C","Grado de pertenencia","Temperatura Ambiental")
	return



def funcionFrio(temperatura):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	frio = fuzz.smf(temperatura,0,25)
	for i in range(len(frio)):
		frio[i] = 1-frio[i]

	return frio

def funcionTemplado(temperatura):
	#gaussmf(valores,promedio,desviacion estandar)
	templado = fuzz.gaussmf(temperatura,20,10)
	return templado

def funcionCalor(temperatura):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	calor = fuzz.smf(temperatura,10,30)
	return calor
#getTemperaturaAmbiental(30)
temperaturaAmbiental()
