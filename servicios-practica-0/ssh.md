---

### SSH
___

La configuración de ssh es fundamental para contar con seguridad en la tranferencia de archivos. Para contentar tanto clientes como servidores toda comunicación con los dispositivos finales estará encriptada mediante ssh.

Para realizar la practica debemos de contar con

* Router actuando como servidor SSH
* Hosts

### Configuración de SSH de Host a Mikrotik
___

Debemos de contar con una clave publica y privada para poder autentificarnos con Mikrotik.  
* Disponer de un **usuario nuevo** creado para actuar como cliente ssh.
* Permisos del cliente.

El primer paso es bastante sencillo. Debemos de generar una clave pública, para lo que usaremos el comando: 

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
Para poder copiar la clav pública debemos de contar con el paquete FTP instalado, la sintaxis para copiar la clave publica o privada es 
```
ftp + IP
``` 
Posteriormente nos pedira el usuario y la clave, en el caso de mikrotik el usuario es: 
```
admin sin clave
```

Con eso tendremos la clave copiada en **/files** dentro de mikrotik. Nos ubicaremos en mikrotik para importar la clave pública, lo haremos mediante el comando:

```
[admin@mikrotik]> user ssh-keys import public-key-file=id_rsa.pub
```

Una vez copiada correctamente, se podrá acceder al router sin necesidad de una clave.

### Configuración de SSH de Host a Host
___
Debemos de contar con el paquete **OpenSSH**. Hay que tener claro quien es cliente-servidor; el host encargado de copiar la clave actuará de cliente.

Al igual que antes, debemos de contar con un usuario nuevo donde generaremos la clave mediante: 

```
ssh-keygen
```

Una vez generada vamos a copiarla al cliente mediante el comando:

```
ssh-copy-id host@ip
```

Si queremos disponer de mayor seguridad podemos bloquear el acceso al servidor ssh con clave, de esta forma solo quien disponga de la clave publica o privada podrá autentificarse en el servidor. 

Para realizarlo vamos al fichero de configuración de ssh ubicado en **/etc/ssh/sshd_config** y desactivaremos la siguiente directiva: 

```
PasswordAuthentication no 
```




