from VALID import ns, OK
import pickle
import time
import subprocess

moneda=pickle.load(open("divisa.mio","rb"))
if moneda==(" "):
    divisa=input("Introduce divisa: ")
    pickle.dump(divisa,open("divisa.mio","wb"))


def moneda(n):
    moneda=pickle.load(open("divisa.mio","rb"))
    if n==1:
        Moneda=moneda
    else:
        Moneda=list(moneda)
        if Moneda[-1]==("a") or Moneda[-1]==("e") or Moneda[-1]==("i") or Moneda[-1]==("u") or Moneda[-1]==("o"):
            Moneda=moneda+"s"
        else:
            Moneda=moneda+"es"
    return Moneda

def valid_password(c):
    if len(c)<5 or len(c)>18:
        c=valid_password(input("La contraseña ha de tener entre 5 y 18 caracteres: "))
    if not any(i.isdigit() for i in c):
        c=valid_password(input("La contraseña ha de contener, al menos, un digito: "))
    return c
        
contraseña=pickle.load(open("contraseña.mio","rb"))
print("*****************ACCESO POR CONTRASEÑA*****************")
if contraseña==(" "):
    time.sleep(1)
    print("ANTES DE EMPEZAR DEBES ESTABLECER UNA CONTRASEÑA")
    contraseña=valid_password(input("Establecer contraseña: "))
    pickle.dump(contraseña,open("contraseña.mio","wb"))
    subprocess.call(["cmd.exe","/C","cls"])
else:
    print("")
    print("¿Que desea hacer:")
    print("A)Acceder mediante contraseña actual")
    print("B)Cambiar contraseña actual")
    print("")
    opcion=input("Escriba aquí su opción: ")
    while opcion!=("A") and opcion!=("B"):
        opcion=input("Escriba solo \'A\' o \'B\' según su opción: ")
    if opcion==("A"):
        contra=input("Introduce contraseña: ")
        while contra!=contraseña:
            print(chr(7));contra=input("Contraseña incorrecta: ")

    else:
        contra=input("Introduce contraseña actual: ")
        while contra!=contraseña:
            contra=input("Contraseña no válida: ")
        nueva_contra=valid_password(input("Introduce nueva contraseña: "))
        contraseña=nueva_contra
        pickle.dump(contraseña,open("contraseña.mio","wb"))
    subprocess.call(["cmd.exe","/C","cls"])

while True:
    print("***********BIENVENIDO AL GESTOR DE SU DINERO***********")
    saldo=pickle.load(open("dinero.mio","rb"))
    print("")
    print("¿Que desea hacer?:")
    print("A)Ver saldo actual.")
    print("B)Introducir cambios en el saldo.")
    print("C)Realizar simulación.")
    print("D)Cambiar de moneda.")
    print("")
    op=input("Introduzca aquí su opción: ")
    while op!=("A") and op!=("B") and op!=("C") and op!=("D"):
        op=input("Escriba solo \'A\', \'B\' o \'C\' según su opción: ")
    if op==("A"):
        print("Su saldo actual es de",saldo[0],moneda(saldo[0]))
    else:
        if op==("D"):
            divisa=input("Introduce nueva divisa: ")
            pickle.dump(divisa,open("divisa.mio","wb"))
        else:
            oper=("")
            DIN=0
            if op==("C"):
                print("SIMULACION")
            while oper!=("="):
                oper=input("Introduce tipo de operación: ")
                while oper!=("+") and oper!=("-") and oper!=("="):
                    oper=input("Escribe \'+\',\'-\' o \'=\' según el tipo de operación que dese realizar: ")
                if oper==("+"):
                    euros=OK(input("Introduce cantidad: "))
                    DIN+=euros
                if oper==("-"):
                    euros=OK(input("Introduzca cantidad: "))
                    DIN-=euros
            saldo[0]=saldo[0]+DIN
            if op==("B"):
                pickle.dump(saldo,open("dinero.mio","wb"))
                print("El saldo, ahora, es de",saldo[0],moneda(saldo[0]))
            else:
                print("Tras la operación simulada su saldo sería de",saldo[0],moneda(saldo[0]))
            
    c=ns(input("¿Desea continuar?: "))
    if c==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
        
            
        
    


            
