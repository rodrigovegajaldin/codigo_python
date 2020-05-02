#este programa borra los repetidos de una lista 
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 10,10]

#

# coloca tu código aquí

#

lugares=[]

for i in range(len(miLista)-1):

    if miLista[i] in miLista[i+1:]:

        for j in range(i+1,len(miLista)):

            if miLista[i]==miLista[j]:

                if j not in lugares:

                    lugares.append(j)

lugares.sort()

lugares.reverse()

for i in lugares:

    del miLista[i]

#print(lugares)  

print("La lista solo con elementos únicos:")

print(miLista)


