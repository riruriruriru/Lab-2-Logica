import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import graficar as graficar

#función que crea y retorna las reglas definidas por el enunciado y la combinatoria de antecedentes para evitar caidas en el momento de desfuzzificacion
def reglas(tamanioTaza, temperaturaAmbiental, intensidadCafe, nivelAgua, cantidadCafe,cantidadLeche, cantidadChocolate, tiempoPreparacion, tipoCafe):
	if tipoCafe == "Latte": #reglas para latte
		regla1Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'],cantidadLeche['media'], tiempoPreparacion['media']))
		regla2Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['media'],cantidadLeche['poca'], tiempoPreparacion['poca']))
		regla3Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla4Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['poca']))
		regla5Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla6Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['mucha']))
		#fin de reglas de enunciado
		#inicio combinatoria
		regla7Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['media'],tiempoPreparacion['media']))
		regla8Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla9Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], cantidadLeche['mucha'], tiempoPreparacion['poca']))
		regla10Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['poca']))
		regla11Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], cantidadLeche['mucha'], tiempoPreparacion['poca']))
		regla12Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['poca']))
		regla13Latte = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], cantidadLeche['media'], tiempoPreparacion['poca']))

		regla14Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['mucha'], tiempoPreparacion['media']))
		regla15Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla16Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['mucha']))
		regla17Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['mucha'], tiempoPreparacion['media']))
		regla18Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['media']))
		regla19Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['mucha'], tiempoPreparacion['poca']))
		regla20Latte = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['poca']))

		regla21Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['mucha'], tiempoPreparacion['mucha']))
		regla22Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla23Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla24Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla25Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla26Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['mucha'], tiempoPreparacion['mucha']))
		regla27Latte = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		return [regla1Latte,regla2Latte,regla3Latte,regla4Latte,regla5Latte,regla6Latte,regla7Latte,regla8Latte,regla9Latte,regla10Latte,regla11Latte,regla12Latte,regla13Latte,regla14Latte,regla15Latte,regla16Latte,regla17Latte,regla18Latte,regla19Latte,regla20Latte,regla21Latte,regla22Latte,regla23Latte,regla24Latte,regla25Latte,regla26Latte,regla27Latte]

	



	elif tipoCafe == "Mokaccino": #reglas mokaccino
		regla1Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'], cantidadChocolate['poca'], tiempoPreparacion['poca']))
		regla2Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['poca'], tiempoPreparacion['poca']))
		regla3Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['poca'], tiempoPreparacion['media']))
		regla4Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['poca'], cantidadChocolate['poca'], tiempoPreparacion['poca']))
		regla5Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['poca'], tiempoPreparacion['mucha']))
		regla6Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['poca'], tiempoPreparacion['media']))
		#fin de reglas de enunciado
		#inicio combinatoria de reglas
		regla7Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'], cantidadChocolate['poca'] ,tiempoPreparacion['media']))
		regla8Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], cantidadLeche['poca'], cantidadChocolate['poca'] ,tiempoPreparacion['mucha']))
		regla9Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['poca'] ,tiempoPreparacion['media']))
		regla10Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'], cantidadChocolate['poca'] ,tiempoPreparacion['media']))
		regla11Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'], cantidadChocolate['poca'] ,tiempoPreparacion['poca']))
		regla12Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['poca'] ,tiempoPreparacion['media']))
		regla13Moka = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], cantidadLeche['poca'], cantidadChocolate['poca'] ,tiempoPreparacion['media']))

		regla14Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['media'] ,tiempoPreparacion['mucha']))
		regla15Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['media'] ,tiempoPreparacion['media']))
		regla16Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['mucha'], cantidadLeche['poca'], cantidadChocolate['media'] ,tiempoPreparacion['mucha']))
		regla17Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['poca'], cantidadChocolate['media'] ,tiempoPreparacion['media']))
		regla18Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['mucha'], cantidadLeche['poca'], cantidadChocolate['media'] ,tiempoPreparacion['mucha']))
		regla19Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['media'] ,tiempoPreparacion['media']))
		regla20Moka = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['media'] ,tiempoPreparacion['media']))

		regla21Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['mucha'] ,tiempoPreparacion['mucha']))
		regla22Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['mucha'] ,tiempoPreparacion['mucha']))
		regla23Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['mucha'] ,tiempoPreparacion['media']))
		regla24Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], cantidadChocolate['mucha'] ,tiempoPreparacion['mucha']))
		regla25Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], cantidadLeche['poca'], cantidadChocolate['mucha'] ,tiempoPreparacion['mucha']))
		regla26Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], cantidadChocolate['mucha'] ,tiempoPreparacion['mucha']))
		regla27Moka = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], cantidadLeche['poca'], cantidadChocolate['mucha'] ,tiempoPreparacion['media']))
		return [regla1Moka,regla2Moka,regla3Moka,regla4Moka,regla5Moka,regla6Moka,regla7Moka,regla8Moka,regla9Moka,regla10Moka,regla11Moka,regla12Moka,regla13Moka,regla14Moka,regla15Moka,regla16Moka,regla17Moka,regla18Moka,regla19Moka,regla20Moka,regla21Moka,regla22Moka,regla23Moka,regla24Moka,regla25Moka,regla26Moka,regla27Moka]
	
	elif tipoCafe == "Espresso":#reglas para tipo de cafe espresso
		
		regla1Espresso= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], tiempoPreparacion['media']))
		regla2Espresso= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['media'], tiempoPreparacion['poca']))
		regla3Espresso= ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['poca'], tiempoPreparacion['poca']))
		regla4Espresso= ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['media'], tiempoPreparacion['poca']))
		regla5Espresso= ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['media'], tiempoPreparacion['media']))
		regla6Espresso= ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], tiempoPreparacion['poca']))
		#fin de reglas de enunciado
		#inicio combinatoria de reglas
		regla7Espresso= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], tiempoPreparacion['media']))
		regla8Espresso= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], tiempoPreparacion['media']))
		regla9Espresso= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], tiempoPreparacion['poca']))
		regla10Espresso = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], tiempoPreparacion['poca']))
		regla11Espresso = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], tiempoPreparacion['poca']))
		regla12Espresso = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], tiempoPreparacion['poca']))
		regla13Espresso = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], tiempoPreparacion['poca']))

		regla14Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], tiempoPreparacion['media']))
		regla15Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], tiempoPreparacion['media']))
		regla16Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['poca'], tiempoPreparacion['media']))
		regla17Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['media'], tiempoPreparacion['media']))
		regla18Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['media'], tiempoPreparacion['poca']))
		regla19Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['media'], tiempoPreparacion['poca']))
		regla20Espresso = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], tiempoPreparacion['poca']))

		regla21Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], tiempoPreparacion['poca']))
		regla22Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['mucha'], tiempoPreparacion['poca']))
		regla23Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], tiempoPreparacion['media']))
		regla24Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['mucha'], tiempoPreparacion['media']))
		regla25Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], tiempoPreparacion['media']))
		regla26Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], tiempoPreparacion['media']))
		regla27Espresso = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], tiempoPreparacion['media']))
		return [regla1Espresso,regla2Espresso,regla3Espresso,regla4Espresso,regla5Espresso,regla6Espresso,regla7Espresso,regla8Espresso,regla9Espresso,regla10Espresso,regla11Espresso,regla12Espresso,regla13Espresso,regla14Espresso,regla15Espresso,regla16Espresso,regla17Espresso,regla18Espresso,regla19Espresso,regla20Espresso,regla21Espresso,regla22Espresso,regla23Espresso,regla24Espresso,regla25Espresso,regla26Espresso,regla27Espresso]
	
	elif tipoCafe == "Capuccino":#reglas para capuccino
		regla1Capuccino= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'],cantidadLeche['media'], tiempoPreparacion['media']))
		regla2Capuccino= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['media'],cantidadLeche['poca'], tiempoPreparacion['poca']))
		regla3Capuccino= ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla4Capuccino= ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['poca']))
		regla5Capuccino= ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla6Capuccino= ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['mucha']))
		#fin de reglas de enunciado
		#inicio combinatoria de reglas
		regla7Capuccino= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'],tiempoPreparacion['poca']))
		regla8Capuccino= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['poca']))
		regla9Capuccino= ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['poca']))
		regla10Capuccino = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['poca']))
		regla11Capuccino = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla12Capuccino = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['poca'], cantidadCafe['media'], cantidadLeche['poca'], tiempoPreparacion['media']))
		regla13Capuccino = ctrl.Rule(tamanioTaza['pequenio'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['poca'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['media']))

		regla14Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla15Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla16Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['frio'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['media']))
		regla17Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla18Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['media'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['media']))
		regla19Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['media'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla20Capuccino = ctrl.Rule(tamanioTaza['mediano'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['media'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['poca']))

		regla21Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla22Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['frio'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla23Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla24Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['medio'], ( nivelAgua['mucha'], cantidadCafe['media'], cantidadLeche['media'], tiempoPreparacion['mucha']))
		regla25Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['calido'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['mucha']))
		regla26Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['suave'], ( nivelAgua['mucha'], cantidadCafe['poca'], cantidadLeche['media'], tiempoPreparacion['media']))
		regla27Capuccino = ctrl.Rule(tamanioTaza['grande'] & temperaturaAmbiental['caluroso'] & intensidadCafe['fuerte'], ( nivelAgua['mucha'], cantidadCafe['mucha'], cantidadLeche['poca'], tiempoPreparacion['media']))
		return [regla1Capuccino,regla2Capuccino,regla3Capuccino,regla4Capuccino,regla5Capuccino,regla6Capuccino,regla7Capuccino,regla8Capuccino,regla9Capuccino,regla10Capuccino,regla11Capuccino,regla12Capuccino,regla13Capuccino,regla14Capuccino,regla15Capuccino,regla16Capuccino,regla17Capuccino,regla18Capuccino,regla19Capuccino,regla20Capuccino,regla21Capuccino,regla22Capuccino,regla23Capuccino,regla24Capuccino,regla25Capuccino,regla26Capuccino,regla27Capuccino]
