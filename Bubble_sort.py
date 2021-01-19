"""Burble Ordenation
peor de los casos: BIG 'O' en sort methods"""

numbers = [3,45,6,7,12,0.2,89,98,12,21,63,85,72,100,23,24]
aux = 0
length = len(numbers)

for i in range[0,length]:
	for j in range[0,(length-1)]:
		aux = numbers[j]
		if numbers[j] > numbers[j+1]:
			numbers[j] = numbers[j+1]
			numbers[j+1] = aux



	print(numbers)