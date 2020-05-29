#este programa tambien practica el uso de la funcion lambda pero con la funcion filter()

from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

#la funcion filter recibe una funcion condicion y un iterable, y devuelve un iterable con los valores del segundo argumento que pasen la condicion

print(data)
print(filtered)
