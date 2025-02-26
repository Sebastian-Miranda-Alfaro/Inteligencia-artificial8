#eJERCICIO 1
edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos: "))

if edad > 16 and ingresos >= 1000:
    print("Tiene que tributar")
else:
    print("No tienes que tributar")
#EJERCICIO 2
Factura = float(input("Ingrese la cantidad sin iva de su factura "))
IVA = input("Ingrese el porcentaje de iva que desea aplicar ")
if IVA == "" : 
    IVA=21
else: 
    IVA = float(IVA)
Total = Factura *(1 + IVA/100) 
print("El total de la Factura es :", Total)
#Ejercicio 3
frase=input("Ingrese una frase ")
letra=input("Ingrese una letra ")
f=frase.count(letra)
print(f"Tu frase tiene {f} letras ")