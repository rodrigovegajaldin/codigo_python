#!/usr/bin/env python3
#este progrma hace el juego de TIC TAC TOE

print('\033[5;32;40m')

from random import randrange


def DisplayBoard(board):

#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
	print('\
	+-------+-------+-------+\n\
	|       |       |       |\n\
	|   ',board[0][0],'   |   ',board[0][1],'   |   ',board[0][2],'   |\n\
	|       |       |       |\n\
	+-------+-------+-------+\n\
	|       |       |       |\n\
	|   ',board[1][0],'   |   ',board[1][1],'   |   ',board[1][2],'   |\n\
	|       |       |       |\n\
	+-------+-------+-------+\n\
	|       |       |       |\n\
	|   ',board[2][0],'   |   ',board[2][1],'   |   ',board[2][2],'   |\n\
	|       |       |       |\n\
	+-------+-------+-------+',sep='')

def EnterMove(libres):

#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

	valores=['1','2','3','4','5','6','7','8','9']
	while True:
		usuario=input('Ingresa tu movimiento:')
		if usuario =='':
			continue
		elif usuario not in valores:
			print('Tu movimiento tiene que ser un entero entre 1 y 9')
			continue
		if int(usuario) in libres:
			break	
		else:
			print('Tu lugar esta ocupado')
	return int(usuario)

def MakeListOfFreeFields(board, valor=0, jugador=2):

#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
	if jugador!=2:
		if jugador == 0:
			for fila in range(0,3):
				for lugar in range(0,3):
					if board[fila][lugar]==valor:
						board[fila][lugar]='X'	
		if jugador == 1:
			for fila in range(0,3):
				for lugar in range(0,3):
					if board[fila][lugar]==valor:
						board[fila][lugar]='O'	

	libres=[]
	for fila in board:
		for lugar in fila:
			if type(lugar) == int:
				libres.append(lugar)	
	return board,libres

def VictoryFor(board,libres):

#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
	contx=[[0,0,0],[0,0,0]]
	conto=[[0,0,0],[0,0,0]]
	diagx=[0,0]
	diago=[0,0]

	for filas in range(3):
		for lugar in range(3):
			if board[filas][lugar]=='X':
				contx[0][lugar]+=1
				contx[1][filas]+=1
				if filas==lugar:
					diagx[1]+=1
					if lugar==1:
						diagx[0]+=1
				elif filas==0 and lugar==2 or filas==2 and lugar==0: 	
					diagx[0]+=1

			elif board[filas][lugar]=='O':
				conto[0][lugar]+=1
				conto[1][filas]+=1
				if filas==lugar:
					diago[1]+=1
					if lugar==1:
						diago[0]+=1
				elif filas==0 and lugar==2 or filas==2 and lugar==0: 	
					diago[0]+=1

	print('columnas en x:',contx[0])
	print('filas en x:',contx[1])
	print('diagonal en x/:',diagx[0])
	print('diagonal en x\\:',diagx[1])
	print('columnas en o:',conto[0])
	print('filas en o:',conto[1])
	print('diagonal en o/:',diago[0])
	print('diagonal en o\\:',diago[1])
	

	if 3 in contx[0] or 3 in contx[1] or 3 in diagx:
		print()
		print('GANA COMPUTADORA!!!!!')
		return 'termino'
	elif 3 in conto[0] or 3 in conto[1] or 3 in diago:
		print()
		print('GANA JUGADOR!!!!!!')
		return 'termino'
	elif len(libres)==0:
		print()
		print('TERMINO, NADIE GANA!!!!')
		return 'termino'

def DrawMove(libres):

#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

	while True:
		compu = randrange(10)
		if compu in libres:
			break	
	return compu


board=[[1,2,3],[4,5,6],[7,8,9]]
board,libres=MakeListOfFreeFields(board)

while True: 

	turno = input('Quien empieza, tu o yo?\n')

	if turno =='yo':
		turno=1
		DisplayBoard(board)
		break
	elif turno =='tu':
		turno=0
		break
	else:
		print('Solo estamos jugando tu y yo')


while True:

	if turno == 0:
		valor=DrawMove(libres)
		next_turno=1
	elif turno ==1:
		valor=EnterMove(libres)
		next_turno=0
		
	board,libres=MakeListOfFreeFields(board,valor,turno)
	DisplayBoard(board)
	if turno == 0:
		print('compu:',valor)
	elif turno == 1:
		print('Tu valor fue:',valor)
	print('libres:',libres)
	gana=VictoryFor(board,libres)
	if gana !=None:
		break 
	
	turno=next_turno
		
	#valor=DrawMove(libres)
	#board,libres=MakeListOfFreeFields(board,valor,0)
	#DisplayBoard(board)
	#print('compu:',valor)
	#print('libres:',libres)
	#gana=VictoryFor(board,libres)
	#if gana !=None:
	#	break 

	#valor=EnterMove(libres)
	#board,libres=MakeListOfFreeFields(board,valor,1)
	#DisplayBoard(board)
	#print('tu valor fue:',valor)
	#print('libres:',libres)
	#gana=VictoryFor(board,libres)
	#if gana !=None:
	#	break 

