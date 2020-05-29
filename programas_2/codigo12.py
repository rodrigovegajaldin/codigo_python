# esta funcion practica el uso de la funcion lambda y de la funcion map()

#utilizamos lambda en esos lugares poq son funciones que queremos pasar pero no necesitamos guardarlas ya que no las volveremos a usar

lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))	

#map() recive dos argumentos el primero es una funcion y el segundo es un iterable, devuelve otro iterable con los resultados de la evaluacion de la funcion en todos los valores del segundo argumento

print(lista2)
for x in map(lambda x: x * x, lista2):
	print(x, end=' ')
print()
