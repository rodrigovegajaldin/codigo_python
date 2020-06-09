#este programa cuenta cuantas veces se repite cada letra del abecedario en un archivo de texto

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

for resultado in sorted(diccionario):
	print(resultado , ' -> ' ,  diccionario[resultado])
