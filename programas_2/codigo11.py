#este programa practica el uso de los generadores e iteradores class Fib:

#este es un generador en forma de clase

class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		'''Este metodo es el que hace que se reconosca a la clase como un generador, si no se lo pone y se lo usa dentro un iterador (ciclo for) dara error'''
		print("__iter__")		
		return self

	def __next__(self):
		''''Este metodo es el generador propiamente dicho, este metodo se repetira las veces que sea necesario, si no se lo pone dara error poq la clase no tendra valores para generar'''
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n: #tenemos que poner una condicion para detener la iteracion, de lo contrario seguira al infinito
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

for i in Fib(10):
	print(i)
