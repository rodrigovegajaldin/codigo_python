#este programa simula un diplay de 7 segmentos 
#utilizamos el diccionario como un switch case


def dibujar(valor):
	leds=[]
	valor = list(str(valor))
	print (valor)
	for i in valor:
		leds.append(valores(int(i)))	
	return leds


def valores(valor):

	elegir={
		1:['  #' for i in range(5)],
		2:['###','  #','###','#  ','###'],
		3:['###','  #','###','  #','###'],
		4:['# #','# #','###','  #','  #'],
		5:['###','#  ','###','  #','###'],
		6:['###','#  ','###','# #','###'],
		7:['###','  #','  #','  #','  #'],
		8:['###','# #','###','# #','###'],
		9:['###','# #','###','  #','###'],
		0:['###','# #','# #','# #','###']
	}
	
	return elegir.get(valor)


while True:
	try: 
		valor = int(input('Dame un numero:'))
		assert valor > 0 
    
	except (ValueError,AssertionError):
		print('Tiene que ser un entero positivo.')        
		continue
	break

grafica=dibujar(valor)
for i in range(5):
	for j in range(len(grafica)):
		print(grafica[j][i],' ',end='')
	print()
	
