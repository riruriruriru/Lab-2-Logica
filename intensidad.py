import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar

def funcionSuave(intensidad):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	suave = fuzz.trapmf(intensidad,[1,1,2,3])
	#for i in range(len(suave)):
	#	suave[i] = 1-suave[i]

	return suave
def funcionMedio(intensidad):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	medio = fuzz.trimf(intensidad,[2,3,4])
	#for i in range(len(medio)):
	#	medio[i] = 1-medio[i]

	return medio
def funcionFuerte(intensidad):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	fuerte = fuzz.trapmf(intensidad,[1,1,3,4])
	for i in range(len(fuerte)):
		fuerte[i] = 1-fuerte[i]

	return fuerte

def intensidad():
	intensidad = ctrl.Antecedent(np.arange(1,6),'intensidad') 
	intensidad["suave"] = funcionSuave(intensidad.universe)
	intensidad["medio"] = funcionMedio(intensidad.universe)
	intensidad["fuerte"] = funcionFuerte(intensidad.universe)
	graficar.graficar(intensidad.universe,[intensidad["suave"].mf,intensidad["medio"].mf,intensidad["fuerte"].mf],["Suave","Medio","Fuerte"],"Grado de Intensidad","Grado de pertenencia","Intensidad del Café")
	return intensidad

