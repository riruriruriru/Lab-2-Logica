import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar

#Funcion que retorna la funcion de pertenencia de la temperatura
def temperaturaAmbiental():
	temperatura = ctrl.Antecedent(np.arange(0,45),'temperatura') #Se crea el antecedente temperatura
	temperatura['frio'] = funcionFrio(temperatura)#Se crean sus variables lingüisticas y se les da una funcion de pertenencia
	temperatura['calido'] = funcionTemplado(temperatura)
	temperatura['caluroso'] = funcionCalor(temperatura)
	#Se grafica el antecedente temperatura
	graficar.graficar(temperatura.universe,[temperatura["frio"].mf,temperatura["calido"].mf,temperatura["caluroso"].mf],["Frío","Cálido","Caluroso"],"Temperatura en °C","Grado de pertenencia","Temperatura Ambiental")
	return temperatura



def funcionFrio(temperatura):
	#se define la funcion de pertenencia para caso frío
	frio = fuzz.trapmf(temperatura.universe,[0,0,15,20])
	return frio

def funcionTemplado(temperatura):
	#funcion de pertenencia para caso templado
	templado = fuzz.trimf(temperatura.universe,[15,20,25])
	return templado

def funcionCalor(temperatura):
	#funcion de pertenencia para caso calido
	calor = fuzz.trapmf(temperatura.universe,[20,25,35,35])
	return calor
