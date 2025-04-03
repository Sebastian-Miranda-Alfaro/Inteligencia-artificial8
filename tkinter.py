from tkinter import *
def mensaje() :
    print("Mensaje del boton")
#Crear ventana
raiz=Tk()
#clase title
raiz.title("ventana de pruebas")
raiz.resizable(True, False)
raiz.geometry("650x350")
raiz.config(bg="blue")
lbl=Label(raiz,text="Esta es una etiqueta")
lbl.pack()
#btn=Button(raiz,text="presiona el boton", bg="yellow",fg = "green",command=mensaje)
#btn.pack()
#btn=Button(raiz, text="Presiona el boton", command=mensaje)
#btn.config(fg="green",bg="yellow")
btn=Button(raiz,text="Presiona el boton", command=mensaje)
btn["fg"]="red"
btn["bg"]="blue"
btn.pack()
raiz.mainloop()
