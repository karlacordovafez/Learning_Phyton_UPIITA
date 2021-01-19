"""Algoritmo de Selección"""

numbers = [3,45,6,7,12,0.2,89,98,12,21,63,85,72,100,23,24]
print(numbers)

for i in range(len(numbers)): 
    aux = i 
    for j in range(i+1, len(numbers)): 
        if numbers[aux] > numbers[j]: 
            aux = j        
    numbers[i], numbers[aux] = numbers[aux], numbers[i]

print(numbers)