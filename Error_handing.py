"""Error handing"""

import sys

#funcion
def division(int1,int2):
	try:
		return int1/int2
	except:
		raise Exception('No se puede dividir entre cero')

def linux_function():
	assert ('linux' in sys.platform), 'This code only runs on Linux'
	print('Doing something')


try:
	linux_function()
except AssertionError as error:
	print(error)
	print('Linux function was not executed')
	#pass (actúa como salto de línea)	

#print(division(0,0))

#El raise sirve para crear una exception que originalmente no existe.
"""Otra forma:
assert ('linux' in sys.platform), 'This code only runs on Linux'
assert (condición), 'mensaje'
"""