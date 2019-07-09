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
	leche = ctrl.Consequent(np.arange(0,30,1),'cafe')
	leche['poca'] = fuzz.trapmf(cafe.universe,[0,0,7,15])
	leche['media'] = fuzz.trimf(cafe.universe,[10,15,20])
	leche['mucha'] = fuzz.trapmf(cafe.universe,[15,22,30,30])
	chocolate = ctrl.Consequent(np.arange(0,30,1),'cafe')
	chocolate['poca'] = fuzz.trapmf(cafe.universe,[0,0,7,15])
	chocolate['media'] = fuzz.trimf(cafe.universe,[10,15,20])
	chocolate['mucha'] = fuzz.trapmf(cafe.universe,[15,22,30,30])
	
	
	
	#cafe: 0-150
	
	
	#cafe = ctrl.Consequent(np.arange(0, 151, 1), 'cafe')
	#leche = ctrl.Consequent(np.arange(0, 58, 1), 'leche')
	#chocolate = ctrl.Consequent(np.arange(0, 15, 1), 'chocolate')
	#tiempo = ctrl.Consequent(np.arange(1, 4.5, 0.5), 'tiempo')
	graficar.graficar(agua.universe,[agua['poca'].mf,agua['media'].mf,agua['mucha'].mf],["Poca","Media","Mucha"],"Cantidad de Agua[ml]","Grado de pertenencia","Cantidad de Agua")
	#graficar.graficar(leche,[leche["poca"],leche["media"],leche["mucha"]],["Poca","Medio","Mucha"],"Cantidad de Leche[grs]","Grado de pertenencia","Cantidad de Leche")
	graficar.graficar(cafe.universe,[cafe["poca"].mf,cafe["media"].mf,cafe["mucha"].mf],["Poca","Media","Mucha"],"Cantidad de Café[grs]","Grado de pertenencia","Cantidad de Leche")
	#graficar.graficar(chocolate,[chocolate["poca"],chocolate["media"],chocolate["mucha"]],["Poca","Media","Mucha"],"Cantidad de Chocolate[grs]","Grado de pertenencia","Cantidad de Leche")
	#graficar.graficar(tiempo,[tiempo["poca"],tiempo["media"],tiempo["mucha"]],["Poca","Media","Mucha"],"Tiempo[s]","Grado de pertenencia","Cantidad de Tiempo")
	graficar.graficarGrid(agua.universe,cafe.universe,leche.universe,chocolate.universe,[agua['poca'].mf,agua['media'].mf,agua['mucha'].mf],[cafe["poca"].mf,cafe["media"].mf,cafe["mucha"].mf],[leche["poca"].mf,leche["media"].mf,leche["mucha"].mf],[chocolate["poca"].mf,chocolate["media"].mf,chocolate["mucha"].mf],["Poca","Media","Mucha"],["Agua [ml]","Cafe [grs]","Leche [grs]","Chocolate [grs]"],["Pertenencia","Pertenencia","Pertenencia","Pertenencia"],"Cantidades vs Pertenencia")
	return

#graficarGrid(x1,x2,x3,x4,y1,y2,y3,y4,names,xlabel,ylabel,title)


cantidadesAguaLecheChocolateCafeTiempo()
