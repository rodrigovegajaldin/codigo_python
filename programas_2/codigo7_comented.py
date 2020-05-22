#este programa practica las clases orientadas a objetos y las pilas
#esta clase hace una pila 

class Pila:	#definimos la clase Pila

	def __init__(self):	#definimos la funcion contructor, es importante poner self para que se especifiquen las propiedades de clase

		self.__listaPila = []	#declaramos la variable como privada poniendo los dos guiones bajo

	def push(self, val):	#pasamos 'self' como parametro a las funciones para q puedan acceder a las propiedades de la clase

		self.__listaPila.append(val)

	def pop(self):

		val = self.__listaPila[-1]
		del self.__listaPila[-1]
		return val


class SumarPila(Pila):   #creamos una subclase que HEREDA las propiedades de Pila y asi especificasmos la superclase

	def __init__(self):

		Pila.__init__(self)	#se tiene que invocar al constructor de la superclase para acceder a sus propiedades
					#se pone self solo si la invocacion esta en el mismo archivo de la superclase 
						#si es desde fuera no se pone self     
		self.__sum = 0	#definimos un nuevo atributo

	def getSuma(self):
		return self.__sum

	def push(self, val):	#RE-definimos la funcion push e instanciamos la funcion push de la superclase 
		self.__sum += val
		Pila.push(self, val)

	def pop(self):
		val = Pila.pop(self)
		self.__sum -= val
		return val

objetoPila = SumarPila()

for i in range(5):
	objetoPila.push(i)

print(objetoPila.getSuma())

for i in range(5):
	print(objetoPila.pop())

print(objetoPila.__dict__)
print(type(objetoPila.__dict__))
