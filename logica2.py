import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import prepararCafe as rules
import temperaturaAmbiental as temp
import tamanioTaza as taza
import intensidad as intensity
import cantidadAguaLecheChocolate as quantity
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


#Se importan los otros archivos de la carpeta que contienen el resto de las funciones
###########################################################################################################
################Bloque de definición de funciones##########################################################

#Función que se encarga de escribir en un archivo de salida y escribe los resultados con el formato indicado
#en el enunciado
def writeOutput(inputTipo, inputTemperatura, inputIntensidad, inputTamanio, agua, cafe,leche,choc,tiempo):
	strName = "Cafe_"+str(inputTamanio)+"_"+str(inputTipo)+"_"+str(inputIntensidad)+"_"+str(inputTemperatura)
	archivo = open(strName+".txt", 'w')
	archivo.write("Nivel de Agua: "+str(agua)+" mL")
	archivo.write("Cantidad de Café: "+str(cafe)+ " grs")
	archivo.write("Cantidad de Leche: "+str(leche)+" grs")
	archivo.write("Cantidad de Chocolate: "+str(choc)+" grs")
	archivo.write("Tiempo de Preparación: "+str(tiempo)+ " segundos")

#Clase que contiene los colores utilizados en el menú
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Se recibe el valor desfuzzificado del agua y se acerca al valor mayor más cercano
#Ej: 128 ml => 150 ml
def distance(valorAgua):
	print("valorAgua"+str(valorAgua))#aqui
	valoresAgua = [0,30,60,90,120,150,200,250,300,350,400,450]
	for valor in valoresAgua:
		distancia = valor-valorAgua
		if distancia >= 0:
			return int(valor)
