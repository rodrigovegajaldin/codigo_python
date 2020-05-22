#este programa simula la funcion split() 
#recibe una cadena y la devulve en una lista separando cada palabra por los espacios

def misplit(strng):

#

# coloca tu código aquí

#

    #print(strng)

    #print(len(strng))

    cadena=[]

    cadena2=[]

    aux=''

    try:

        assert len(strng) != 0

        strng = list(strng)

        #print(strng)

        for i in range(len(strng)):

            if ord(strng[i]) != 32:

                aux += strng[i]

                if i == len(strng)-1 and aux != '':

                    cadena.append(aux)

            elif aux !='':

                cadena.append(aux)

                aux=''

    except AssertionError:

        return cadena 

    return cadena



print(misplit("Ser o no ser, esa es la pregunta"))

print(misplit("Ser o no ser,esa es la pregunta"))

print(misplit("   "))

print(misplit(" abc "))

print(misplit(""))
