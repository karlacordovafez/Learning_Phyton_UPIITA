"""Clase for"""
# Estudiantes:
names = ['Abraham','César','Daniel','Daniela','Diego','Edgar']
for name in names:
	print(f'Student: {name}')
else:
	print('No more names\n')

numbers = []
for number in range(0, 21, 2):
	numbers.append(number)
print("\nNumeros de 2 en 2 hasta 21:")
print(numbers)

string = 'Mauricio'
for char in string:
	if char != 'i':
		print(char)	
	else:
		print(f'{char} --- Esta es una letra "i"')
else:
	print('Bye\n')


lista = {1:'Abraham',2:'César',3:'Daniel',4:'Daniela',5:'Diego',6:'Edgar'}
print(lista)
