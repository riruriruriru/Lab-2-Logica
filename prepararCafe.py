import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import graficar as graficar

def reglas(tamanioTaza, temperaturaAmbiental, intensidadCafe, nivelAgua, cantidadCafe,cantidadLeche, cantidadChocolate, tiempoPreparacion, tipoCafe):
	if tipoCafe == "Latte":
		regla1Latte = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['frio'] & intensidadCafe['suave'], (nivelAgua['poca'],cantidadCafe['poca'],cantidadLeche['media'],tiempoPreparacion['media']))
		regla2Latte = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], (nivelAgua['poca'],cantidadCafe['poca'],cantidadLeche['poca'],tiempoPreparacion['poca']))
		regla3Latte = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['calido'] & intensidadCafe['medio'], (nivelAgua['media'],cantidadCafe['media'],cantidadLeche['media'],tiempoPreparacion['poca']))
		regla4Latte = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], (nivelAgua['media'],cantidadCafe['mucha'],cantidadLeche['poca'],tiempoPreparacion['poca']))
		regla5Latte = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], (nivelAgua['mucha'],cantidadCafe['mucha'],cantidadLeche['poca'],tiempoPreparacion['mucha']))
		regla6Latte = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['calido'] & intensidadCafe['suave'], (nivelAgua['mucha'],cantidadCafe['poca'],cantidadLeche['mucha'],tiempoPreparacion['media']))
		return regla1Latte,regla2Latte,regla3Latte,regla4Latte,regla5Latte,regla6Latte
	
	elif tipoCafe == "Mokaccino":
		regla1Moka = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], (nivelAgua['poca'],cantidadCafe['media'],cantidadLeche['poca'],cantidadChocolate['poca'],tiempoPreparacion['poca']))
		regla2Moka = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], (nivelAgua['poca'],cantidadCafe['poca'],cantidadLeche['media'],cantidadChocolate['poca'],tiempoPreparacion['poca']))
		regla3Moka = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['frio'] & intensidadCafe['medio'], (nivelAgua['media'],cantidadCafe['media'],cantidadLeche['media'],cantidadChocolate['poca'],tiempoPreparacion['media']))
		regla4Moka = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], (nivelAgua['media'],cantidadCafe['media'],cantidadLeche['poca'],cantidadChocolate['poca'],tiempoPreparacion['poca']))
		regla5Moka = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], (nivelAgua['mucha'],cantidadCafe['media'],cantidadLeche['media'],cantidadChocolate['poca'],tiempoPreparacion['mucha']))
		regla6Moka = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['calido'] & intensidadCafe['suave'], (nivelAgua['mucha'],cantidadCafe['poca'],cantidadLeche['media'],cantidadChocolate['poca'],tiempoPreparacion['media']))
		return regla1Moka,regla2Moka,regla3Moka,regla4Moka,regla5Moka,regla6Moka
	
	elif tipoCafe == "Espresso":
		regla1Espresso = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['frio'] & intensidadCafe['suave'], (nivelAgua['poca'],cantidadCafe['poca'],tiempoPreparacion['media']))
		regla2Espresso = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], (nivelAgua['poca'],cantidadCafe['media'],tiempoPreparacion['poca']))
		regla3Espresso = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['calido'] & intensidadCafe['medio'], (nivelAgua['media'],cantidadCafe['poca'],tiempoPreparacion['poca']))
		regla4Espresso = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], (nivelAgua['media'],cantidadCafe['media'],tiempoPreparacion['poca']))
		regla5Espresso = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['frio'] & intensidadCafe['suave'], (nivelAgua['mucha'],cantidadCafe['media'],tiempoPreparacion['media']))
		regla6Espresso = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], (nivelAgua['mucha'],cantidadCafe['media'],tiempoPreparacion['poca']))
		return regla1Espresso,regla2Espresso,regla3Espresso,regla4Espresso,regla5Espresso,regla6Espresso
	
	elif tipoCafe == "Capuccino":
		regla1Capuccino = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['frio'] & intensidadCafe['suave'], (nivelAgua['poca'],cantidadCafe['poca'],cantidadLeche['media'],tiempoPreparacion['media']))
		regla2Capuccino = ctrl.Rule(tamanioTaza['pequenio'] &temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], (nivelAgua['poca'],cantidadCafe['media'],cantidadLeche['poca'],tiempoPreparacion['poca']))
		regla3Capuccino = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['calido'] & intensidadCafe['medio'], (nivelAgua['media'],cantidadCafe['media'],cantidadLeche['media'],tiempoPreparacion['media']))
		regla4Capuccino = ctrl.Rule(tamanioTaza['mediano'] &temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], (nivelAgua['media'],cantidadCafe['media'],cantidadLeche['poca'],tiempoPreparacion['poca']))
		regla5Capuccino = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['calido'] & intensidadCafe['suave'], (nivelAgua['mucha'],cantidadCafe['poca'],cantidadLeche['media'],tiempoPreparacion['media']))
		regla6Capuccino = ctrl.Rule(tamanioTaza['grande'] &temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], (nivelAgua['mucha'],cantidadCafe['media'],cantidadLeche['poca'],tiempoPreparacion['mucha']))
		return regla1Capuccino,regla2Capuccino,regla3Capuccino,regla4Capuccino,regla5Capuccino,regla6Capuccino

