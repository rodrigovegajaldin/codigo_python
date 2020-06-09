#este programa lee un archivo de nombres implementando todos los errores posibles

from os import strerror

class ExcepcionDatosAlumnos(Exception):
	pass

class LineaErronea(ExcepcionDatosAlumnos):
	# coloca tu código aquí
	def __init__(self , linea = '', mensaje = ''):
		ExcepcionDatosAlumnos.__init__(self , mensaje)
		self.linea = linea
        
class ArchivoVacio(ExcepcionDatosAlumnos):
	# coloca tu código aquí
	def __init__(self , archivovacio ='', mensaje='' ):
		ExcepcionDatosAlumnos.__init__(self, mensaje)
		self.archivovacio = archivovacio
try:
	while True:
		archivo = input('Dame el archivo:\n')
		if archivo!='':
			break
		print('La linea esta vacia')
	diccionario = {}

	stream = open(archivo , 'rt')
	contador = 0
		
            
	for lineas in stream:
		nombre = ''
		nota = 0

		lineas = lineas[:-1]
		for espacio in lineas.split(' '):
#			print(type(espacio),espacio.isalnum(), len(espacio),espacio)
			if espacio.isalnum():
				
				if espacio.isalpha():
					nombre += ' '+espacio 
#					print(nombre)
				elif espacio.isdigit():
					nota += int(espacio)
#					print(nota)
				else:
					raise LineaErronea(lineas , 'La linea esta mal escrita !!!')

			elif espacio == '':
				continue

			else:
				raise LineaErronea(lineas , 'La linea esta mal escrita !!!')

		nombre = nombre.replace(' ' , '' ,1)		            
		if nombre in diccionario:
			diccionario[nombre] += nota

		else:
			diccionario[nombre] = nota
		contador += 1

	print(contador)
	if contador == 0:
		fichero = archivo.split('/')
		raise ArchivoVacio(fichero[-1],'Este archivo esta vacio:') 

	print(diccionario)
	stream.close()

except IOError as e:
	print('Se produjo un error de E/S: ', strerror(e.errno))
    
except LineaErronea as le:
	print(le , '\n\t' , le.linea)

except ArchivoVacio as av:
	print(av , '\n\t' , av.archivovacio)
