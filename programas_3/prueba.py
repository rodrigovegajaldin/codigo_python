
from os import strerror

try:

	stream = open('/home/rodrigo/Escritorio/curso_python/codigo.txt' , 'rt')


	dato = stream.read()
	print('dato:',len(dato))

	while dato != '':
		print('dato:',len(dato))
		print('este es el dato:',dato,'!!!')
		dato = stream.read()

	print('termino de leer')

	stream.close()

except IOError as e:
	print('error E/S: ' , strerror(e.errno))
