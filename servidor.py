import socket
import sys
import ast
import csv

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('0.0.0.1', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio desarrollado.")
    sys.exit(0)

IP = get_ip()  
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en el puerto: ", PUERTO, "en el servidor ", IP, "\n")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IP, PUERTO))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(2)

print ("Servicio configurado en puerto ", PUERTO, "en el servidor ", IP, "\n")
agenda = []
try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ", direccion_cliente)

        while True:
            try:
                recibido = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >> ", recibido)
                if recibido == str(4):
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                elif recibido == str(1):
                    respuesta_servidor = direccion_cliente[0] + " envio: " + "El cliente escogio agregar un nuevo contacto"
                    datos_agenda = socket_cliente.recv(1024).decode('utf-8')
                    print("Datos ingresados: ", datos_agenda)
                    lista_datos = ast.literal_eval(datos_agenda)
                    agenda.append(lista_datos)
                    print(agenda)
                    socket_cliente.send("Datos recibidos".encode("utf-8"))
                
                elif recibido == str(2):
                    busqueda = socket_cliente.recv(1024).decode('utf-8')
                    print("El cliente escogio buscar un contacto")
                    print("nombre a buscar", busqueda)
                    bandera = False
                    for i in agenda:
                        print(i)
                        print(i[0])
                        if str(i[0]) == str(busqueda):
                            bandera = True
                            break
                    if bandera:
                        socket_cliente.send(str(i).encode("utf-8"))
                        bandera = False
                    else:
                        socket_cliente.send("Cliente no encontrado".encode("utf-8"))
                
                elif recibido == str(3):
                    eliminar = socket_cliente.recv(1024).decode('utf-8')
                    print("El cliente escogio buscar un contacto")
                    print("nombre a eliminar", eliminar)
                    bandera = False
                    for i in agenda:
                        print(i)
                        print(i[0])
                        if str(i[0]) == str(eliminar):
                            agenda.remove(i)
                            bandera = True
                            break
                    if bandera:
                        socket_cliente.send("Cliente eliminado con exito".encode("utf-8"))
                        bandera = False
                    else:
                        socket_cliente.send("Cliente no encontrado".encode("utf-8"))
            
            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")