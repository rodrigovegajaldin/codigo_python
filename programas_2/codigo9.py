#Este programa prueba el uso de las clases 

class ListaContactos(list):
	def buscar(self, nombre):
		'''Devuelve todos los contactos que continen el valor 
		de busqueda en su nombre.'''
		contactos_coincidentes = []
		for contacto in self:
			print(contacto.nombre , contacto.email , contacto.telefono)
			if nombre in contacto.nombre:
				contactos_coincidentes.append(contacto)
		return contactos_coincidentes

class  Contacto:
	todos_contactos = ListaContactos()
	
	def __init__(self, nombre, email):
		self.nombre = nombre 
		self.email = email
		Contacto.todos_contactos.append(self)

class Vendedor(Contacto):
	def __init__(self, nombre, email, telefono):
		self.telefono = telefono
		Contacto.__init__(self, nombre, email)
		
	def pedido(self, pedido):
		print('en una aplicacion completa enviaria el pedido {} pedido a {}'.format(pedido,self.nombre))


#from codigo9 import ListaContactos, Contacto, Vendedor
#c1 = Contacto('Juan A', 'juana@cualquiera.net')
#c2 = Contacto('Juan B', 'juanb@cualquiera.net')
#c3 = Contacto('Jose c', 'josec@cualquiera.net')

ac1 = Vendedor('Juan A', 'juana@cualquiera.net', '1234567')
ac2 = Vendedor('Juan B', 'juanb@cualquiera.net', '7654321')
ac3 = Vendedor('Jose c', 'josec@cualquiera.net', '7979674')

[c.nombre for c in Contacto.todos_contactos.buscar('Juan')]	#buscamos todos los contactos que tengan el nombre Juan

print([[c.nombre, c.email, c.telefono] for c in Contacto.todos_contactos])

	#todos los contactos estan guardados en la variable de clase Contacto.todos_contactos en forma de lista
		#pero esta variable es un objeto de la clase


class NombreLargoDict(dict):	#estamos heredando la clase dict
	def clave_maslarga(self):
		maslarga = None
		for key in self:
			if not maslarga or len(key) > len(maslarga):
				maslarga = key
		return maslarga


#from codigo9 import NombreLargoDict
clavelarga = NombreLargoDict()
clavelarga['hola'] = 1
clavelarga['la mas larga'] = 5
print(clavelarga.clave_maslarga())
print(clavelarga)	#en este caso la lista se guarda en EL OBJETO CLAVELARGA
