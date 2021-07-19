import csv


def agenda():
    print("AGENDA");
    print("Presione '1' Si desea Agregar un nuevo contacto");
    print("Presione '2' Si desea Buscar un contacto");
    print("Presione '3' Si desea Eliminar un contacto");
    print("Presione '4' Si desea Salir");
    
def busqueda():
    print("Presione '5' Si desea realizar una busqueda por nombre");
    print("Presione '6' Si desea realizar una busqueda por telefono");
    print("Presione '7' Si desea realizar una busqueda por direccion");
    
def eliminar():
    print("Presione '8' Si desea eliminar por nombre");
    print("Presione '9' Si desea eliminar por telefono");
    
agendaContact     = []
nombre_contact    = []
telefono_contact  = []
direccion_contact = []

opciones       = 0
opcionBusqueda = 0
opcionEliminar = 0
agenda()

while opciones != 4:
    opciones =  int(input("Ingrese la opcion: "))
    if opciones == 1:
        print("Ingrese el nombre del contacto");
        nombre_contact      = input()
        
        print("Ingrese el numero de teléfono del contacto");
        telefono_contact    = input()
      
        print("Ingrese la direccion del contacto");
        direccion_contact   = input() 
        with open('agenda.csv', 'a') as f:
                writer = csv.writer(f, lineterminator ='\r')
                writer.writerow( (nombre_contact, telefono_contact, direccion_contact) )
        
        
            
    elif opciones == 2:
        busqueda()
        opcionBusqueda = input("¿Por qué opción desea buscar?\n");
        if opcionBusqueda == 5: 
            nombre_contact = input("Nombre contacto buscado:")
            if nombre_contact in telefono_contact: 
                print("Telefono:", telefono_contact[nombre_contact]);
            else:
                print("La busqueda no arroja nada");
                          
        elif opcionBusqueda == 6:
            telefono_contact = input("Telefono contacto buscado:")
            if telefono_contact in nombre_contact:
                print("Nombre:", nombre_contact[telefono_contact]);
            else:
                print("La busqueda no arroja nada");
        
        elif opcionBusqueda == 7:
            direccion_contact = input("Direccion del contacto buscado:")
            if direccion_contact in nombre_contact:
                print("Nombre:", direccion_contact[nombre_contact]);
            else:
                print("La busqueda no arroja nada");
                
    elif opciones == 3:
        eliminar()
        opcionEliminar = int(input("¿Por qué opción desea eliminar?\n"));
        if opcionEliminar == 8: 
            print("Nombre del contacto: ")
            nombre_contact: str(input())
            with open('agenda.csv', 'r') as f:
                reader = list(csv.reader(f))
            with open('agenda.csv', 'w') as f:
                writer = csv.writer(f, lineterminator ='\r')
                for i, row in enumerate(reader):
                    if nombre_contact != row[0]:
                        writer.writerow(row)
                        print("contacto eliminado")