#Función que recibe las entradas y llama a las correspondientes funciones de pertenencia
#Además, llama a la función que define las reglas y luego utiliza los inputs en las reglas de inferencia
#Finalmente, llama a la función de escritura de resultados y muestra los gráficos de las funciones de pertenencia
def preparacionDeCafe(inputTemperatura, inputTaza, inputInt, inputTipo):
	inputTaza = distance(inputTaza)
	if inputTemperatura == 0:
		inputTemperatura = inputTemperatura+1
	print("Input taza: "+str(inputTaza))
	temperaturaFuzzy = temp.temperaturaAmbiental()#Se crean las funciones de pertenencia de los antecedentes
	tamanioTazaFuzzy = taza.tamanioTaza()
	intensidadFuzzy =intensity.intensidad()
	agua, cafe, leche, chocolate, tiempo = quantity.cantidadesAguaLecheChocolateCafeTiempo() #Se llama a una función que retorna las funciones de pertenencia de los consecuentes
	reglas = rules.reglas(tamanioTazaFuzzy, temperaturaFuzzy, intensidadFuzzy, agua, cafe,leche, chocolate, tiempo, inputTipo) #Se llama a la funcion que crea las reglas
	controlCafetera = ctrl.ControlSystem(reglas) #Se crea un "controlador" con las reglas
	opciones = ctrl.ControlSystemSimulation(controlCafetera) #Se simula el sistema de control 
	opciones.input['temperatura'] = inputTemperatura
	opciones.input['tamanio'] = inputTaza
	opciones.input['intensidad'] = inputInt #Se entregan los input al sistema de control
	opciones.compute()
	#Bloque de if que obtiene los resultados dependiendo del tipo de café que se quiere preparar
	if inputTipo == "Latte": 
		resultadoAgua =distance(opciones.output['agua'])
		resultadoTiempo =int(opciones.output['tiempo'])
		resultadoLeche =int(opciones.output['leche'])
		resultadoCafe =int(opciones.output['cafe'])
		print("Nivel de Agua: "+str(resultadoAgua)+" mL")
		print("Cantidad de Café: "+str(resultadoCafe)+" grs")
		print("Cantidad de Leche: "+str(resultadoLeche)+" grs")
		print("Tiempo de Preparación: "+str(resultadoTiempo)+" segundos")
		writeOutput(inputTipo, inputTemperatura, inputInt, inputTaza, resultadoAgua, resultadoCafe,resultadoLeche,0,resultadoTiempo)#Se escribe en archivo de salida
		temperaturaFuzzy.view(sim=opciones)
		tamanioTazaFuzzy.view(sim=opciones)
		intensidadFuzzy.view(sim=opciones)
		
		agua.view(sim=opciones)
		tiempo.view(sim=opciones)
		cafe.view(sim=opciones)
		chocolate.view(sim=opciones)
		leche.view(sim=opciones) #Se muestran gráficos de resultado
		plt.show()
	elif inputTipo == "Capuccino":
		resultadoAgua =distance(opciones.output['agua'])
		resultadoTiempo =int(opciones.output['tiempo'])
		resultadoLeche =int(opciones.output['leche'])
		resultadoCafe =int(opciones.output['cafe'])
		print("Nivel de Agua: "+str(resultadoAgua)+" mL")
		print("Cantidad de Café: "+str(resultadoCafe)+" grs")
		print("Cantidad de Leche: "+str(resultadoLeche)+" grs")
		print("Tiempo de Preparación: "+str(resultadoTiempo)+" segundos")
		writeOutput(inputTipo, inputTemperatura, inputInt, inputTaza, resultadoAgua, resultadoCafe,resultadoLeche,0,resultadoTiempo)
		temperaturaFuzzy.view(sim=opciones)
		tamanioTazaFuzzy.view(sim=opciones)
		intensidadFuzzy.view(sim=opciones)
		
		agua.view(sim=opciones)
		tiempo.view(sim=opciones)
		cafe.view(sim=opciones)
		chocolate.view(sim=opciones)
		leche.view(sim=opciones)
		plt.show()
	elif inputTipo == "Mokaccino":
		resultadoAgua =distance(opciones.output['agua'])
		resultadoTiempo =int(opciones.output['tiempo'])
		resultadoLeche =int(opciones.output['leche'])
		resultadoCafe =int(opciones.output['cafe'])
		resultadoChocolate =int(opciones.output['chocolate'])
		print("Nivel de Agua: "+str(resultadoAgua)+" mL")
		print("Cantidad de Café: "+str(resultadoCafe)+" grs")
		print("Cantidad de Leche: "+str(resultadoLeche)+" grs")
		print("Cantidad de Chocolate: "+str(resultadoChocolate)+" grs")
		print("Tiempo de Preparación: "+str(resultadoTiempo)+" segundos")
		writeOutput(inputTipo, inputTemperatura, inputInt, inputTaza, resultadoAgua, resultadoCafe,resultadoLeche,resultadoChocolate,resultadoTiempo)
		temperaturaFuzzy.view(sim=opciones)
		tamanioTazaFuzzy.view(sim=opciones)
		intensidadFuzzy.view(sim=opciones)
		
		agua.view(sim=opciones)
		tiempo.view(sim=opciones)
		cafe.view(sim=opciones)
		chocolate.view(sim=opciones)
		leche.view(sim=opciones)
		plt.show()
	elif inputTipo == "Espresso":
		resultadoAgua =distance(opciones.output['agua'])
		resultadoTiempo =int(opciones.output['tiempo'])
		resultadoCafe =int(opciones.output['cafe'])
		print("Nivel de Agua: "+str(resultadoAgua)+" mL")
		print("Cantidad de Café: "+str(resultadoCafe)+" grs")
		print("Tiempo de Preparación: "+str(resultadoTiempo)+" segundos")
		writeOutput(inputTipo, inputTemperatura, inputInt, inputTaza, resultadoAgua, resultadoCafe,0,0,resultadoTiempo)
		temperaturaFuzzy.view(sim=opciones)
		tamanioTazaFuzzy.view(sim=opciones)
		intensidadFuzzy.view(sim=opciones)
		
		agua.view(sim=opciones)
		tiempo.view(sim=opciones)
		cafe.view(sim=opciones)
		chocolate.view(sim=opciones)
		leche.view(sim=opciones)
		plt.show()

