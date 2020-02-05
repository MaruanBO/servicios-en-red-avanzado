#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Parametros:
filename="credenciales.txt"
delim=":"
# Abrir fichero en lectura
file_in_Line = open(filename, "r")
# Leer lineas
line = file_in_Line.readline()
#Bucle para recorrer el fichero
while line:
	index=line.split(delim)
	#Obtenemos usuario y clave
	user=index[0]
	passwd=index[1]
	# While anindado para leer los el usuario y clave
	line = file_in_Line.readline()
	username=raw_input('Enter username: ')
	password=raw_input('Enter password: ')
	#Compara los datos introducidos con la clave del fichero
	if username == user or password == passwd:
		print("Bienvenido: "+user)
		break
	else:
		print('Clave o Contraseña incorrecta')
