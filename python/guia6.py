import importlib
import math
# Ejercicio1-------------------------------------------------------------------------------------------------------------------
# 1.1)-----------------------------------------------------------
def imprimir_hola_mundo()->None:
    print("¡Hola mundo!")
    
# 1.2)-----------------------------------------------------------
def imprimir_un_verso():
    print("Oid mortales")

# 1.3)-----------------------------------------------------------
def raizDe2()->float:
    res: float = round(math.sqrt(2),4)
    return res 
    
# 1.4)-----------------------------------------------------------
def factorial_de_dos()->int:
    return (2*1)
    
# 1.5)-----------------------------------------------------------
def perimetro()->float:
    pi = math.pi
    return (2 * pi )    
 
# Ejercicio2-------------------------------------------------------------------------------------------------------------------
# 2.1)-----------------------------------------------------------
def imprimir_saludo(nombre: str):    
    print("Hola " + str(nombre)) 
    
# 2.2)-----------------------------------------------------------
def raiz_cuadrada_de(numero: int)->float:
    res: float = math.sqrt(numero)
    return(res) 
    
# 2.3)-----------------------------------------------------------
def fahrenheit_a_celsius(t: int)->float:
    res: float = ((t-32)*5)/9
    return res 

# 2.4)-----------------------------------------------------------
def imprimir_dos_veces(s: str):
    print(s*2)
    
# 2.5)-----------------------------------------------------------    
def es_multiplo_de(n: int, m:int)->bool:
    res: bool = (n%m ==0)
    return res 

# 2.6)-----------------------------------------------------------
def es_par (n: int)->bool:
    res: bool = es_multiplo_de(n, 2)
    return res 

# 2.7)-----------------------------------------------------------
def cantidad_de_pizzas(comensales, min_cant_de_porciones)->int:
    res: int = math.ceil((comensales * min_cant_de_porciones)/8) 
    return res 

# Ejercicio3-------------------------------------------------------------------------------------------------------------------
# 3.1)-----------------------------------------------------------
def alguno_es_0(n1:float, n2:float)->bool:
    res: bool = (n1==0)or(n2==0) 
    return res 

# 3.2)-----------------------------------------------------------
def ambos_es_0(n1:float, n2:float)->bool:
    res: bool = (n1==0)and(n2==0) 
    return res 

# 3.3)-----------------------------------------------------------
def es_nombre_largo(nombre: str)->bool:
    largoDeNombre: int = len(nombre)
    res: bool = (largoDeNombre >= 3)and(largoDeNombre <=8 )    
    return res
    
# 3.4)-----------------------------------------------------------
def es_bisiesto(año: int)->bool:
    res: bool = (año % 400 ==0) or ( (año%4)==0 and (año%100) != 0)
    return res     

# Pregunta de clase: ejecucion simbolica (revisar en teorica)
# Ejercicio4-------------------------------------------------------------------------------------------------------------------
def peso_pino(altura: float)->float:
    res: float
    if altura < 3 :
        res = altura * 300 
    else : 
        res = altura*200 + 300
    
    return res 

def es_peso_util(peso: float)->bool:
    res: bool = (peso >= 400) and (peso <= 1000) 
    return res 

def sirve_pino(altura: float)->bool:  #Un pino que pesa entre 400kg y 1000kg, es un pino que mide entre (4/3)m y 3,5m
    res: bool = (altura >= 4/3) and (altura <= 3.5)
    return res 

def sirve_pinoComp(altura: float)->bool:
    return es_peso_util(peso_pino(altura))

# Ejercicio5-------------------------------------------------------------------------------------------------------------------
# 5.1)-----------------------------------------------------------
def devolver_el_doble_si_es_par(numero)->int:
    res: int 
    if numero % 2 == 0 :
        res = numero*2
    else :
        res = numero
    return res 

# 5.2)-----------------------------------------------------------







 
    





    






    