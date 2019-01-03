from tkinter import *
import time
import pickle
ventana=Tk()
ventana.title("MI CONTADOR")
ventana.geometry("392x394")

def clear():
    global din
    global numero
    input_text.set(din[0])
    numero=""

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
    if numero!="":
        if simula==False:
            din[0]=din[0]+float(numero)
            input_text.set(din[0])
            pickle.dump(din,open("mi_dinero","wb"))
        else:
            valor_sim+=float(numero)
            input_text.set(valor_sim)
        numero=""
        
def resta():
    global din
    global numero
    global simula
    global valor_sim
    if numero!="":
        if simula==False:
            din[0]=din[0]-float(numero)
            input_text.set(din[0])
            pickle.dump(din,open("mi_dinero","wb"))
        else:
            valor_sim-=float(numero)
            input_text.set(valor_sim)
        numero=""


def cambiar(n):
    global simula
    global valor_sim
    global din
    if simula==False:
        t[n].config(bg="light green")
        valor_sim=din[0]
        simula=True
    else:
        t[n].config(bg="grey")
        simula=False
        valor_sim=0
    

input_text=IntVar()
numero=""
simula=False
comas=0
co_b="grey"
din=pickle.load(open("mi_dinero","rb"))
valor_sim=din[0]
Label(ventana,text="by doubleA",fg="red").place(x=1,y=1)
Button(ventana,text="SUMAR",bg="grey",width=48,height=2,command=suma).place(x=21,y=153)
Button(ventana,text="RESTAR",bg="grey",width=48,height=2,command=resta).place(x=21,y=198)
Button(ventana,text="0",bg=co_b,width=4,height=1,command=lambda:num("0")).place(x=21,y=260)
Button(ventana,text="1",bg=co_b,width=4,height=1,command=lambda:num("1")).place(x=61,y=260)
Button(ventana,text="2",bg=co_b,width=4,height=1,command=lambda:num("2")).place(x=101,y=260)
Button(ventana,text="3",bg=co_b,width=4,height=1,command=lambda:num("3")).place(x=141,y=260)
Button(ventana,text="4",bg=co_b,width=4,height=1,command=lambda:num("4")).place(x=181,y=260)
Button(ventana,text="5",bg=co_b,width=4,height=1,command=lambda:num("5")).place(x=21,y=288)
Button(ventana,text="6",bg=co_b,width=4,height=1,command=lambda:num("6")).place(x=61,y=288)
Button(ventana,text="7",bg=co_b,width=4,height=1,command=lambda:num("7")).place(x=101,y=288)
Button(ventana,text="8",bg=co_b,width=4,height=1,command=lambda:num("8")).place(x=141,y=288)
Button(ventana,text="9",bg=co_b,width=4,height=1,command=lambda:num("9")).place(x=181,y=288)
Button(ventana,text=",",bg=co_b,width=27,height=1,command=coma).place(x=21,y=320)
Button(ventana,text="DESHACER",bg=co_b,width=27,height=1,command=clear).place(x=21,y=352)
t=[]
bott=Button(ventana,text="SIMULACIÓN",bg="grey",width=16,height=2,command=lambda: cambiar(0))
t.append(bott)
bott.place(x=247,y=270)
Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=input_text,bd=20,insertwidth=4,bg="light grey",justify="right").place(x=16,y=60)
clear()

ventana.mainloop()


