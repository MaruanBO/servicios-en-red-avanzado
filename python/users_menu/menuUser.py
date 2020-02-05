#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import fileinput
import hashlib


# Opciones del menu
def menu():
	print("1. Iniciar sesión")
	print("2. Registar usuario")
	print("3. Modificar usuario")
	print("4. Salir")

# Bucle que se rompe si no seleccionas ninguna opcion
while True:
	menu()
	eligio=int(raw_input("-Selecciona algo :"))
	if eligio==1:
	        username_log = raw_input("Introduce el usuario: ")
                password_log = raw_input("Introduce la clave: ")
                searchKey = hashlib.sha256(password_log).hexdigest()
                lines = open("accountMenu.txt", "r" ).readlines()
                # Verficicación de si existe el usuario en la el fichero
                for line in lines:
                        if re.search(searchKey, line ):
                        	print "Login realizado correctamente"
	elif eligio==2:
		username_log = raw_input("Introduce el usuario: ")
                password_log = raw_input("Introduce la clave: ")
		newPassword = hashlib.sha256(password_log).hexdigest()
		#Introducimos el usuarios delimitado por :
		file = open("accountMenu.txt","a")
		file.write (username_log)
		file.write (":")
		file.write (newPassword)
		file.write("\n")
		file.close()
		print ("Registrado correctamente.")

	elif eligio==3:
		print "De no existir el usuario se saldra del programa"
		password_old = raw_input("Introduce la antigua clave del usuario modificar: ")
                password_new = raw_input("Introduce la nueva clave para el usuario:")
                h_old = hashlib.sha256(password_old).hexdigest()
		h_new = hashlib.sha256(password_new).hexdigest()
	 	lines = open("accountMenu.txt", "r" ).readlines()

		# Verficicación para evitar introducir valores sin que la clave exista
                for line in lines:
                        if re.search(h_old, line ):
				# Misma clave verificacion:
				if h_old == h_new:
                        		print("No puede usar la misma clave")
                		else:
					# abrimos el fichero r+b (permite escribir y en modo binario)
					file_mod = open("accountMenu.txt", 'r+b')
					# Leemos el fichero en memoria
					file_content = file_mod.read()
					# Regex para buscar la clave ecriptada
					file_content = re.sub(r"\b{}\b".format(h_old),h_new, file_content)
					# Volvemos al inicio del fichero para poder sobrescribir
					file_mod .seek(0)
					# Limpiamos el contenido
					file_mod .truncate()
					# Actualizamos el contenido
					file_mod .write(file_content)
					# Cerramos el fichero
					file_mod.close()
					print "Datos modificados correctamente"
	elif eligio==4:
		print "Saliendo del programa"
		break
	else:
		print "Opcion incorrecta"
