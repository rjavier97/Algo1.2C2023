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

# Ejercicio6-------------------------------------------------------------------------------------------------------------------
# 6.1)-----------------------------------------------------------
def imprimirDel1Al10()->None:
    n: int = 1
    while (n<=10) :
        print(str(n))
        n += 1

# 6.2)-----------------------------------------------------------
def imprimirParesDel10Al40()->None:
    n: int=10
    while (n<=40) :
        print(n)
        n += 2

# 6.3)-----------------------------------------------------------
def imprimirEco10Veces()->None:
    n:int = 1
    while (n<=10) : 
        print("eco")
        n+=1
# 6.4)-----------------------------------------------------------
def cuentaRegresiva(n: int)->None:
    while (n>=1) :
        print(n)
        n -= 1  # esto es igual a hacer n = n - 1
    print("Despegue")
# 6.5)-----------------------------------------------------------
def viajeEnElTiempo(añoDePartida: int, añoDeLlegada: int)->None:
    año: int = añoDePartida
    while (año>añoDeLlegada) :
        año -= 1
        print("Viajó un año al pasado, estamos en el año: "+str(año))
        
# 6.6)-----------------------------------------------------------
def viajeEnElTiempoAC(añoDePartida: int)->None:
    año: int = añoDePartida - 20
    while (año>=-384):
        if (año>=0) :
            print("Viajó 20 años al pasado, estamos en el año: "+str(año))
        else: 
            print("Viajó 20 años al pasado, estamos en el año: "+str(-año)+" a.C.")
        año -= 20 

# Ejercicio7-------------------------------------------------------------------------------------------------------------------
# 7.1)-----------------------------------------------------------
def imprimirDel1Al10For()->None:
    for i in range(1,11) :
        print(str(i))

# 7.2)-----------------------------------------------------------
def imprimirParesDel10Al40For()->None:
    for i in range(10,41,2) :
        print(i) 
# 7.3)-----------------------------------------------------------
def imprimirEco10VecesFor()->None:
    for i in range(0,10):
        print("eco")
# 7.4)-----------------------------------------------------------
def cuentaRegresivaFor(n: int)->None:
    for i in range(n,0,-1) : 
        print(i)
    print("Despegue")
# 7.5)-----------------------------------------------------------
def viajeEnElTiempoFor(añoDePartida: int, añoDeLlegada: int)->None:
    for i in range(añoDePartida-1,añoDeLlegada-1,-1):
        print("Viajó un año al pasado, estamos en el año: "+str(i))
# 7.6)-----------------------------------------------------------
def viajeEnElTiempoACFor(añoDePartida: int)->None:
    for i in range(añoDePartida-20,-394-1,-20):  # hasta lo más cercano al 384 a.C
        if i>=0 :
            print("Viajó 20 años al pasado, estamos en el año: "+str(i))
        else: 
            print("Viajó 20 años al pasado, estamos en el año: "+str(-i)+" a.C.")

# Ejercicio8-------------------------------------------------------------------------------------------------------------------
# Realizar la ejecución simbólica de los siguientes códigos:
# 1) x=5 ; y=7; x=x+y
# 2) x=5 ; y=7 ; z=x+y; y=z*2
# 3) x=5 ; y=7 ; x="hora"; y=x*2
# 4) x=False ; res=not(x)
# 5) x=True ; y=False ; res= x and y ; x= res and x

# 8.1)-----------------------------------------------------------
# x=5
""" Estado1; vale x==5 """
# y=7
""" Estado2; vale y==7 ∧ x==x@1 """ ## donde x==x@1=5
# x=x+y
""" Estado3; vale x==x@2+y@2 ∧ y==y@2 """ ## donde x==5+7=12 ∧ x@2==5  ∧ y=y@2==7

# 8.2)-----------------------------------------------------------
# x=5  
""" Estado1; vale x==5 """
# y=7 
""" Estado2; vale y==7 ∧ x==x@1 """ ## donde x==x@1=5
# z=x+y 
""" Estado3; vale z==x@2+y@2 ∧ x==x@2 ∧ y==y@2 """ ## donde z==5+7=12  ∧ x==x@2=5 ∧ y==y@2=7
# y=z*2
""" Estado4; vale y==z@3 *2 ∧ z==z@3 ∧ x==x@3 """  ## donde y==12*2=24  ∧ z==z@3=12 ∧ x==x@3=5

# 8.3)-----------------------------------------------------------
# x=5  
""" Estado1; vale x==5 """
# y=7
""" Estado2; vale y==7 ∧ x==x@1"""  ## donde x==x@1=5 
# x="hora" 
""" Estado3; vale x=="hora" ∧ y==y@2 """ ## donde y==y@2=7 
# y=x*2
""" Estado4; vale y==(x@3)*2  ∧ x==x@3 """ ## donde y=="horahora" ∧ x==x@3="hora"

# 8.4)-----------------------------------------------------------
# x=False 
""" Estado1; vale x==False """
# res=not(x)
""" Estado2; vale res==not(x@1) ∧ x==x@1 """  ## donde res==True ∧ x==x@1=False 

# 8.5)-----------------------------------------------------------
# x=True 
""" Estado1; vale x==True """
# y=False 
""" Estado2; vale y==False ∧ x==x@1""" ## donde x==x@1= True
# res = x and y 
""" Estado3; vale res==(x@2 and y@2) ∧ x==x@2 ∧ y==y@2 """ ## donde res==(True and False)==False ∧ x==x@2=True ∧ y==y@2=False
# x = res and x
""" Estado4; vale x==(res@3 and x@3) ∧ res==res@3 """ ## donde x==(False and True)==False ∧ res==res@3=False ∧ x==x@3=True

# Ejercicio9-------------------------------------------------------------------------------------------------------------------
# 1. ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
# 2. ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# 3. En cada función, realizar la ejecución simbólica.
# 4. Dar la especificación en lenguaje natural para cada función, rt y ro.

# def rt(x: int, g: int) -> int:
#     g = g + 1
#     return x + g
    
# g: int = 0
# def ro(x: int) -> int:
#     global g
#     g = g + 1
#     return x + g






## Ejemplo de la teorica 7
# def duplicar(x: list, y: list):
#     print("ANTES:\n x:",x,"\n y:",y)
#     y = x
#     y *= 2 
#     print("DESPUES:\n x:",x,"\n y:",y)

# duplicar(['a','b','c'],['d','e'])










       



 
    





    






    