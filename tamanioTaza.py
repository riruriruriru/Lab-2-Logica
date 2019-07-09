import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar

def tamanioTaza():
	tamanio = ctrl.Antecedent([0,30,60,90,120,150,200,250,300,350,400,450],'tamanio')
	tamanio['pequenio'] = funcionPequenio(tamanio)
	tamanio['mediano'] = funcionMediano(tamanio)
	tamanio['grande'] = funcionGrande(tamanio)
	graficar.graficar(tamanio.universe,[tamanio["pequenio"].mf,tamanio["mediano"].mf,tamanio["grande"].mf],["Pequeño","Mediano","Grande"],"Tamaño de taza en ml","Grado de pertenencia","Tamaño taza")
	return tamanio

def funcionPequenio(tamanio):
	pequenio = fuzz.zmf(tamanio.universe,250,400)
	return pequenio

def funcionMediano(tamanio):
	mediano = fuzz.gaussmf(tamanio.universe,350,50)
	return mediano

def funcionGrande(tamanio):
	grande = fuzz.zmf(tamanio.universe,300,400)
	for i in range(len(grande)):
		grande[i] = 1-grande[i]
	return grande

tamanioTaza()