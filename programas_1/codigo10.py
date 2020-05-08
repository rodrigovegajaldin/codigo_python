#este programa ordena los numeros que el usuario vaya metiendo

lista=[]
llave=''

while llave!=-1:
	llave = int(input('introduce numero, -1 para terminar:')) 
	if llave!=-1:
		lista.append(llave)
print('odenando...')

for i in range(len(lista)):
	for j in range(i,len(lista)):
		if lista[i]>lista[j]:
			lista[i],lista[j]=lista[j],lista[i]
			print(lista)
#lista.sort()
print('Tu lista ordenada es:',lista)
