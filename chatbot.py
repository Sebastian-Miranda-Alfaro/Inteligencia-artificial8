#Ejemplo de chatbot

#Base de conocimiento 
conocimiento ={
    "hola":["Hola!! En que puedo ayudarte?"," Hola como estas?"],
    "adios":["Hasta luego, Que tengas un buen dia", "Adios","Vuelve pronto"],
    "como estas":["Estoy bien, gracias por preguntar","Me siento genial hoy"],
    "que puedes hacer":["Puedo responder preguntas simples",],
    "nombre":["Me llamo chatbot","Soy un chatbot sin nombre "]}
def responder (pregunta):
    pregunta=pregunta.lower()
    for clave in conocimiento:
        if clave in pregunta:
            return conocimiento[clave][0]
    return "Lo siento no puedo entenderte"

#Bucle para interactuar con el usuario 
print("Chatbot: Hola!! Escribe adios para salir")
while True:
    usuario=input("Tu: ").strip().lower()
    if usuario in ["adios", "bye","salir"]:
        print("Chatbot: ", conocimiento["adios"][0])
        break
    respuesta=responder(usuario)
    print("Chatbot: ",respuesta)