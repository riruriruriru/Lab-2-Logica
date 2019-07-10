import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar

def temperaturaAmbiental():
	temperatura = ctrl.Antecedent(np.arange(0,45),'temperatura')
	temperatura['frio'] = funcionFrio(temperatura)
	temperatura['calido'] = funcionTemplado(temperatura)
	temperatura['caluroso'] = funcionCalor(temperatura)
	#graficar.graficar(temperatura.universe,[temperatura["frio"].mf,temperatura["calido"].mf,temperatura["caluroso"].mf],["Frío","Cálido","Caluroso"],"Temperatura en °C","Grado de pertenencia","Temperatura Ambiental")
	return temperatura



def funcionFrio(temperatura):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	frio = fuzz.trapmf(temperatura.universe,[0,0,15,20])
	return frio

def funcionTemplado(temperatura):
	#gaussmf(valores,promedio,desviacion estandar)
	templado = fuzz.trimf(temperatura.universe,[15,20,25])
	return templado

def funcionCalor(temperatura):
	#smf(valores,desde donde deja de ser 0, desde donde empieza a ser 1)
	calor = fuzz.trapmf(temperatura.universe,[20,25,35,35])
	return calor




