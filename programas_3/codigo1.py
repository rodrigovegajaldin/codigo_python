#este programa practica el manejo de archivos
#solo abriremos un fichero

try:
	stream = open("/home/rodrigo/Escritorio/curso_python/documento_1", "rt")
	print(stream.__dict__)
	#texto = stream.read()
	#print(stream.read(1))

	contar = 0
#	ch = stream.read(1)
#	while ch != '':
#		print(ch,end='')
#		contar += 1
#		ch = stream.read(1)

	contenido = stream.read()
	for ch in contenido:
		print(ch, end= '')
		contar += 1

	stream.close()
	print('El archivo tiene ',contar,'caracteres')

#except IOError:
#	print(IOError.errno)	#este es para ver problemas de apertura
#	print('este es el error de apertura')

except Exception as exc:
	print("No se puede abrir el archivo:", exc)
#	print('El archivo no se pudo abrir:', strerror(exc.errno));

