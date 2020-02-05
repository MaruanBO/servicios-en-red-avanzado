#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

import dns.rdataset
import dns.rdtypes.IN.A
import dns.rdtypes.IN.AAAA
import dns.zone

# Opciones del menu

def menu():
	print("1. Crear registro A dns")
	print("2. Crear registro AAAA dns")
	print("3. Salir")

class validate: #clase register tiene 2 metodos ipv6 y 4 realizan un regex sobre el valor introducido seria la parte de Zona de dominio y una vez
		#verificado lo que hace es añadir el registro
	def ipv4(self,ipv4):
		if re.match('^(?:(?:^|\.)(?:2(?:5[0-5]|[0-4]\d)|1?\d?\d)){4}$',ipv4):
			return True
		else:
			return False
	def ipv6(self,ipv6):
        	if re.match('(?:(?:(?:[A-f0-9]{1,4}:){6}|(?=(?:[A-f0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![:.\w]))(([0-9A-f]{1,4}:){0,5}|:)((:[0-9A-f]{1,4}){1,5}:|:)|::(?:[A-f0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])|(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?=(?:[A-Fa-f0-9]{0,4}:){0,7}[A-Fa-f0-9]{0,4}(?![:.\w]))(([0-9A-f]{1,4}:){1,7}|:)((:[0-9A-f]{1,4}){1,7}|:)|(?:[A-f0-9]{1-4}:){7}:|:(:[A-f0-9){1,4}){7})(?![:.\w]))',ipv6):
			return True
		else:
			return False
class register:

	def ipv4Register(self,ipv4):
		conf = '/etc/bind/zones/db.maruan.sri.iesiliberis.com'
                #Fichero de configuracion y dns
                hostname = 'maruan.sri.iesiliberis.com'
                zone = dns.zone.from_file(conf, os.path.basename(conf))
                rdataset = zone.find_rdataset(hostname, dns.rdatatype.A, create=True)
                rdata = dns.rdtypes.IN.A.A(dns.rdataclass.IN, dns.rdatatype.A, ipv4)
                rdataset.add(rdata, 86400)
                zone.to_file(conf)
                print (">> Registro ipv4 añadido correctamente")

	def ipv6Register(self,ipv6):
		conf = '/etc/bind/zones/db.maruan.sri.iesiliberis.com'
		hostname = 'maruan.sri.iesiliberis.com'
		zone = dns.zone.from_file(conf, os.path.basename(conf))
		rdataset = zone.find_rdataset(hostname, dns.rdatatype.AAAA, create=True)
		rdata = dns.rdtypes.IN.AAAA.AAAA(dns.rdataclass.IN, dns.rdatatype.AAAA, ipv6)
		rdataset.add(rdata, 86400)
		zone.to_file(conf)
		print (">> Registro ipv6 añadido correctamente")

# Bucle que se rompe si no seleccionas ninguna opcion
while True:
	menu()
	eligio=int(raw_input(">> Selecciona algo :"))

	if eligio==1:
		ip = raw_input('Introduce un registro A >> ')
		#Creamos un nuevo objeto de la clase validate
		re_add = validate()
		#Llamamos al metodo sin argumentos ya que se llama asi mismo mediante self
		if re_add.ipv4(ip) == True:
			add=register()
                	add.ipv4Register(ip)
		else:
			print ">> Direccion ipv4 invalida"
		#if val == True:
		#	add=register()
		#	add.ipv4Register(ip)
		#else:
		#	print("ipv4 invalida")

	elif eligio==2:
		ip = raw_input('Introduce un registro AAAA >> ')
		re_add = validate()
		if re_add.ipv6(ip) == True:
                        add=register()
                        add.ipv6Register(ip)
                else:
                        print ">> Direccion ipv6 invalida"


	elif eligio==3:
		print ("Saliendo del programa")
		break
	else:
		print ("Opcion incorrecta")
