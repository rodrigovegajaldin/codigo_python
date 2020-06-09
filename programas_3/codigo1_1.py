#este programa practica el manejo de archivos

#este programa practica el uso de la funcion readlines()

from os import strerror

try:
	stream = open("/home/rodrigo/Escritorio/curso_python/documento_1", "rt")
	print(stream.__dict__)

	contar = 0
	ch = stream.readlines(1)
	while len(ch) != 0:
		print(ch,end='')
		contar += 1
		ch = stream.readlines(1)

	stream.close()
	print('El archivo tiene ',contar,'caracteres')

#except IOError:
#	print(IOError.errno)	#este es para ver problemas de apertura
#	print('este es el error de apertura')

except IOError as exc:
	print('Se produjo un error de E/S:', strerror(exc.errno));

