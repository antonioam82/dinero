# -*- coding:utf-8 -*-
from tkinter import *
import time
import pickle
ventana=Tk()
ventana.title("MI CONTADOR")
ventana.geometry("392x394")
ventana.configure(background="light blue")

def clear():
    global din
    global numero
    global comas
    global modific
    global valor_original
    if modific==True:
        din[0]=valor_original
        pickle.dump(din,open("mi_dinero","wb"))
    input_text.set(din[0])
    numero=""
    comas=0

def coma():
    global numero
    global comas
    if comas==0 and numero!="":
        numero=numero+"."
        input_text.set(numero)
        comas+=1

def num(n):
    global numero
    numero=numero+n
    input_text.set(numero)
    

def suma():
    global din
    global numero
    global simula
    global valor_sim
    global modific
    if numero!="":
        if simula==False:
            din[0]=din[0]+float(numero)
            input_text.set(din[0])
            pickle.dump(din,open("mi_dinero","wb"))
            modific=True
        else:
            valor_sim+=float(numero)
            input_text.set(valor_sim)
        numero=""
        
def resta():
    global din
    global numero
    global simula
    global valor_sim
    global modific
    if numero!="":
        if simula==False:
            din[0]=din[0]-float(numero)
            input_text.set(din[0])
            pickle.dump(din,open("mi_dinero","wb"))
            modific=True
        else:
            valor_sim-=float(numero)
            input_text.set(valor_sim)
        numero=""

def ver():
    global din
    global view
    global numero
    global valor_sim
    if view==False:
        t[-2].config(bg="light green")
        input_text.set(din[0])
        view=True
    else:
        t[-2].config(bg="slategray")
        if simula==True:
            input_text.set(valor_sim)
        else:
            if numero!="":
                input_text.set(numero)
        view=False


def cambiar():
    global simula
    global valor_sim
    global din
    global comas
    global numero
    if simula==False:
        t[-1].config(bg="light green")
        valor_sim=din[0]
        simula=True
    else:
        t[-1].config(bg="slategray")
        input_text.set(din[0])
        numero=""
        simula=False
        valor_sim=0
    comas=0
    

input_text=IntVar()
numero=""
modific=False
simula=False
view=False
comas=0
co_b="slategray"
din=pickle.load(open("mi_dinero","rb"))
valor_original=din[0]
valor_sim=din[0]
t=[]
Label(ventana,text="by doubleA",fg="red",bg="light blue").place(x=1,y=1)
Bsum=Button(ventana,text="SUMAR",bg=co_b,width=48,height=2,command=suma).place(x=21,y=153)
t.append(Bsum)
Bres=Button(ventana,text="RESTAR",bg=co_b,width=48,height=2,command=resta).place(x=21,y=198)
t.append(Bres)
B0=Button(ventana,text="0",bg=co_b,width=4,height=1,command=lambda:num("0")).place(x=21,y=260)
t.append(B0)
B1=Button(ventana,text="1",bg=co_b,width=4,height=1,command=lambda:num("1")).place(x=61,y=260)
t.append(B1)
B2=Button(ventana,text="2",bg=co_b,width=4,height=1,command=lambda:num("2")).place(x=101,y=260)
t.append(B2)
B3=Button(ventana,text="3",bg=co_b,width=4,height=1,command=lambda:num("3")).place(x=141,y=260)
t.append(B3)
B4=Button(ventana,text="4",bg=co_b,width=4,height=1,command=lambda:num("4")).place(x=181,y=260)
t.append(B4)
B5=Button(ventana,text="5",bg=co_b,width=4,height=1,command=lambda:num("5")).place(x=21,y=288)
t.append(B5)
B6=Button(ventana,text="6",bg=co_b,width=4,height=1,command=lambda:num("6")).place(x=61,y=288)
t.append(B6)
B7=Button(ventana,text="7",bg=co_b,width=4,height=1,command=lambda:num("7")).place(x=101,y=288)
t.append(B7)
B8=Button(ventana,text="8",bg=co_b,width=4,height=1,command=lambda:num("8")).place(x=141,y=288)
t.append(B8)
B9=Button(ventana,text="9",bg=co_b,width=4,height=1,command=lambda:num("9")).place(x=181,y=288)
t.append(B9)
Bcoma=Button(ventana,text=",",bg=co_b,width=27,height=1,command=coma).place(x=21,y=320)
t.append(Bcoma)
Bd=Button(ventana,text="DESHACER",bg=co_b,width=27,height=1,command=clear).place(x=21,y=352)
t.append(Bd)
Ba=Button(ventana,text="VALOR ACTUAL",bg=co_b,width=16,height=2,command=ver)
t.append(Ba)
Ba.place(x=247,y=325)
bott=Button(ventana,text="SIMULACIÓN",bg=co_b,width=16,height=2,command=cambiar)
t.append(bott)
bott.place(x=247,y=270)
Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=input_text,bd=20,insertwidth=4,bg="light grey",justify="right").place(x=16,y=60)
clear()

ventana.mainloop()




