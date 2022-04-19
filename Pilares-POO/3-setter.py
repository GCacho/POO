class A():
    def __init__(self):
        self._cuenta = 0       
        self._contador = 0      
    
    @property                   #Decorador para getter: Le decimos a python que este es un metodo get para poder mandar a llamarlo como atributo ejemplo: print(a.cuenta) en lugar de print(a.cuenta()) *nos desasemos del parentesis nada mas* 
    def cuenta(self):
        return self._cuenta     #Este es un ejemplo de metodo get

    @cuenta.setter              #Decorador para el metodo setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador
    
    @contador.setter                #El set puede faltar pero no el get, eso lo combertiria en un objeto de solo lectura
    def contador(self, contador):
        self._contador = contador

a = A()
#print(a._cuenta) #mandar a llamar al atributo tambien funciona pero es una mala practica de programacion
print(a.cuenta) 
#a._cuenta = 20 #Algo asi seria el metodo get pero con malas practicas de programacion
a.cuenta = 20 #Ya aplica con el metodo setter.
print(a.cuenta)
a.contador = 10
print(a.contador)