# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:52:27 2025

@author: sebas
"""

from tkinter import *
vent=Tk()
vent.title("Ejemplo usando place")
vent.geometry("600x200")

def sumar():
    n1=txt1.get()
    n2=txt2.get()
    resultado=float(n1)+float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,resultado)
def restar():
    n1=txt1.get()
    n2=txt2.get()
    resultado=float(n1)-float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,resultado)
    
def multiplicar():
    n1=txt1.get()
    n2=txt2.get()
    resultado=float(n1)*float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,resultado)

def dividir():
    n1=txt1.get()
    n2=txt2.get()
    resultado=float(n1)/float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,resultado)
 
lbl1=Label(vent,text="Primer numero",bg="yellow")
lbl1.place(x=10,y=10,width=150,height=30) 

txt1=Entry(vent,bg="pink")
txt1.place(x=180, y=10,width=50,height=30)

lbl2=Label(vent,text="Segundo numero",bg="yellow")
lbl2.place(x=10,y=50,width=150,height=30) 

txt2=Entry(vent,bg="pink")
txt2.place(x=180, y=50,width=50,height=30)

btn1=Button(vent,text="Sumar", bg="purple",command=sumar)
btn1.place(x=10,y=160, width=100, height=30)

btn2=Button(vent,text="Restar", bg="green",command=restar)
btn2.place(x=120,y=160, width=100, height=30)

btn3=Button(vent,text="Multiplicar", bg="blue",command=multiplicar)
btn3.place(x=230,y=160, width=100, height=30)

btn4=Button(vent,text="Dividir", bg="yellow",command=dividir)
btn4.place(x=340,y=160, width=100, height=30)

lbl3=Label(vent, text="resultado", bg="green")
lbl3.place(x=10, y=120, width=100, height=30)

txt3=Entry(vent,bg="pink")
txt3.place(x=180, y=120, width=80, height=30)
vent.mainloop()