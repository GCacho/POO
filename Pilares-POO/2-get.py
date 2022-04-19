class A():
    def __init__(self):
        self._cuenta = 0        #Un solo guion bajo es para hacerle entender a otros programadores
        self._contador = 0      #que es un dato encapsulado
    
    @property                   #Decorador para getter: Le decimos a python que este es un metodo get para poder mandar a llamarlo como atributo ejemplo: print(a.cuenta) en lugar de print(a.cuenta()) *nos desasemos del parentesis nada mas* 
    def cuenta(self):
        return self._cuenta     #Este es un ejemplo de metodo get

a = A()
#print(a._cuenta) #mandar a llamar al atributo tambien funciona pero es una mala practica de programacion
print(a.cuenta) #imprime el getter. a.cuenta() asi se tendria que mandar a llamar si no existiera el decorador @property