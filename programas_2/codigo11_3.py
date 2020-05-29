#este es un programa que prectica los generadores usando listas de compresion

#generador en forma de lista de compresion

lst = tuple([1 if x % 2 == 0 else 0 for x in range(10)])
genr = (1 if x % 2 == 0 else 0 for x in range(10))

print(type(lst), type(genr))	#aqui podemos comprobar que genr es un genrador 

for v in lst:
	print(v, end=" ")
print()

for v in genr:
	print(v, end=" ")
print()
