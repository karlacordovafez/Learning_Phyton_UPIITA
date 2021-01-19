"""Clase de while"""

count = 0
loop = True

while loop:
	print(count)
	count+=1
	if count == 100:
		loop = False

numbers = []
i=0
while i<21:
	i=i+2
	numbers.append(i)

print("\nNumeros de 2 en 2 hasta 21:")
print(numbers)

