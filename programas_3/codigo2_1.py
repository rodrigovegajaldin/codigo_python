#este archivo practica el uso del metodo write() 

#para archivos de tipo binario

from os import strerror

data = bytearray(10)

for i in range(len(data)):
	data[i] = ord('a') + i

try:
	bf = open('/home/rodrigo/Escritorio/curso_python/file.bin', 'wb')
	bf.write(data)
	bf.close()

except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))


#esta parte del programa practica la lectura de archivos binarios


dataleido = bytearray(1)

try:
	streambin = open('/home/rodrigo/Escritorio/curso_python/file.bin','rb')
	leido = streambin.readinto(dataleido)
	while leido != 0:
		print('lei del archivo:',chr(dataleido[0]),'\nlei',leido,'bytes')
		leido = streambin.readinto(dataleido)
	streambin.close()		

except IOError as e:
	print('Se produjo un error de E/S: ',strerror(e.errno))
