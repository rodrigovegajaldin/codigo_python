def recivir():
	frase=input('Dame una frase:')
	while True:
		try:
			valor=input('Dame el valor de desplazamiento:')
			assert valor.isdigit() and int(valor) in range(1,26)

		except AssertionError:
			print('el valor tiene que ser un enteroentre 1 - 25')	
			continue	
		return frase,valor

def codificar(frase,valor):
	nueva_cadena=''
	frase=list(frase)
	for letra in frase:
		if letra.isalpha():
			if letra.islower():			
				letra = letra.upper()
				code = ord(letra) + valor
				if code > ord('Z'):
					code = code-ord('Z')+ord('A')-1
				nueva_cadena+=chr(code).lower()
			else:
				code = ord(letra) + valor
				if code > ord('Z'):
					code = code-ord('Z')+ord('A')-1
				nueva_cadena+=chr(code)
		else:
			nueva_cadena+=letra
	return nueva_cadena

frase,valor=recivir()
print(codificar(frase,int(valor)))

