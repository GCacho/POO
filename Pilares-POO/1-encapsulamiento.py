#Se utiliza para que los atributos se puedan reutilizar dentro de la misma clase

class A():
    def __init__(self):     #Constructor
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):     #Constructor
        self.__contador = 0 #Doble __ es para encapsular el atributo

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

print("Objeto 1")
a = A()
print(a.cuenta())   #Muestra de primeras 0 del constructor
a.incrementar()     #Incrementa en uno el contador
print(a.cuenta())   #Muestra el uno gracias a la incrementación anterior
print(a.contador)   #Muestra la impresión del contador (son malas prácticas de programación)

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())