import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import uwu as u
def recibirCantidad():
	return

def mostrarParametros(parametros):
	#print("holi")
	#print(parametros)
	largo = len(parametros)
	print("")
	for par in parametros:
		if par[1] != -1:
			print(par[0] + ": " + str(par[1]))
	#print("uwu")
	print("")
def recibirTemperatura():
	nivelTemperatura = 0
	
	cont = 0
	
	while True:
		
		print("Ingrese la temperatura ambiente [°C] número entero entre [0,33]: " )
		cambiar = 0
		try:
			nivelTemperatura = int(input())
			cont = 0
			retorno = [0,nivelTemperatura]
			if nivelTemperatura > 33 or nivelTemperatura < 0:
				print("Ingrese un valor entre el intervalo indicado")
			else:
				while cambiar == 0:
					print("Ingresó una temperatura de °" + str(nivelTemperatura)+". ¿Desea cambiarla?")
					print("1. Si")
					print("2. No")
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
	

def recibirNivelIntensidad():
	u.uwu()
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
		



def menu():
	opcion = 0
	cantidadCafe = -1
	temperaturaAmbiente = -1
	nivelIntensidad = -1
	tipoPreparacion = -1
	while opcion!= 5 or (cantidadCafe != -1 and temperaturaAmbiente != -1 and nivelIntensidad != -1 and tipoPreparacion != -1):		
		parametros = [["Cantidad de Café",cantidadCafe],["Temperatura Ambiente",temperaturaAmbiente],["Nivel de Intensidad",nivelIntensidad],["Tipo de Preparación",tipoPreparacion]]
		mostrarParametros(parametros)
		print("Ingrese una de las siguientes opciones: ")
		print("1. Ingresar cantidad de café [ml]")
		print("2. Ingresar temperatura ambiente [C°]")
		print("3. Nivel de intensidad [1 al 5]")
		print("4. Tipo de preparacion")
		print("5. Salir")
		#print("6. Salir")
		try:
			opcion = int(input())
			if opcion>5 or opcion<1:
				print("Ingrese una opcion valida")
				opcion = 0
			elif opcion == 2:
				retorno = []
				retorno = recibirTemperatura()
				opcion = retorno[0]
				temperaturaAmbiente = retorno[1]
				#print("Temperatura Ambiente: " + str(temperaturaAmbiente))
			
			elif opcion == 3:
				retorno = []
				retorno = recibirNivelIntensidad()
				opcion = retorno[0]
				if opcion == 5:
					return
				nivelIntensidad = retorno[1]
				#print("Nivel de Intensidad: " + str(nivelIntensidad))
			
			elif opcion == 4:
				retorno = []
				retorno = recibirPreparacion()
				opcion = retorno[0]
				if opcion == 5:
					return
				tipoPreparacion = retorno[1]
				#print("Retorno: ")
				#print(retorno)
				#print("Tipo preparacion: " + tipoPreparacion)
			else:
				print("UWU")
		except:
			#print("que wea pasa uwu")
			print("Ingrese el número de la opción correspondiente")
	return

menu()
