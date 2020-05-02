#este programa es prueba de diaz
#intentar volver mas eficiente
for i in range(1,101):
	if i%3!=0 and i%5!=0: 
		print('el numero: ',i)  
	elif i%3==0 and i%5==0:
		print('fizzbuzz')
	elif i%3==0:
		print('fizz')
	elif i%5==0:
		print('buzz')
