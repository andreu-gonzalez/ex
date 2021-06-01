from sala import sala
from salacontroller import salacontroller
from datetime import datetime 
import string
con = salacontroller()
import random
x=1
while True:
    print("1 Aadir sala")
    print("2- Reservar una sala")
    print("3-Listar finalizados")
    print("4-Finalizar reservas")
    while True:
        try:
            opcion=int(input("Que opcion eliges"))
            break
        except ValueError:
            print("Solo numeros")  

    if opcion == 1:
        l = random.choice(string.ascii_letters)
        l2 = random.choice(string.ascii_letters)
        l3 = random.choice(string.ascii_letters)

        nombre = l + l2 +l3 + str(x)
       
        x=x+1

        print(nombre)
        while True:
            try:         
                precio = float(input("Dime el precio "))
                break
            except ValueError:
                print("Tiene que ser un numero ")  
        while True:
            try:         
                capacidad = int(input("Dime la capacidad "))
                break
            except ValueError:
                print("Tiene que ser un numero") 

        sal = sala(nombre,capacidad,precio)

        if con.addsala(sal):
            print("Se ha guardado") 
        else:
            print("No se ha guardado") 
    if opcion ==2:
        nombre=input("Dime el nombre")
        while True:
            dni = input("Dime el dni ")
            if dni =="":
                print("Dni vacio")
            elif con.Comprobardni(dni) :
                print("DNI es valido")
                break
            else:
                print("DNI no es valido")
        while True:        
            try: 
                day=input("pon la fecha")
                date_format='%d/%m/%Y'
                date_day = datetime.strptime(day, date_format)
                break
            except ValueError:
                 print("Tiene que ser del formato dd/mm/yyyy")    
        if con.registrarevento(nombre,dni,date_day):
            print("se ha guardado")
        else:
            print("no se ha guradado")    
        lista = con.listar()
        for i in lista:
            print("reserva ",lista[i].getReservas())
    if opcion==3:
        print("LISTAR SALAS")
        lista = con.listar()
        for i in lista:
            if len(lista[i].mostrarParticipantes()):
                print("Nombre ",lista[i].getNombre())
                print("Capacidad ",lista[i].getCapacidad())
                print("Precio ",lista[i].getPrecio())
                print("Acumulados ",lista[i].getAcumulados())
                print("Num reserva ",lista[i].getNumreserva())
                print("reserva ",lista[i].getReservas())
                print("Finalizado ",lista[i].mostrarParticipantes())
    if opcion==4:
        nombre=input("Dime el nombre ")
        while True:
            dni = input("Dime el dni ")
            if dni =="":
                print("Dni vacio")
            elif con.Comprobardni(dni):
                print("DNI es valido")
                break
            else:
                print("DNI no es valido")
        while True:        
            try: 
                day=input("pon la fecha ")
                date_format='%d/%m/%Y'
                date_day = datetime.strptime(day, date_format)
                break
            except ValueError:
                 print("Tiene que ser del formato dd/mm/yyyy ")       
        if con.registrarfinalizado(nombre,dni,date_day):
            print("Registro del finalizado")
        else:
            print("No se ha registrado") 



        
      