#Función llamada por el menú que recibe el tamaño de la taza en ml
def recibirCantidad():
	cantidadCafe = 0
	
	cont = 0
	
	while True:
		
		print("Ingrese el tamaño de taza [ml] número entero entre [0,450]: " )
		cambiar = 0
		try:
			cantidadCafe = int(input())
			cont = 0
			retorno = [0,cantidadCafe]
			if cantidadCafe > 450 or cantidadCafe < 0:
				print("Ingrese un valor entre el intervalo indicado")
			else:
				while cambiar == 0:
					print("Ingresó un tamaño de " + str(cantidadCafe)+"[ml]. ¿Desea cambiarla?")
					print(bcolors.BOLD+bcolors.OKGREEN+"1. Si"+bcolors.ENDC)
					print(bcolors.BOLD+bcolors.OKGREEN+"2. No"+bcolors.ENDC)
					try:
						cambiar = int(input())
						if cambiar == 1:
							cambiar = 3
							print("Se eliminará su valor ingresado...")
						elif cambiar == 2:
							retorno = [0, cantidadCafe]
							return retorno
						else:
							print("Ingrese una opción válida")
							cambiar = 0
					except:
						print("Ingrese el número de la opción correspondiente")
		except:
			cont = 0
			print("Ingrese número entero entre [0,450]")
	return
	
#Funcion que muestra los parámetros ya ingresados en el menu principal
def mostrarParametros(parametros):

	largo = len(parametros)
	print("")
	for par in parametros:
		if par[1] != -1:
			print(par[0] + ": " + str(par[1]))
	#print("uwu")
	print("")
#funcion que recibe la temperatura ingresada por el usuario
def recibirTemperatura():
	nivelTemperatura = 0
	
	cont = 0
	
	while True:
		
		print("Ingrese la temperatura ambiente [°C] número entero entre [0,33] 🥶 🥵 " )
		cambiar = 0
		try:
			nivelTemperatura = int(input())
			cont = 0
			retorno = [0,nivelTemperatura]
			if nivelTemperatura > 33 or nivelTemperatura < 0:
				print("Ingrese un valor entre el intervalo indicado")
			else:
				while cambiar == 0:
					print("Ingresó una temperatura de " + str(nivelTemperatura)+"°. ¿Desea cambiarla?")
					print(bcolors.BOLD+bcolors.OKGREEN+"1. Si"+bcolors.ENDC)
					print(bcolors.BOLD+bcolors.OKGREEN+"2. No"+bcolors.ENDC)
					try:
						cambiar = int(input())
						if cambiar == 1:
							cambiar = 3
							print("Se eliminará su valor ingresado...")
						elif cambiar == 2:
							retorno = [0, nivelTemperatura]
							return retorno
						else:
							print("Ingrese una opción válida")
							cambiar = 0
					except:
						print("Ingrese el número de la opción correspondiente")
		except:
			cont = 0
			print("Ingrese número entero entre [0,33]")
	return
	
#Funcion que recibe el nivel de intensidad y lo retorna al menu principal
def recibirNivelIntensidad():
	nivelIntensidad = ["1", "2", "3", "4", "5"]
	opcion = 0
	cont = 0
	while opcion !=6 or opcion != 7:
		print("Ingrese una de las siguientes opciones: " )
		for nivel in nivelIntensidad:
			cont = cont +1
			print(str(cont)+". "+nivel)
			if cont == 5:
				print("6. Retroceder al menú anterior")
				print("7. Salir")
		try:
			opcion = int(input())
			cont = 0
			if opcion>7 or opcion<1:
				print("Ingrese una opcion valida")
				opcion = 0
			elif opcion == 1:
				return [0, 1]
				
			elif opcion == 2:
				return [0, 2]
				
			elif opcion == 3:
				return [0, 3]
				
			elif opcion == 4:
				return [0, 4]
			elif opcion == 5:
				return [0, 5]
					
			elif opcion == 6:
				retorno = [0,-1]
				return retorno
			elif opcion == 7:
				retorno = [5,-1]
				return retorno
			else:
				print("uwu")
		except:
			cont = 0
			print("Ingrese el número de la opción correspondiente")
	return
#Funcion que recibe el tipo de preparacion y lo retorna al menu principal
def recibirPreparacion():
	tipoP = ["Latte", "Capuccino", "Mokaccino", "Espresso"]
	opcion = 0
	cont = 0
	while opcion !=5:
		print("Ingrese una de las siguientes opciones: " )
		for tipo in tipoP:
			cont = cont +1
			print(str(cont)+". "+tipo)
			if cont == 4:
				print("5. Retroceder al menú anterior")
				print("6. Salir")
		try:
			opcion = int(input())
			cont = 0
			if opcion>6 or opcion<1:
				print("Ingrese una opcion valida")
				opcion = 0
			elif opcion == 1:
				return [0, "Latte"]
				
			elif opcion == 2:
				return [0, "Capuccino"]
				
			elif opcion == 3:
				return [0, "Mokaccino"]
				
			elif opcion == 4:
				return [0, "Espresso"]
				
			elif opcion == 5:
				retorno = [0,-1]
				return retorno
			elif opcion == 6:
				retorno = [5,-1]
				return retorno
			else:
				print("uwu")
		except:
			cont = 0
			print("Ingrese el número de la opción correspondiente")
	return
		


