#este codigo solo sirve pa pruebas
numeroMayor = -99999999
contador = 0

while True:
	numero = input("Ingresa un número o escribe -1 para finalizar el programa:")
	if numero == '':
		print('Tienes que meter un numero')
		continue
	else:
		numero=int(numero)
	if numero == -1:
		break
	else:
		contador = 1
		if numero > numeroMayor:
			numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 
