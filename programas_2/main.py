from sys import path 

path.append('/home/rodrigo/Escritorio/curso_python/programas_2')

print(path)
import modulo

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo.suml(zeros))
print(modulo.prodl(ones))
