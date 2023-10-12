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
def el_doble_si_es_par(numero)->int:
    res: int 
    if numero % 2 == 0 :
        res = numero*2
    else :
        res = numero
    return res 

# 5.2)-----------------------------------------------------------
def par_sino_el_que_sigue(num: int)->int:
    res: int
    if num % 2 == 0 :
        res = num
    else : 
        res = num + 1 
    return res 

def par_sino_el_que_sigue1(num: int)->int:
    res: int
    if num % 2 == 0 :
        res = num
    if num % 2 != 0 :
        res = num + 1 
    return res 

def par_sino_el_que_sigue2(num: int)->int:
    res: int = num + 1     # Asumo que el numero es impar, 
    if num % 2 == 0 :      # Si el numero ingresado es par, entonces que me devuelva ese numero par
        res = num 
    return res 

# 5.3)-----------------------------------------------------------
def funcionMultiplo(num:int)->int:
    res: int 
    if num % 3 == 0 :
        res = num*2
    elif num % 9 == 0 :
        res = num*3
    else :
        res = num 
    return res 

def funcionMultiplo1(num:int)->int:
    res: int = num
    if num % 3 == 0 :
        res = num*2
    if num % 9 == 0 :
        res = num*3
    return res 
    
#Pregunta: ¿Ambas implementaciones funcionan? 
#Respuesta: No, cuando el numero es multiplo de 9, funcionMultiplo1 devuelve un valor distinto a funcionMultiplo

# 5.4)-----------------------------------------------------------
def lindoNombre(nombre:str):
    if len(nombre) >= 5 :
        print('Tu nombre tiene muchas letras')
    else :
        print("Tu nombre tiene menos de 5 caracteres")

# 5.5)-----------------------------------------------------------
def elRango(numero:int):
    if numero < 5 :
        print("Menor a 5")
    elif numero>=10 and numero<=20 :
        print("Entre 10 y 20")
    elif numero>20 :
        print("Mayor a 20")

# 5.6)-----------------------------------------------------------
def vacacionarOTrabajar(sexo:str , edad:int):
    if ("f"==sexo=="F" and edad>=60 ) or ("M"==sexo=="m" and edad>=65) or edad<18 :
        print("Andá de vacaciones")
    else : 
        print("Te toca trabajar")










       



 
    





    






    