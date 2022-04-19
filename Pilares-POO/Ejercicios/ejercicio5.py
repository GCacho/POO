#Crear un programa con tres clases Universidad, con atributos 
#nombre (Donde se almacena el nombre de la Universidad). 
#Otra llamada Carerra, con los atributos especialidad (En donde 
#me guarda la especialidad de un estudiante). Una ultima llamada 
#Estudiante, que tenga como atributos su nombre y edad. 
#El programa debe imprimir la especialidad, edad, nombre y 
#universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self, nombre):
        self.nombre = nombre
    
class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre_estudiante, edad):
        self.nombre_estudiante = nombre_estudiante
        self.edad = edad
        print(f"Nombre: {self.nombre_estudiante}\nEdad: {self.edad} años. \nEspecialidad: {self.especialidad}\nUniversidad: {self.nombre}")

   
if __name__ == "__main__":
    persona = Estudiante("UABCS")
    persona.carrera("Sistemas")
    persona.datos("Guillermo", 26)
