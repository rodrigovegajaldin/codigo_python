#este programa entrega los numeros primos que van desde el 1-19
def isPrime(num):

#

# coloca tu código aquí

#

    contador=0

    for i in range(2,num):

        if num%i==0:

            contador+=1

    if contador>0:

        return False

    else:

        return True



for i in range(1, 20):

    if isPrime(i + 1):

        print(i + 1, end=" ")

print()
