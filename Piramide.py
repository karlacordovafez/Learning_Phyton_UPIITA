"""Crear una pirámide con la longitud dada como altura"""

longitud = int(input("Ingresa longitud de la piramide: "))

for i in range(0,longitud):
	numero = i+1
	for j in range(0,numero):
		print(numero,end='');
	print()

for i in range(1,longitud):
	numero = longitud - i
	for j in range(0,numero):
		print(numero,end='');
	print()