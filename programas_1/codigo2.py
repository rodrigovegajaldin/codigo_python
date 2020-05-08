hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
minuto_total=min+dura
minuto2=60//minuto_total
minuto3=1-minuto2
minuto_final=int(((minuto_total-60)*minuto3)+(minuto_total*minuto2))

hora_total=hora+minuto3
hora2=24//hora_total
hora3=1-hora2
hora_final=int(((hora_total-23)*hora3)+(hora_total*hora2))
print('la hora actual es: ',hora_final,':',minuto_final

