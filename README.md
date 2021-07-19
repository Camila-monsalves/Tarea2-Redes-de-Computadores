# Tarea2-Redes-de-Computadores

Integrantes:

-Vania Espinoza 
-Camila Monsalves
-Luis Sepúlveda

Se debe dsarrollar una aplicación cliente-servidor mediante sockets en lenguaje Python, la cual es una agenda que debera hacer las siguientes funcionalidades: ingresar, 
borrar, consultar, nombre, teléfono, dirección

a) #Intalación y clonación de repositorio
Para el correcto funcionamiento de la agenda se deberán hacer los siguientes pasos.

Primero se deberá instalar una terminal ubuntu en su computadora, 
puede hacerlo mediante el siguiente link: https://www.microsoft.com/es-cl/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab

	a1) Luego de hacer la descarga, deberá crear un usuario y una contraseña para acceder y ejecutar los siguientes pasos.

	a2) Para la clonación del repositorio debe estar en ubuntu con su usuario y contraseña creada, y ubicarse en donde quiera guardar los datos.
	para instalar los archivos debe escribir lo siguiente en ubuntu.
	
		git clone https://github.com/camila-monsalves/Tarea2-Redes-de-Computadores.git

	Luego poner el usuario y la contraseña, presionar Enter y esperar la clonación.

b) #Compilación y ejecución de la app
Puede asegurar los archivos se clonaron bien si ingresa el comando 

	ls

Presione Enter y debería existir una carpeta llamada Tarea2-Redes-de-Computadores

	b1) Abrimos el archivo Tarea2-Redes-de-Computadores para lo que debemos escribir el siguiente comando

		cd Tarea2-Redes-de-Computadores

	b2) Ahora con el comando 

		ls 

	Verificamos que existen los archivos 
	cliente.py
	servidor.py
	agenda.csv

	b3) Para compilar primero debemos instalar algunas librerias que son necesarias, por lo que tendremos que poner los siguientes comandos 

	sudo apt install python3-pandas
	sudo add-apt-repository universe
	sudo apt-get update

	
	## SERVIDOR
	Primero que todo debemos compilar el Servidor para poder ejecutar de buena manera la aplicación
	En Ubuntu al servidor.py le asiganmos un puerto (se sugiere puerto 8080) y lo ejecutamos de la siguiente manera
	
	
	python3 servidor.py (Puerto de servicio)

	
	## CLIENTE 
	Luego compilaremos el cliente en otro terminal de Ubuntu
	Ahora haremos el mismo ejercicio con el cliente.py especificando su dirección ip y Puerto de servicio como se puede ver abajo

	python3 cliente.py (Dirección IP + Puerto de servicio)

	