#Funcion menu principal, en esta funcion se llama a las funciones que piden y procesan parámetros, además de la función que se encarga de preparar el café
def menu():
	opcion = 0
	cantidadCafe = -1
	temperaturaAmbiente = -1
	nivelIntensidad = -1
	tipoPreparacion = -1
	exit = 0;
	while opcion!= 5 and (cantidadCafe == -1 or temperaturaAmbiente == -1 or nivelIntensidad == -1 or tipoPreparacion == -1):		
		parametros = [["Tamaño de Taza",cantidadCafe],["Temperatura Ambiente",temperaturaAmbiente],["Nivel de Intensidad",nivelIntensidad],["Tipo de Preparación",tipoPreparacion]]
		mostrarParametros(parametros)
		print(bcolors.BOLD+bcolors.YELLOW+"Ingrese una de las siguientes opciones: "+ bcolors.ENDC)
		if cantidadCafe == -1:	
			print(bcolors.OKBLUE+"1. Ingresar tamaño de taza [ml]"+bcolors.ENDC)
		else:
			print(bcolors.OKGREEN+"1. Modificar tamaño de taza [ml]"+bcolors.ENDC)
		if temperaturaAmbiente == -1:
			print(bcolors.OKBLUE+"2. Ingresar temperatura ambiente [C°]"+
			bcolors.ENDC)
		else:
			print(bcolors.OKGREEN+"2. Modificar temperatura ambiente [C°]"+bcolors.ENDC)
		if nivelIntensidad == -1:	
			print(bcolors.OKBLUE+"3. Ingresar Nivel de intensidad [1 al 5]"+bcolors.ENDC)
		else:
			print(bcolors.OKGREEN+"3. Modificar Nivel de intensidad [1 al 5]"+bcolors.ENDC)
		if tipoPreparacion == -1:	
			print(bcolors.OKBLUE+"4. Ingresar Tipo de preparacion"+bcolors.ENDC)
		else: 
			print(bcolors.OKGREEN+"4. Modificar Tipo de preparacion"+bcolors.ENDC)
		print(bcolors.RED+"5. Salir"+bcolors.ENDC)
		try:
			opcion = int(input())
			if opcion>5 or opcion<1:
				print("Ingrese una opcion valida")
				opcion = 0
			elif opcion == 1:
				retorno = []
				retorno = recibirCantidad()
				opcion = retorno[0]
				cantidadCafe = retorno[1]
				
			elif opcion == 2:
				retorno = []
				retorno = recibirTemperatura()
				opcion = retorno[0]
				temperaturaAmbiente = retorno[1]
			elif opcion == 3:
				retorno = []
				retorno = recibirNivelIntensidad()
				opcion = retorno[0]
				
				if opcion == 5:
					return
				nivelIntensidad = retorno[1]
			
			elif opcion == 4:
				retorno = []
				retorno = recibirPreparacion()
				opcion = retorno[0]
				if opcion == 5:
					return
				tipoPreparacion = retorno[1]
			
			else:
				exit = 1
		except:
			print("Ingrese el número de la opción correspondiente")
	if exit == 0:#Si se ingresaron todos los parámetros y el usuario no eligió la opción salir:
		print(bcolors.BOLD+bcolors.YELLOW+"Terminó de ingresar todas las opciones"+bcolors.ENDC)
		print(bcolors.BOLD+bcolors.YELLOW+bcolors.UNDERLINE + "Iniciando preparación de café ☕️ ..."+bcolors.ENDC)
		print(bcolors.BOLD+bcolors.YELLOW+bcolors.UNDERLINE + "Preparando ☕️ "+str(tipoPreparacion)+""+bcolors.ENDC)
		preparacionDeCafe(temperaturaAmbiente,cantidadCafe,nivelIntensidad,tipoPreparacion) #Se prepara café
	return

####################Bloque principal ###############################
menu() #Se llama a la funcion menu, que consiste en el menu principal y se encarga de llamar al resto de funciones
