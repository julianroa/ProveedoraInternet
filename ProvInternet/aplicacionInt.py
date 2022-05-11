#Especificacion
#==============
import datetime
from datetime import date
from dateutil import relativedelta
from tad1final import *
from tad2final3 import *
import os
'''
'''



list= crearLista()

print('=====Bienvenido a la aplicacion de clientes=====')

rta= '0'
i=0

while rta != 8: 
     print("1-Agregar cliente")
     print("2-Modificar cliente")
     print("3-Eliminar cliente")
     print("4-Mostrar listado de clientes")
     print("5-Eliminar clientes con un servicio dado")
     print("6-Realizar descuento en el precio a clientes con antigüedad mayor a 3 años")
     print("7-Mostrar listado de clientes que todavía poseen promoción")
     print("8-Salir")
     rta=int(input("Opción "))
     os.system ("cls")
     if (rta==1):
       
        Nombre= input("Ingrese el nombre del cliente ")
        Apellido= input("Ingrese el apellido del cliente ")
        NumCliente= int(input ("Ingrese el número de cliente "))
        TipoS= input ("Ingrese el tipo de servicio ")
        ingfecha = input('Ingresa una fecha en el formato AAAA-MM-DD ')
        year, month, day = map(int, ingfecha.split('-'))
        FechaAlta = datetime.date(year, month, day)
        Precio= float(input("ingrese el precio del servicio "))

        c=CrearCliente()
        CargarCliente(c,Nombre,Apellido,NumCliente,TipoS,FechaAlta,Precio)

        agregarCliente(list,c)
        print("\n")
        print("Cliente creado y cargado con exito")
        print("\n")
        print("Presione enter para continuar")
        caracter=input()
        os.system("cls")
     elif (rta == 2):
          NumCliente=int(input("Ingrese el numero de cliente del cliente a modificar "))
          for i in range(cantidadTotal(list)):
               c = recuperarPorPosicion(list,i)
               print('...')
               if (verNroCli(c)) == NumCliente:
                    print ("Cliente encontrado")
                    os.system("cls")
                    print ("1-Modificar nombre")
                    print ("2-Modificar apellido")
                    print ("3-Modificar numero de cliente")
                    print ("4-Modificar fecha de alta")
                    print ("5-Modificar tipo de servicio")
                    print("6-Modificar precio de servicio")
                    j=int(input("Opción"))
                    os.system("cls")
                    if (j==1):
                         Nombre=input("Ingrese el nuevo nombre ")
                         modificarNombre(c,Nombre)
                    elif(j==2):
                         Apellido=input("Ingrese el nuevo apellido ")
                         modificarApellido(c,Apellido)
                    elif(j==3):
                         NumCliente=int(input("Ingrese el nuevo numero de cliente "))
                         modificarNroCli(c,NumCliente)
                    elif(j==4):
                         ingfecha = input('Ingresa una fecha en el formato AAAA-MM-DD ')
                         year, month, day = map(int, ingfecha.split('-'))
                         FechaAlta = datetime.date(year, month, day)
                         modificarFechaAlta(c,FechaAlta)
                    elif(j==5):
                         TipoS=input("Ingrese el nuevo tipo de servicio ")
                         modificarTservicio(c,TipoS)
                    elif (j==6):
                         Precio=float(input("Ingrese el nuevo precio de servicio "))
                         modificarPservicio(c,Precio)
     elif (rta==3):
          NumCliente=int(input("Ingrese el numero de cliente del cliente a eliminar "))
          i=0
          while i < (cantidadTotal(list)):
               c = recuperarPorPosicion(list,i)
               print('...')
               if (verNroCli(c)) == NumCliente:
                    print ("Cliente encontrado")
                    print("...")
                    eliminarCliente(list,c)
                    print("Cliente eliminado con exito")
                    i=cantidadTotal(list)+1
                    print ("\n")
                    print ("Presione enter para continuar")
                    cantidad=input()

                    os.system("cls")


               else:
                    i=i+1        


          
     elif (rta==4):
          for i in range(cantidadTotal(list)):
           c = recuperarPorPosicion(list,i)
           print("==========\r\n")
           print(">Nombre: ",verNombre(c))
           print(">Apellido: ",verApellido(c))
           print(">Nro de cliente: ",verNroCli(c))
           print(">Tipo de servicio: ",verTservicio(c))
           print(">Fecha de alta: ",verFechaAlta(c))
           print(">Precio de servicio: ",verPservicio(c))
           print("\n")
           print ("Presione enter para continuar")

           caracter = input()

     elif (rta==5):
          tiservicio=(input("Ingrese el tipo de servicio en minusculas "))
          i=0
          
          while i < (cantidadTotal(list)):
               c = recuperarPorPosicion(list,i)
               print('...')
               if (verTservicio(c).lower()) == tiservicio:
                    print ("Cliente encontrado") 
                    print("...")      
                    eliminarCliente(list,c)
                    print("Cliente eliminado con exito")
                    print("\n")
                    print("-----------------------------")
                    print("\n")
                    i=i-1
                    

          
                    
               else:
                    i=i+1
          print ("\n")     
          print("Presione enter para continuar")   
          cantidad=input()
          os.system("cls")
     elif (rta==6):
          desc=float(input("Ingrese el descuento a realizar (FORMATO = 0,xxx) " ))
          pdesc=float(1-desc)
          for i in range(cantidadTotal(list)):
               c = recuperarPorPosicion(list,i)
               print('...')
               hoy=date.today()
               nanios=relativedelta.relativedelta(hoy,verFechaAlta(c))
               if (nanios.years > 3):
                   
                    modificarPservicio(c,(verPservicio(c)*pdesc))
     elif (rta==7):
          
          for i in range(cantidadTotal(list)):
               c = recuperarPorPosicion(list,i)
               print('...')
               hoy=date.today()
               nmeses=relativedelta.relativedelta(hoy,verFechaAlta(c))
               if (nmeses.months <= 3):
                   
                
                   
                    print("==========\r\n")
                    print(">Nombre: ",verNombre(c))
                    print(">Apellido: ",verApellido(c))
                    print(">Nro de cliente: ",verNroCli(c))
                    print(">Tipo de servicio: ",verTservicio(c))
                    print(">Fecha de alta: ",verFechaAlta(c))
                    print(">Precio de servicio: ",verPservicio(c))

                    print("==========\r\n")

          print ("Presione enter para continuar")                       
          caracter = input()
          os.system("cls")          
     
                
                





