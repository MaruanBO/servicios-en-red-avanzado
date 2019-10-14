---
title: "Configuración de servidores DHCP-RELAY-SSH en mikrotik"
date : "05-10-2019"
output: "-"
---

### Tabla de contenidos
1. [DHCP RELAY](#nombre-en-minusculas)
2. [DHCP SERVER ](#nombre-en-minusculas)
3. [SSH](#ssh)
4. [Conclusión](#nombre-en-minusculas)
4. [Fuentes](#nombre-en-minusculas)

### Introducción

En este documento veremos la configuración de los servidores SSH, DHCP, RELAY. A continuación veremos el trabajo realizado de cada integrante.
+ Cosmin Marius Turosu
    * Configuración DHCP relay
+ Jose Manuel Corona Villán
    * Configuración DHCP
+ Maruan Boukhriss 
    * Configuración SSH.

Todo lo relaccionado con comunicación entre dispositivos finales fue realizado grupalmente. Cada uno de los integrantes entiende y comprende como poder realizar cualquiera de los puntos explicados en el siguiente documento.
### SSH
___
La configuración de ssh es fundamental para contar con seguridad en la tranferencia de archivos. Para contentar tanto clientes como servidores toda comunicación con los dispositivos finales estara encriptada mediante ssh.
SSH dispone de varios comandos que practicamente hace sencillo cualquier tipo de configuración por esa obvia razón será sencillo la configuración.

Para realizar la practica debemos de contar con

1. Router actuando como servidor SSH
2. Hosts

Para poder realizar gustosamente la practica debemos de conocer las diferentes posibilidades que nos ofrece su configuración

### Configuración de SSH de Host a Mikrotik
___
Debemos de contar con una clave publica y privada para poder autentificarnos con Mikrotik. Es bastante sencillo las unicas precauciones y dolores de cabeza son. 
1. No disponer de un **usuario nuevo** creado para actuar como cliente ssh.
2. Permisos del cliente.

El primero paso es bastante sencillo debemos de generar una clave pública, para generarla usaremos 

```
ssh-keygen
``` 

Este comando generara dos claves ubicadas en ~/.ssh/id_rsa y ~/.ssh/id_rsa.pub.

```
Generating public/private dsa key pair.
Enter file in which to save the key (/home/maruan/.ssh/id_dsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/maruan/.ssh/id_dsa.
Your public key has been saved in /home/maruan/.ssh/id_dsa.pub.
```
Una vez generada vamos copiarla al Mikrotik mediante FTP o SSH. En nuestro caso vamos a copiarlo mediante FTP por rapidez y sencilles, de querer hacerlo mediante SSH debemos de hacerlo mediante **SCP**.

```
ftp 192.168.0.34
Connected to 192.168.0.34.
220 mikrotik FTP server (MikroTik 2.9.18) ready
Name (192.168.0.34:user): admin
331 Password required for admin
Password:
ftp> put id_dsa.pub (**Nos encontramos ubicados en /home/maruan/.ssh/**)
226 ASCII transfer complete
ftp> exit
```
Para poder usar debemos de contar con el paquete FTP instalado, la sintaxis para copiar la clave publica o privada es **ftp + IP**. Posteriormente nos pedira el usuario y la clave, en el caso de mikrotik el usuario es **admin sin clave**.
Con eso tendremos la clave copiada en **/files** dentro de mikrotik. Nos ubicamos en mikrotik para poder importar la clave copiada del cliente. Para importar la clave lo haremos mediante el comando 

```
[admin@mikrotik]> user ssh-keys import public-key-file
```

Una vez copiada correctamente te puedo asegurar que si accedes con el usuario que genero la clave publica podras hacerlo sin clave

### Configuración de SSH de Host a Host
___
Está parte es bastante sencilla es el mismo proceso realizado anteriormente. Debemos de contar con los paquetes **OpenSSH**. Hay que tener claro quien es cliente-servidor, el host encargado de copiar la clave actuará de cliente.
Como lo anteriormente explicado debemos de contar con un usuario nuevo donde generaremos la clave mediante 

```
ssh-keygen
```

Una vez generada vamos a copiarla al cliente mediante el comando 

```
ssh-copy-id host@ip
```
Con esa sintaxis podremos acceder mediante ssh sin clave. Si queremos disponer de mas seguridad podemos bloquear el acceso al servidor ssh con clave, de esta forma solo quien disponga de la clave publica o privada podrá autentificarse en el servidor. Para realizarlo vamos al fichero de configuración de ssh ubicado en **/etc/ssh/sshd_config** y desactivaremos la siguiente directiva 

```
PasswordAuthentication no 
```
### Conclusión
___
### Fuentes
___

Trabajo realizado por:
1. Cosmin Marius Turosu
2. Jose Manuel Corona Villán
3. Marouane Boukhriss



