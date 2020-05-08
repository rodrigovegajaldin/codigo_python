#este programa muestra la serie de fibonacci
#f1= 1
#f2= 1
#f3= f1 + f2 = 1 + 1 = 2
#f4= f2 + f3 = 1 + 2 = 3
#f5= f3 + f4 = 2 + 3 = 5

def fib(n):
	if n < 1:
		return None
	if n < 3:
		return 1
	return fib(n - 1) + fib(n - 2)

valor=int(input('Hasta que valor sera la serie:'))
for n in range(1,valor+1):
	if n < 3:
		print('f',n,' => ',fib(n),sep='')
	else:
		print('f',n,' => f',n-2,' + f',n-1,' = ',fib(n),sep='')
