import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import graficar as graficar

#funcion que define y retorna las funciones de pertenencia para cada consecuente
def cantidadesAguaLecheChocolateCafeTiempo():
	agua = ctrl.Consequent([0, 30, 60, 90, 120, 150, 200, 250, 300, 350, 400, 450], 'agua') #consecuente agua
	agua['poca'] = fuzz.trapmf(agua.universe,[0,0,90,200])
	agua['media'] = fuzz.trapmf(agua.universe,[90,200,250,350])
	agua['mucha'] = fuzz.trapmf(agua.universe,[250,350,450,450])
	cafe = ctrl.Consequent(np.arange(0,30,1),'cafe')#consecuente cafe
	cafe['poca'] = fuzz.trapmf(cafe.universe,[0,0,7,15])
	cafe['media'] = fuzz.trimf(cafe.universe,[10,15,20])
	cafe['mucha'] = fuzz.trapmf(cafe.universe,[15,22,30,30])
	leche = ctrl.Consequent(np.arange(0,50,1),'leche')#consecuente leche
	leche['poca'] = fuzz.trapmf(leche.universe,[0,0,13,25])
	leche['media'] = fuzz.trimf(leche.universe,[13,25,38])
	leche['mucha'] = fuzz.trapmf(leche.universe,[25,38,50,50])
	chocolate = ctrl.Consequent(np.arange(0,80,1),'chocolate')#consecuente chocolate
	chocolate['poca'] = fuzz.trapmf(chocolate.universe,[0,0,20,40])
	chocolate['media'] = fuzz.trimf(chocolate.universe,[20,40,60])
	chocolate['mucha'] = fuzz.trapmf(chocolate.universe,[40,60,80,80])
	tiempo = ctrl.Consequent(np.arange(0,34,1),'tiempo')#consecuente tiempo
	tiempo['poca'] = fuzz.trapmf(tiempo.universe,[0,0,8,17])
	tiempo['media'] = fuzz.trimf(tiempo.universe,[8,17,25])
	tiempo['mucha'] = fuzz.trapmf(tiempo.universe,[17,25,34,34])
	#se grafican todos los consecuentes
	graficar.graficarGrid(agua.universe,cafe.universe,leche.universe,chocolate.universe, tiempo.universe,[agua['poca'].mf,agua['media'].mf,agua['mucha'].mf],[cafe["poca"].mf,cafe["media"].mf,cafe["mucha"].mf],[leche["poca"].mf,leche["media"].mf,leche["mucha"].mf],[chocolate["poca"].mf,chocolate["media"].mf,chocolate["mucha"].mf],[tiempo["poca"].mf,tiempo["media"].mf,tiempo["mucha"].mf],["Poca","Media","Mucha"],["Agua [ml]","Cafe [grs]","Leche [grs]","Chocolate [grs]", "Tiempo [s]"],["Pertenencia","Pertenencia","Pertenencia","Pertenencia"],"Cantidades vs Pertenencia")
	return agua, cafe, leche, chocolate, tiempo
