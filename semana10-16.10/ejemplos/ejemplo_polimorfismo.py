class Animal:

    def __init__(self, nombre: str , edad: int):
        self.nombre = nombre
        self.edad = edad    
    
    def emitir_sonido(self):
        pass

class Perro(Animal):
    def emitir_sonido(self):
        return "Guau!"

class Gato(Animal):
    def emitir_sonido(self):
        return "Miau!"

# Funcion que utiliza polimorfismo
def hacer_emitir_sonido(animal):
    return animal.emitir_sonido()

# Crear instancias de diferentes animales
miPerro = Perro("Dylan", 10)
miGato = Gato("Azrael", 15) 

# Llamar a la funcion polimorfica con diferentes instancias
print(hacer_emitir_sonido(miPerro))  # Imprime "Guau!"
print(hacer_emitir_sonido(miGato))   # Imprime "Miau!"
