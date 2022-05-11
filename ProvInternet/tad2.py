#ESTRUCTURA INTERNA

'''
    lista {

        clientes: [c]
    }
'''

#ESPECIFICACION
#
#
#def crearLista():
#Crea un lista
#
#def agregarCliente(l,c):
#Carga un cliente en la lista
#
#def eliminarCliente(l,c):
#Elimina un cliente
#
#
#def recuperarPorPosicion(l,i):
#Retorna el cliente con posicion i de la lista
#
#
#def cantidadTotal(l):
#Retorna la cantidad de clientes que hay en la lista
#
#IMPLEMENTACION

#
#

def crearLista():
#Crea una nueva lista
    l=[]
    return l

def agregarCliente(l,c):
#Carga el cliente a la lista
    l.append(c)

def eliminarCliente(l,c):
#Elimina el cliente pasado por parametro
    l.remove(c)
   
    

        


    




 


def recuperarPorPosicion(l,i):
#Retorna el cliente con posicion i de la lista
    return l[i]

def cantidadTotal(l):
#Retorna la cantidad de clientes que hay en la lista
    return len(l)







    
