#este programa convierte de millas/galon a litros/100km y viceversa
def l100kmtompg(liters):

#

# coloca tu código aqui

#

    return 1/(liters*(1.609344/(100*3.785411784)))



def mpgtol100km(miles):

#

# coloca tu código aqui

#

    return 1/(miles*(1.609344/(100*3.785411784)))



print(l100kmtompg(3.9))

print(l100kmtompg(7.5))

print(l100kmtompg(10.))

print(mpgtol100km(60.3))

print(mpgtol100km(31.4))

print(mpgtol100km(23.5))
