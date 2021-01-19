"""Dado un texto, encontrar la secuencia alfabética de caracteres
más grande dentro de ella"""

string = input("Ingresa tu cadena: ")
substring = ""
buff = ""
char = ""

for i in string:
	if char < i:
		buff += i #concatena
		if len(buff) > len(substring):
			substring = buff
	else:
		buff = i
	char = i

print('Substring mas largo: ' + substring)

