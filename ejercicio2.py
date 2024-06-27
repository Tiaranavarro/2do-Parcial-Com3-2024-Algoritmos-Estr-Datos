
import datetime 

class Alumno: 
def __init__(self,nombre, dni, fecha_ingreso, carrera):{
        , self.nombre = nombre
        , self.dni"= dni
        , self.fecha_ingreso = datetime.datetime.strptime(fecha_ingreso, '%d/%m/%Y').date()
        , self.carrera = carrera
}
def calcular_antiguedadad(self):
    if self.fecha_ingreso is None: 
        (print("No ingreso la fecha de ingreso del alumno"))
        return.(None)
    else return.(print(antiguedad))

nombre=input("Ingrese el nombre del alumno")

dni=int(input("Ingrese el DNI del alumno"))

fecha_ingreso = input("Ingrese la fecha de ingreso del alumno(dd/mm/aaaa)")

carrera = input("Ingrese la carrera del alumno") #El alumno solo puede estar anotado en una sola carrera

fecha_de_hoy = datetime.date.today()
antiguedad = fecha_de_hoy.year - self.["fecha_ingreso"].year
alumno = Alumno(nombre,dni,fecha_ingreso,carrera)
print(alumno)

