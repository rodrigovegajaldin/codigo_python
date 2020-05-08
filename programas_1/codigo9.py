#este programa elimina las vocales de lo que meta el usuario 
llave=1
while llave:
 recuperada=''
 userWord=input('ingrese una palabra:').upper()
 print(userWord)
 for letra in userWord:
  if letra !='A':
   if letra !='E':
    if letra !='I':
     if letra !='O':
      if letra !='U':
       #print(letra)
       recuperada = recuperada +letra
 print(recuperada,'\n')
 pregunta=input('quieres volver a jugar:')
 if pregunta == 'no':
  llave = 0
	
