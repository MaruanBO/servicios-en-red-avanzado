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


def ipv4():
	ipv4 = raw_input("Introduce el registro A >> ")
	if re.match('^(?:(?:^|\.)(?:2(?:5[0-5]|[0-4]\d)|1?\d?\d)){4}$',ipv4):
		conf = '/etc/bind/zones/db.maruan.sri.iesiliberis.com'
		hostname = 'maruan.sri.iesiliberis.com'
    		zone = dns.zone.from_file(conf, os.path.basename(conf))
    		rdataset = zone.find_rdataset(hostname, dns.rdatatype.A, create=True)
    		rdata = dns.rdtypes.IN.A.A(dns.rdataclass.IN, dns.rdatatype.A, ipv4)
    		rdataset.add(rdata, 86400)
    		zone.to_file(conf)
		print ("Registro ipv4 añadido correctamente")
	else:
		print ("Ipv4 Invalida")


def ipv6():
        ipv6 = raw_input("Introduce el registro AAAA >> ")
        if re.match('(?:(?:(?:[A-f0-9]{1,4}:){6}|(?=(?:[A-f0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![:.\w]))(([0-9A-f]{1,4}:){0,5}|:)((:[0-9A-f]{1,4}){1,5}:|:)|::(?:[A-f0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])|(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?=(?:[A-Fa-f0-9]{0,4}:){0,7}[A-Fa-f0-9]{0,4}(?![:.\w]))(([0-9A-f]{1,4}:){1,7}|:)((:[0-9A-f]{1,4}){1,7}|:)|(?:[A-f0-9]{1-4}:){7}:|:(:[A-f0-9){1,4}){7})(?![:.\w]))',ipv6):
                conf = '/etc/bind/zones/db.maruan.sri.iesiliberis.com'
                hostname = 'maruan.sri.iesiliberis.com'
                zone = dns.zone.from_file(conf, os.path.basename(conf))
                rdataset = zone.find_rdataset(hostname, dns.rdatatype.AAAA, create=True)
                rdata = dns.rdtypes.IN.AAAA.AAAA(dns.rdataclass.IN, dns.rdatatype.AAAA, ipv6)
                rdataset.add(rdata, 86400)
                zone.to_file(conf)
                print ("Registro ipv6 añadido correctamente")
        else:
                print ("Ipv6 Invalida")

# Bucle que se rompe si no seleccionas ninguna opcion
while True:
	menu()
	eligio=int(raw_input("-Selecciona algo :"))

	if eligio==1:
		ipv4()

	elif eligio==2:
		ipv6()

	elif eligio==3:
		print ("Saliendo del programa")
		break
	else:
		print ("Opcion incorrecta")
