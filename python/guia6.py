# Ejercicio1-------------------------------------------------------------------------------------------------------------------
#String = str
#division entera:(a // b), resto de division:(a % b) 
#En la terminal: 1) import importlib, 2) importlib.reload(nombre de la funcion)
# si no hay un return, la funcion devuelve -> None: (ej1 a), tambien puede no escribirse nada como valor de retorno (ej1 b)
import importlib
import math
# a)-----------------------------------------------------------
def imprimir_hola_mundo()->None:
    print("¡Hola mundo!")
    
# b)-----------------------------------------------------------
def imprimir_un_verso():
    print("Oid mortales")

# c)-----------------------------------------------------------
def raizDe2()->float:
    res: float = round(math.sqrt(2),4)
    return res 
    
# d)-----------------------------------------------------------
def factorial_de_dos()->int:
    return (2*1)
    
# e)-----------------------------------------------------------
def perimetro()->float:
    pi = math.pi
    return (2 * pi )    
 
# Ejercicio2-------------------------------------------------------------------------------------------------------------------
# a)-----------------------------------------------------------
def imprimir_saludo(nombre: str):    
    print("Hola " + str(nombre)) 
    
# b)-----------------------------------------------------------
def raiz_cuadrada_de(numero: int)->float:
    res: float = math.sqrt(numero)
    return(res) 
    
# c)-----------------------------------------------------------
def fahrenheit_a_celsius(t: int)->float:
    res: float = ((t-32)*5)/9
    return res 

# d)-----------------------------------------------------------
def imprimir_dos_veces(s: str):
    print(s*2)
    
# e)-----------------------------------------------------------    
def es_multiplo_de(n: int, m:int)->bool:
    res: bool = (n%m ==0)
    return res 

# f)-----------------------------------------------------------
def es_par (n: int)->bool:
    res: bool = es_multiplo_de(n, 2)
    return res 

# f)-----------------------------------------------------------
def cantidad_de_pizzas(comensales, min_cant_de_porciones)->int:
    res: int = math.ceil((comensales * min_cant_de_porciones)/8) 
    return res 

# Ejercicio3-------------------------------------------------------------------------------------------------------------------
# a)-----------------------------------------------------------
def alguno_es_0(n1:float, n2:float)->bool:
    res: bool = (n1==0)or(n2==0) 
    return res 

# b)-----------------------------------------------------------
def ambos_es_0(n1:float, n2:float)->bool:
    res: bool = (n1==0)and(n2==0) 
    return res 

# c)-----------------------------------------------------------
def es_nombre_largo(nombre: str)->bool:
    largoDeNombre: int = len(nombre)
    res: bool = (largoDeNombre >= 3)and(largoDeNombre <=8 )    
    return res
    
# d)-----------------------------------------------------------
def es_bisiesto(año: int)->bool:
    res: bool = (año % 400 ==0) or ( (año%4)==0 and (año%100) != 0)
    return res     

# Pregunta de clase: ejecucion simbolica (revisar en teorica)
# Ejercicio4-------------------------------------------------------------------------------------------------------------------


    






    