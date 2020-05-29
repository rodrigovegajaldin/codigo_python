#este programa es un uso mas complejo de los cierres 

def crearcierre(par):
	loc = par
	def potencia(p):
		return p ** loc
	return potencia

fsqr = crearcierre(2)
fcub = crearcierre(3)	#podemos ver que podemos crear los cierres que querramos
for i in range(5):
	print(i, fsqr(i), fcub(i))
