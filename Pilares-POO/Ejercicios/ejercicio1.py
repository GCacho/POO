#Realizar un programa que conste de una clase llamada Estudiante, 
#que tenga como atributos el nombre y la nota del alumno. 
#Definir los métodos para inicializar sus atributos, 
#imprimirlos y mostrar un mensaje con el resultado de la nota 
#y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")
    
    def resultados(self):
        if self.nota < 7:
            print("Haz REPROBADO!")
        else:
            print("Haz APROBADO!")

    @property
    def nombre(self):
        return(self._nombre)
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return(self._nota)
    
    @nota.setter
    def nota(self, nota):
        self._nota = nota

if __name__ == "__main__":
    estudiante1 = Estudiante("Guillermo", 8)
    estudiante1.imprimir()
    estudiante1.resultados()

    estudiante2 = Estudiante("Alejandro", 4)
    estudiante2.imprimir()
    estudiante2.resultados()

