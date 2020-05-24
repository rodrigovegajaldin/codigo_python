#en este programa practicamos la composicion (parecido a la herencia)

import time

class Pistas:
	def cambiardireccion(self, izquierda, on):
		print("pistas: ", izquierda, on)

class Ruedas:
	def cambiardireccion(self, izquierda, on):
		print("ruedas: ", izquierda, on)

class Vehiculo:
	def __init__(self, controlador):
		self.controlador = controlador	# esta es un objeto tipo clase, dependiendo del valor de la variable se convierte en un instanciador de alguna de la superclase 
		print(type(self.controlador))

	def girar(self, izquierda):	#dependiendo de la clase que se invoca llama a metodo 'cambiardireccion' de la clase respectiva
		self.controlador.cambiardireccion(izquierda, True)
		time.sleep(0.25)
		self.controlador.cambiardireccion(izquierda, False)




conRuedas = Vehiculo(Ruedas())	#le pasamos la clase a invocar como argumento 
conPistas = Vehiculo(Pistas())

print()
print('que es el objeto: ',type(conRuedas))
print()

conRuedas.girar(True)
conPistas.girar(False)
