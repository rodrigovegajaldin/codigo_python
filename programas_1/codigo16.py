#este programa muestra la funcion factorial

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)


limite = int(input('ingrese un numero para factorial:'))
print('El factorial de ',limite,'! es:',factorialFun(limite),sep='')
