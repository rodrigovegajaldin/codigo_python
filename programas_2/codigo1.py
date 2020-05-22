#este programa prueba el uso de las excepciones


def readint(prompt, min, max):

#

# tu codigo aqui

#

    while True:

        try:

            valor = int(input(prompt))

            assert valor >min and valor<max

        except ValueError:

            print('Error: entrada incorrecta')

            continue

        except AssertionError:

            print('Error: el valor no esta dentro del rango parmitido (min..max)')

            continue

        return valor 

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)



print("El numero es:", v)
