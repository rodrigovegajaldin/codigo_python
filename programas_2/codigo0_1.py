#este programa prueba la libreria matplotlib para graficar 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import threading

#year=[1950,1970,1990,2010]
#pop=[2.519,3.692,5.263,6.972]
#plt.plot(year,pop)
#plt.show()

datos = [1]

def getdata(out_data):
	nuevo = int(input('dame dato:'))
	if len(out_data) >10:
		out_data.pop(0)
	out_data.append(nuevo)

datacolector = threading.Thread(target = getdata, args=(datos))
datacolector.start()

def actualizar(num, hl, data):
	dx = np.array(range(len(data)))
	dy = np.array(data)	
	hl.set_data(x,data)
	return h1,

fig = plt.figure(figsize=(10,8))
plt.ylim(0,20)
plt.xlim(0,200)
hl, = plt.plot(list(range(len(datos))), datos)

line_ani = animation.FuncAnimation(fig, actualizar , fargs = (hl, datos),interval=50 , blit =False)

plt.show()

datacolector.join()




