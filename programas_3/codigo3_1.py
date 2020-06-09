#este programa cuenta cuantas veces se repite cada letra del abecedario en un archivo de texto

#este programa hace lo mismo que el anterior pero ordena segun los valores de cada letra pero de mayor a menor y lo guarda en un archivo con el mismo nombre pero con extencion '.hist' al final

from os import strerror

diccionario = {}

while True:
	fuente = input('Dame el archivo fuente:\n')
	if fuente!='':
		break
try:
	for linea in  open(fuente , 'rt'):
		for letra in linea.lower():
			if letra.isalpha():
				if letra in diccionario:
					diccionario[letra] += 1
				else:
					diccionario[letra] = 1		
except IOError as e:
	print('Se produjo un error de E/S: ' , strerror(e.errno))

diccionario2 = {}

for llave , valor in diccionario.items():
	diccionario2[valor] = llave


diccionario = sorted(diccionario2)
diccionario.reverse()
while True:
	destino = input('Dame el archivo destino:\n')
	if destino!='':
		break

try:

	stream2 = open(destino,'wt')

	for valor  in diccionario:
#		print(type(valor),diccionario2[valor])
		stream2.write(diccionario2[valor]+' -> '+str(valor)+'\n')

except IOError as e:
	print('Se produjo un error de E/S: ' , strerror(e.errno))

stream2.close()
print('el programa termino')
