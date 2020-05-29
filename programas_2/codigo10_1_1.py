#el codigo10_1.py tiene el porblema de que si no se le manda argumentos a los errores este genera problemas

#este codigo soluciona digo problema

#agregamos valores por default a las clases de los errores

class PizzaError(Exception):
	def __init__(self, pizza='desconocida', mensaje=''):
		Exception.__init__(self, mensaje)
		self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
	def __init__(self, pizza='desconocida', queso='>100', mensaje=''):
		PizzaError.__init__(self, pizza, mensaje)
		self.queso = queso


def hacerPizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError
	if queso > 100:
		raise DemasiadoQuesoError
	print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		hacerPizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)

