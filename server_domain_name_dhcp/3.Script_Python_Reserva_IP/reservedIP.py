#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

def menu():
        print("1. Reservar direccion ip")
        print("2. Modificar reserva")
        print("3. Eliminar reserva")
        print("4. Salir")


class validate: #clase register tiene 2 metodos ipv4 y mac realizan un regex para los datos introducidos en los campos devolviendo true o false, cortesia de cristina.
        def ipv4(self,ipv4):
                if re.match('^(?:(?:^|\.)(?:2(?:5[0-5]|[0-4]\d)|1?\d?\d)){4}$',ipv4):
                        return True
                else:
                        return False
        def mac(self,mac):
                if re.match('[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}',mac):
                        return True
                else:
                        return False

class register:
        def reservedIp(self,name,mac,ip):
                #Bucle recorre el fichero e inserta los datos en la ultima fila mediante \n
                with open('/etc/dhcp/dhcpd.conf', 'a') as outfile:
                        outfile.write("\nhost"+" "+name+"{\n")
                        outfile.write("\thardware ethernet "+ mac+";"+"\n")
                        outfile.write("\tfixed-address "+ip+";"+"\n")
                        outfile.write("}")
                        print (">> Datos insertados correctamente!")

        def modReservIp(self,h_old,h_new):
                # abrimos el fichero r+b (permite escribir y en modo binario)
                file_mod = open("/etc/dhcp/dhcpd.conf", 'r+b')
                # Leemos el fichero en memoria
                file_content = file_mod.read()
                # Regex para buscar la clave ecriptada
                file_content = re.sub(r"\b{}\b".format(h_old),h_new, file_content)
                # Volvemos al inicio o top del fichero para poder sobrescribir
                file_mod .seek(0)
                # Limpiamos el contenido
                file_mod .truncate()
                # Actualizamos el contenido
                file_mod .write(file_content)
                # Cerramos el fichero
                file_mod.close()
                print ">> Datos modificados correctamente"

        def delReserv(self,host,mac,ip): #Bucle para recorrer una fila en concreto por el valor entregado y cambiarlo por un campo vacio
                                         #De no hacerlo asi modificaremos el fichero introduciendo en el tres veces los valores que ya existen.
                for line in fileinput.input('/etc/dhcp/dhcpd.conf', inplace=1):
                        sys.stdout.write(line.replace('host '+host+' {', ''))
                for line in fileinput.input('/etc/dhcp/dhcpd.conf', inplace=1):
                        sys.stdout.write(line.replace('hardware ethernet '+mac+';', ''))
                for line in fileinput.input('/etc/dhcp/dhcpd.conf', inplace=1):
                        sys.stdout.write(line.replace('fixed-address '+ip+';}', ''))

                print ">> Datos modificados correctamente"



# Bucle que se rompe si no seleccionas ninguna opcion
while True:
        menu()
        eligio=int(raw_input("- Selecciona algo :"))

        if eligio==1:
                mac=raw_input ("- Introduce la dirreción mac: ")
                ip=raw_input ("- Introduce la dirrecion ip a reservar: ")
                name=raw_input ("- Introduce el nombre que deseas darle al cliente a reservar: ")

                #Creamos un nuevo objeto de la clase validate
                re_add = validate()
                #Verificamos la direccion ip y mac y de ser true los introducimos en le fichero
                if re_add.ipv4(ip) == False:
                        print (">> Direccion IPV4 invalida")
                if re_add.mac(mac) == False:
                        print (">> Direccion mac invalida")
                else:
                        add=register()
                        add.reservedIp(name,mac,ip)

        elif eligio==2:
                # Verificacion de datos y inserccion de datos
                h_old= raw_input("-Direccion ip de la reserva a modificar: ")
                h_new= raw_input("-Nueva reserva: ")
                re_add = validate()
                if re_add.ipv4(h_old) == True and re_add.ipv4(h_new) == True:
                        mod=register()
                        mod.modReservIp(h_old,h_new)
                else:
                        print (">> Direccion ip invalida")
 	elif eligio==3:
                host=raw_input("- Host a eliminar: ")
                delIp=raw_input("- Direccion ip de la reserva a eliminar: ")
                delMac=raw_input("- Direccion mac a eliminar: ")
                mod=register()
                mod.delReserv(host,delMac,delIp)
        elif eligio==4:
                print (">> Saliendo del programa")
                break

        else:
                print (">> Opcion incorrecta")



