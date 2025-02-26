meses=("Enero","Febrero","Marzo","Abril","Mayo",
       "Junio","Julio","Agosto","Septiembre","Octubre",
       "Noviembre","Diciembre")
numero=int(input("Introduce un numero: "))
numero-=1
if(numero>=0 and numero <len(meses)):
    print(meses[numero])
else:
    print("error")

#Ejercicio 2
v1=(1,2,3)
v2=(-1,0,2)
ProductoEscalar = (v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])
print(ProductoEscalar)

#Ejercicio 3
creditos={"Matematicas":6,"redes":4,"Sistemas operativos":5}
TotalCreditos = sum(creditos.values())
for materia, credito in creditos.items():
    print(f"Materia: <{materia}> tiene <creditos>: {credito}")
print(f"El total de creditos es {TotalCreditos}")

#Ejercicio 4
clientes = {}
def AñadirCliente():
    nif = input("Ingrese el NIF del cliente: ")
    if nif in clientes:
        print("El cliente ya existe" )
        return
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")

    preferente = input("¿Es un cliente preferente? (sí/no): ").lower()
    preferente = True if preferente in ("si") else False
    clientes[nif] = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }

    print("Cliente añadido correctamente ")

def EliminarCliente():
    nif = input("Ingrese el NIF del cliente a eliminar: ")
    if nif in clientes:
        del clientes[nif]
        print("El cliente ha sido eliminado correctamente.")
    else:
        print("Cliente no encontrado.")

def MostrarCliente():
    nif = input("Ingrese el NIF del cliente a buscar: ")  
    if nif in clientes:
        print("Datos del cliente:")
        for clave, valor in clientes[nif].items():
            print(f"{clave}: {valor}")
    else:
        print("Cliente no encontrado.")

def ListarClientes():
    if not clientes:
        print(" Aun no hay clientes registrados.")
        return
    
    print("Lista de clientes:")
    for nif, datos in clientes.items():
        print(f"{nif}:{datos['nombre']}")

def ListarClientesPreferentes():
    preferentes = {nif: datos for nif, datos in clientes.items() if datos["preferente"]}
    
    if not preferentes:
        print("No hay clientes preferentes registrados.")
        return

    print("Clientes Preferentes:")
    for nif, datos in preferentes.items():
        print(f"{nif}:{datos['nombre']}")

#Menú
while True:
    print("\nMenú de gestión de clientes:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        AñadirCliente()
    elif opcion == "2":
        EliminarCliente()
    elif opcion == "3":
        MostrarCliente()
    elif opcion == "4":
        ListarClientes()
    elif opcion == "5":
        ListarClientesPreferentes()
    elif opcion == "6":
        print("Saliendo del programa ")
        break
    else:
        print("Opción no válida. Intente con un numero del 1-6.")
