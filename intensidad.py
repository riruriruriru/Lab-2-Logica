import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar

def funcionSuave(intensidad):
	suave = fuzz.trapmf(intensidad,[1,1,2,3])
	

	return suave
def funcionMedio(intensidad):
	medio = fuzz.trimf(intensidad,[2,3,4])

	return medio
def funcionFuerte(intensidad):
	fuerte = fuzz.trapmf(intensidad,[1,1,3,4])
	for i in range(len(fuerte)):
		fuerte[i] = 1-fuerte[i]

	return fuerte

#funcion que retorna al antecedente intensidad luego de definir todas las funciones de pertenencia para sus variables lingüisticas
def intensidad():
	#se crea el antecedente
	intensidad = ctrl.Antecedent(np.arange(1,6),'intensidad') 
	intensidad["suave"] = funcionSuave(intensidad.universe)
	intensidad["medio"] = funcionMedio(intensidad.universe)
	intensidad["fuerte"] = funcionFuerte(intensidad.universe)
	#se grafica el antecedente intensidad
	graficar.graficar(intensidad.universe,[intensidad["suave"].mf,intensidad["medio"].mf,intensidad["fuerte"].mf],["Suave","Medio","Fuerte"],"Grado de Intensidad","Grado de pertenencia","Intensidad del Café")
	return intensidad

