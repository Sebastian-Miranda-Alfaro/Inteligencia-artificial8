#Tuplas
t = ('a','b','c','d')
print(type(t))

t1='a'
print(type(t))
t[0]=2 #No se puede asignar valor una vez creada

#Sets
set1={1,2,3,"Sebastian Miranda",1,2,5,10}
#Agregar elementos al set de datos
set1.add("ejemplo")
#Agregar mas de un elemento al set 
set1.update(["a","b","True","False"])
#Eliminar datos de set 
set1.discard("ejemplo")

#Diccionario 
carro={"marca": "ford", "modelo": "mustang", "año": "1964"}
carro.get("modelo")
carro.keys()  #Todas las llaves que tenga el diccionario 
carro.values() #Todos los valores dentro de las llaves
carro.update({"color":"rojo"})

lista_marcas=["ford","audi","seat"]
carros={"marca":lista_marcas}
carros.update({"colores":["rojo","azul","gris"]})

#Crear una tupla
#pedir un numero al usuario y si el numero 
#en la longitud maxima de la tupla,
#muestre el contenido en esa posicion 
#sino, nos muestre un mensaje de error

meses=("Enero","Febrero","Marzo","Abril","Mayo",
       "Junio","Julio","Agosto","Septiembre","Octubre",
       "Noviembre","Diciembre")
numero=int(input("Introduce un numero: "))
if(numero>0 and numero <len(meses)):
    print(meses[numero])
else:
    print("error")
    
#Ejemplo de diccionarios 
#Escribir un programa que pregunte al usuario su nombre
#Edad, direccion y telefono
#que guarde en un diccionario, despues mostrar por pantalla
#el siguiente mensaje 
#nombre tiene edad, vive en la direccion y su numero de 
#telefono es el que nos den 

nombre=input("Cual es tu nombre? ")
edad=input("Cual es tu edad? ")
direccion=input("Cual es tu direccion? ")
telefono=input("Cual es tu telefono? ")

usuario={"nombre":nombre,"edad":edad,"direccion":direccion,
         "telefono":telefono}
print(usuario["nombre"],"tiene",usuario["edad"],"años","vive en",
      usuario["direccion"],"su numero es", usuario["telefono"])
