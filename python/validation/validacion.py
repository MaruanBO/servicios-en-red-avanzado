#!/usr/bin/env python
import re
import os
# Opciones del menu
print("1. Clave segura")
print("2. Mac delimitada por -")
print("3. IPV4 CIDR")
print("4. IPV6 CIDR")
print("5. URL")


# Bucle que se rompe si no seleccionas ninguna opcion
while True:
	eligio=int(input("-Selecciona algo :"))
	if eligio==1:

		password = raw_input("Introduce una clave >> ")
		#Minimo longitud de 8 valores con digitos, caracteres especiales quitando espacios y letras mayusculas y miniscula
		if re.match('(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', password):
			print("Clave correcta")
		else:
			print("Clave inseguro")

	elif eligio==2:

		mac = raw_input("Mac delimitada por - >> ")
		#Direccion mac mayus y minus limitada por 2 valores y delimitada por -
       		if re.match('^[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}-[0-9A-Fa-f]{2}$',mac):
               		print("Mac correcta")
       		else:
               		print("Mac incorrecta")

	elif eligio==3:

        	ipv4 = raw_input("IPV4 CIDR >> ")
		# IPV4 que soporta la mascara 0-30 limitada por los 3 valores ya que es la /+Digitos
        	if re.match('^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))$',ipv4):
                	print("IPV4 CIDR correcta")
        	else:
                	print("IPV4 CIDR Incorrecta")

	elif eligio==4:
		# Direccion IPV6 limitada por /4,/7.. etc se repite el mismo bloque solo cambia el numero de mascara
        	ipv6 = raw_input("IPV6 CIDR >> ")
        	if re.match('^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(\/((1(1[0-9]|2[0-8]))|([0-9][0-9])|([0-9])))?$',ipv6):
                	print("IPV6 CIDR correcta")
        	else:
                	print("IPV6 CIDR Incorrecta")

        elif eligio==5:

                url = raw_input("URL >> ")
		#Direccion URL https predispuesto por defecto solo se admiten minimo de 3 a 63 valores contando www con un limite de 255 valores y 127 subredes
                if re.match('^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\{3,63}.-]+)+[\w{0,255}\-\._~:/?#[\]@!\$&\(\)\*\+,;=.]+$',url):
                        print("URL correcta")
                else:
                        print("URL Incorrecta")

	else: ## Si no se elige la opcion correcta vuelve a preguntar
       		print "opcion incorrecta"
