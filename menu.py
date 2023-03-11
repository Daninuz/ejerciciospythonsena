global lista
listaCitas = []
listaDoctors=[]
#defino los valores
class Usuario:

    def __init__(self, rut, nombre, edad):
        self.rut=rut
        self.nombre=nombre
        self.edad=edad
   

    def solicitarCita(self):
        self.rut = input('Número de cocumento:')
        self.nombre = input('Ingrese su Nombre:')
        self.edad = input('Eps a la que pertenece:')
        listaCitas.append(self)
        print("Exitosamente creada")

    def cancelarCita():
      print("Eliminar cita")
      for x in listaCitas:
       print (x) 

    
    def consultarCita(self):
       print("consulta su cita")
       self.rut=input('Ingrese el numero de documento:')
       #recorrer lista
       for i in listaCitas:
           if self.rut== 'rut':
               print (rut, nombre, edad)


    def solicitardoctor():
        solicituDoctor= ('Daniel gamboa', 'jordi rios', 'mike diaz', 'tatan perez')
        solicituDoctors=[]
        solicituDoctors.append(solicituDoctor)
        print(solicituDoctors)


class Doctor:

    
    def __init__(self, Neim, Lastname, Especialid, Jornad):
        self.nombre=Neim
        self.lastname=Lastname
        self.especialidad=Especialid
        self.jornada=Jornad

class citas:
    def __init__(self, id):
        self.id=id
        self.Doctor= None
        self.usuario = None


def salir():
    print("Gracias por su visita")

def menu():
     #mostrar menu
        print("menu")
        print("1. solicitar cita")
        print("2. cancelar cita")
        print("3. consultar cita")
        print("salir")
        op=input("Digite opcion:")
        return op

while True:
        op = menu()
        if op == '1':
            a.solicitarCita()
            menu()
        elif op == '2':
            a.cancelarCita()
        elif op == '3':
            a.consultarCita()
        elif op == '5':
            menu()
        elif op == '4':
            salir()
            break



menu()