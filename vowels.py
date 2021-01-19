#contador de vocales utilizando diccionarios

cadena=input('Introduce una cadena: ').upper()

vocales={
    'A':0,
    'E':0,
    'I':0,
    'O':0,
    'U':0
    }

count=0

for letra in cadena:
    if letra =='A':
        vocales['A']+= 1
    elif letra =='E':
        vocales['E']+= 1
    elif letra =='I':
        vocales['I']+= 1
    elif letra =='O':
        vocales['O']+= 1
    elif letra =='U':
        vocales['U']+= 1

print(f'Cantidad de vocales en el texto:')
print('vocales A: ', vocales['A'])
print('vocales E: ', vocales['E'])
print('vocales I: ', vocales['I'])
print('vocales O: ', vocales['O'])
print('vocales U: ', vocales['U'])