lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
resultado = []

for i, letra in enumerate(lista):
    if (i + 1) % 3 != 0:
        resultado.append(letra)
print(resultado)

#Ejercicio 2

palabra = input("Introduce una palabra: ")
vocales = "aeiou"
conteoVocales = {}
for vocal in vocales:
    conteoVocales[vocal] = palabra.count(vocal)
for vocal, cantidad in conteoVocales.items():
    print(f"La vocal '{vocal}' aparece {cantidad} veces.")
