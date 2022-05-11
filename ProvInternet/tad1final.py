#Especificacion
#==============
"""
    Cliente = {
        Nombre: String
        Apellido: String
        nroCli: Int
        Tservicio: String
        fechaAlta: String
        Pservicio: Int
    }

"""

#def crear cliente ():
#crea y retorna un cliente vacio

#def cargarCliente(cliente,nrocliente,nom,ape,alta,tipo,precio)
#Carga los datos en "cliente"

#def verNrocliente(cliente)
#Devuelve el numero de "cliente"

#def verApellido(cliente)
#Devuelve el apellido de "cliente"

#def verNombre(cliente)
#Devuelve el nombre de "cliente"

#def verAlta(cliente)
#Devuelve la fecha de alta del "cliente"

#def verTipo(cliente)
#Devuelve el tipo de servicio del "cliente"

#def verprecio(cliente)
#Devuelve el precio del servicio del "cliente"

#def modNombre(cliente,nom)
#Modifica el nombre de "cliente" por "nom"

#def modApellido(cliente,ape)
#Modifica el apellido de "cliente" por "ape"

#def modAlta(cliente,alta)
#Modifica la fecha de alta de "cliente" por "alta"

#def modTipo(cliente,tipo)
#Modifica el tipo de servicio de "cliente" por "tipo"

#def modPrecio(cliente,precio)
#Modifica el precio de "cliente" por "precio"




def CrearCliente():
    c = ['','',0,'','',0]
    return c

def CargarCliente(c,Nombre,Apellido,NumCliente,TipoS,FechaAlta,Precio):
    c[0]=Nombre
    c[1]=Apellido
    c[2]=NumCliente
    c[3]=TipoS
    c[4]=FechaAlta
    c[5]=Precio
    return c

def verNombre(c):
    return c[0]

def verApellido(c):
    return c[1]

def verNroCli(c):
    return c[2]

def verTservicio(c):
    return c[3]
    
def verFechaAlta(c):
    return c[4]

def verPservicio(c):
    return c[5]
    

def modificarNombre(c,Nombre):
    c[0]=Nombre

def modificarApellido(c,Apellido):
    c[1]=Apellido

def modificarNroCli(c,NumCliente):
    c[2]=int(NumCliente)

def modificarTservicio(c,TipoS):
    c[3]=TipoS
    
def modificarFechaAlta(c,FechaAlta):
    c[4]=FechaAlta
    
def modificarPservicio(c,Precio):
    c[5]=float(Precio)