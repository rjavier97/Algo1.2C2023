from queue import LifoQueue as Pila
import random

def contar_lineas(archivo: str)->int:
    a: archivo = open(archivo)
    lineas: int = a.readlines()
    print(a)
    print(lineas)
    print("Mi archivo tiene", len(lineas),"lineas")

    return len(lineas)

# Ejercicio8-------------------------------------------------------------------------------------------------------------------
## Metodos de pila: 
# apilar: ingresa un elemento a la cola: pila.put(elemento) 
# desapilar: devuelve y quita el ultimo elemento insertado: pila.get()
# tope: devuelve (sin sacar) el ultimo elemento insertado
# vacia: retorna verdadero si esta vacia: pila.empty()
def generar_nros_al_azar(n: int, desde: int, hasta: int)->Pila:          ## Para ver una pila print(pila.queue)
    contador: int = 1
    pila:Pila = Pila()     ## con Pila() creo una pila vacia
    while (contador<=n) :
        pila.put(random.randint(desde,hasta))
        contador +=1 
    return pila 

# Ejercicio10-------------------------------------------------------------------------------------------------------------------
def buscar_el_maximo(p :Pila)->int:
    res: int 
    while (not p.empty() ) 
    

