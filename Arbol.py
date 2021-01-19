"""Arbol inteligente"""

arboles = int(input("Ingresa numero de arboles: "))

for i in range(arboles):
	ciclos = int(input("Ingresa numero de ciclos para el arbol: "))
	altura = 1
	for j in range (ciclos):
		if(j%2 == 0):
			altura *= 2
		else:
			altura+= 1
	print(f'La altura de los arboles es {altura}')