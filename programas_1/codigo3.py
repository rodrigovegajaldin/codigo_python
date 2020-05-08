hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

x=(min+dura)//60
y=(min+dura)%60
q=(x+hora)%24
print('\nla hora es: ',q,':',y,'\n\nGRACIAS POR USAR EL PROGRAMA')
