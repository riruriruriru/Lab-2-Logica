import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import graficar as graficar


def cantidadesAguaLecheChocolateCafeTiempo():
	agua = ctrl.Consequent([0, 30, 60, 90, 120, 150, 200, 250, 300, 350, 400, 450], 'agua')
	agua['poca'] = fuzz.trapmf(agua.universe,[0,0,150,250])
	agua['media'] = fuzz.trimf(agua.universe,[150,250,350])
	agua['mucha'] = fuzz.trapmf(agua.universe,[250,350,450,450])
	cafe = ctrl.Consequent(np.arange(0,30,1),'cafe')
	cafe['poca'] = fuzz.trapmf(cafe.universe,[0,0,7,15])
	cafe['media'] = fuzz.trimf(cafe.universe,[10,15,20])
	cafe['mucha'] = fuzz.trapmf(cafe.universe,[15,22,30,30])
	leche = ctrl.Consequent(np.arange(0,340,1),'leche')
	leche['poca'] = fuzz.trapmf(leche.universe,[0,0,85,170])
	leche['media'] = fuzz.trimf(leche.universe,[85,170,255])
	leche['mucha'] = fuzz.trapmf(leche.universe,[170,255,340,340])
	chocolate = ctrl.Consequent(np.arange(0,80,1),'chocolate')
	chocolate['poca'] = fuzz.trapmf(chocolate.universe,[0,0,20,40])
	chocolate['media'] = fuzz.trimf(chocolate.universe,[20,40,60])
	chocolate['mucha'] = fuzz.trapmf(chocolate.universe,[40,60,80,80])
	tiempo = ctrl.Consequent(np.arange(0,34,1),'tiempo')
	tiempo['poca'] = fuzz.trapmf(tiempo.universe,[0,0,8,17])
	tiempo['media'] = fuzz.trimf(tiempo.universe,[8,17,25])
	tiempo['mucha'] = fuzz.trapmf(tiempo.universe,[17,25,34,34])
	
	#graficar.graficar(agua.universe,[agua['poca'].mf,agua['media'].mf,agua['mucha'].mf],["Poca","Media","Mucha"],"Cantidad de Agua[ml]","Grado de pertenencia","Cantidad de Agua")
	#graficar.graficar(leche,[leche["poca"],leche["media"],leche["mucha"]],["Poca","Medio","Mucha"],"Cantidad de Leche[grs]","Grado de pertenencia","Cantidad de Leche")
	#graficar.graficar(cafe.universe,[cafe["poca"].mf,cafe["media"].mf,cafe["mucha"].mf],["Poca","Media","Mucha"],"Cantidad de Café[grs]","Grado de pertenencia","Cantidad de Leche")
	#graficar.graficar(tiempo.universe,[tiempo["poca"].mf,tiempo["media"].mf,tiempo["mucha"].mf],["Poca","Media","Mucha"],"Tiempo en segundos","Grado de pertenencia","Tiempo")
	#graficar.graficar(chocolate,[chocolate["poca"],chocolate["media"],chocolate["mucha"]],["Poca","Media","Mucha"],"Cantidad de Chocolate[grs]","Grado de pertenencia","Cantidad de Leche")
	#graficar.graficar(tiempo,[tiempo["poca"],tiempo["media"],tiempo["mucha"]],["Poca","Media","Mucha"],"Tiempo[s]","Grado de pertenencia","Cantidad de Tiempo")
	graficar.graficarGrid(agua.universe,cafe.universe,leche.universe,chocolate.universe, tiempo.universe,[agua['poca'].mf,agua['media'].mf,agua['mucha'].mf],[cafe["poca"].mf,cafe["media"].mf,cafe["mucha"].mf],[leche["poca"].mf,leche["media"].mf,leche["mucha"].mf],[chocolate["poca"].mf,chocolate["media"].mf,chocolate["mucha"].mf],[tiempo["poca"].mf,tiempo["media"].mf,tiempo["mucha"].mf],["Poca","Media","Mucha"],["Agua [ml]","Cafe [grs]","Leche [grs]","Chocolate [grs]", "Tiempo [s]"],["Pertenencia","Pertenencia","Pertenencia","Pertenencia"],"Cantidades vs Pertenencia")
	return agua, cafe, leche, chocolate, tiempo

#graficarGrid(x1,x2,x3,x4,y1,y2,y3,y4,names,xlabel,ylabel,title)


