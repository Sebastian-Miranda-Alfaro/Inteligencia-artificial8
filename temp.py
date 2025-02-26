import math

print ("hola mundo")

print("Spyder", "es", "el mejor", sep="-")

print('{} es {}'.format('Python', 'tremendo'))
      
#variables
var= "jonathan"
print (type(var))
len(var)

var_int=10
print (type(var_int))

#booleanos
var_t=True
var_false=False

var1= "perro"
var2= "mascota"
print(var1+ " " + var2)

varint1 = 10
varint2 = 20
multi = varint1 * varint2
print(multi)

al_cuadrado = varint1**2
print(al_cuadrado)

div =varint2/2
print(div)

#importar math

multi2 =round(al_cuadrado*math.pi)
print(multi2)

#operadores de asignacion
x =10
x +=5
x *=2
x -=3

#opeadores de compararcion
x<5 and x<10
x>10 or x<4

#estructuras de control
#while
contador =1
limite=5
while contador <= limite:
    print("se imprime el mensaje #"+ str(contador))
    contador+=1
print("salimos del ciclo")

#if
condicion= True
indice = 0
while condicion:
    if indice <=5:
        print("se imprime el mensaje #"+ str(indice))
        indice+=1
    else:
        print("Hemos llegado al indice maximo")
        break

#for
for i in range(10):
    if i <5:
        print("se imprime el mensaje con indice menor a 5"+str(i))
    elif i >5:
        print("se imprime el mensaje con indice mayor a 5"+str(i))
        break

x=input("Cuantos años tienes?")
print(x)
