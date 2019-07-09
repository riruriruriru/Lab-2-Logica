import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import graficar as graficar

def tamanioTaza():
	tamanio = ctrl.Antecedent([0,30,60,90,120,150,200,250,300,350,400,450, 455],'tamanio')
	tamanio['pequenio'] = funcionPequenio(tamanio)
	tamanio['mediano'] = funcionMediano(tamanio)
	tamanio['grande'] = funcionGrande(tamanio)
	#agua = ctrl.Consequent([0, 30, 60, 90, 120, 150, 200, 250, 300, 350, 400, 450], 'agua')
	#agua['poca'] = fuzz.trapmf(agua.universe,[0,0,150,250])
	#agua['media'] = fuzz.trimf(agua.universe,[150,250,350])
	#agua['mucha'] = fuzz.trapmf(agua.universe,[250,350,450,450])
	graficar.graficar(tamanio.universe,[tamanio["pequenio"].mf,tamanio["mediano"].mf,tamanio["grande"].mf],["Pequeño","Mediano","Grande"],"Tamaño de taza en ml","Grado de pertenencia","Tamaño taza")
	return tamanio

def funcionPequenio(tamanio):
	pequenio = fuzz.trapmf(tamanio.universe,[0,0,90,200])
	return pequenio

def funcionMediano(tamanio):
	mediano = fuzz.trapmf(tamanio.universe,[90,200,250,350])
	return mediano

def funcionGrande(tamanio):
	grande = fuzz.trapmf(tamanio.universe,[250,350,455,455])
	return grande
