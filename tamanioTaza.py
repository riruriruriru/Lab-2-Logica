import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar
#funcion que crea el antecedente tamanio y lo retorna
def tamanioTaza():
	tamanio = ctrl.Antecedent([0,30,60,90,120,150,200,250,300,350,400,450],'tamanio')
	tamanio['pequenio'] = funcionPequenio(tamanio)
	tamanio['mediano'] = funcionMediano(tamanio)
	tamanio['grande'] = funcionGrande(tamanio)#se definen las funciones de pertenencia para cada variable lingüistica
	#se grafica el antecedente
	graficar.graficar(tamanio.universe,[tamanio["pequenio"].mf,tamanio["mediano"].mf,tamanio["grande"].mf],["Pequeño","Mediano","Grande"],"Tamaño de taza en ml","Grado de pertenencia","Tamaño taza")
	return tamanio

def funcionPequenio(tamanio):
	pequenio = fuzz.trapmf(tamanio.universe,[0,0,90,200])
	return pequenio

def funcionMediano(tamanio):
	mediano = fuzz.trapmf(tamanio.universe,[90,200,250,350])
	return mediano

def funcionGrande(tamanio):
	grande = fuzz.trapmf(tamanio.universe,[250,350,450,450])
	return grande
