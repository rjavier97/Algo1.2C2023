# Ejercicio1-------------------------------------------------------------------------------------------------------------------
# 1.1)-----------------------------------------------------------
def pertenece(s: [int], e: int)->bool:       
    resultado: bool = False
    indice_actual: int = 0
    longitud: int = len(s)
    while (indice_actual < longitud):
        valor_actual: int = s[indice_actual]
        if (valor_actual == e) : 
            resultado = resultado or True 
        indice_actual += 1 
    return resultado 

def pertenece1(s: [int], e: int)->bool:
    resultado: bool = False
    indice_actual: int = 0
    longitud: int = len(s)
    while (indice_actual < longitud) and (not(resultado)) :
        valor_actual: int = s[indice_actual]
        if (valor_actual == e) : 
            resultado = True
        indice_actual += 1 
    return resultado 

def pertenece2(s:[int], e:int)->bool:
    pertenece: bool = False
    longitud: int = len(s)
    for i in range(0, longitud, 1):   ## Como star=0 , y step:1 son valor por default , se puede poner in range(longitud) nomas
        if (s[i] == e) :
            pertenece = True
    return pertenece    

def pertenece3(s: [int], e: int)->bool:
    pertenece: bool = False
    for elemento in s :
        if elemento == e : 
            pertenece = True 
    return pertenece 

def perteneceGenerico(s:[any], e:any)->bool:
    pertenece: bool = False
    longitud: int = len(s)
    for i in range(0, longitud, 1):
        if (s[i] == e) :
            pertenece = True
    return pertenece    

# 1.2)-----------------------------------------------------------
def divideATodos11(s: "list[int]", e: int)->bool:
    res: bool = True
    for i in range(0 ,len(s)) :  ## Como star=0 es un valor por default, no hace falta escribirlo, in range(len(s)) 
        if (s[i] % e == 0 ) :
            res = res and True 
        else : 
            res = False
    return res 

def divideATodos12(s: "list[int]", e: int)->bool:
    res: bool = True
    for i in range(len(s)) :
        if (s[i] % e != 0 ) :
            res = False
    return res 

def divideATodos21(s:[int], e: int)->bool:
    res: bool = True
    for num in s :
        if num % e == 0 : 
            res = res and True
        else : 
            res = False
    return res 

def divideATodos22(s: [int], e: int)->bool:
    res: bool = True
    for num in s : 
        if num % e != 0 :
            res = False 
    return res 

def divideATodos31(s: "list[int]", e: int)->bool:
    res: bool = True
    indice_actual: int = 0 
    while (indice_actual < len(s) and res == True) :
        if s[indice_actual] % e == 0 :
            res = True
        else : 
            res = False 
        indice_actual += 1 
    return res 

def divideATodos32(s: "list[int]", e:int)->bool:
    res: bool = True 
    indice_actual: int = 0
    while ( indice_actual < len(s) and res==True) : 
        if s[indice_actual] % e != 0 :
            res = False 
        indice_actual += 1 
    return res 

# 1.3)-----------------------------------------------------------
def suma_total1(s: [int])->int:
    total: int = 0
    indice_actual: int = 0
    longitud: int = len(s)
    while(indice_actual < longitud) :
        valor_actual: int = s[indice_actual]
        total = total + valor_actual
        indice_actual += 1
    return total 

def suma_total2(s: [int])->int:
    total:int = 0 
    indice_actual: int = 0
    while (indice_actual < len(s) ) :
        total = total + s[indice_actual]
        indice_actual += 1
    return total 

def suma_total3(s: [int])->int : 
    total: int = 0 
    for num in s :
        total = total + num 
    return total

def suma_total4(s: [int])->int :
    total: int = 0
    for i in range(len(s)) :
        total = total + s[i]
    return total 

# 1.4)-----------------------------------------------------------
def ordenados(s: [int])->bool:
    res: bool = True
    for i in range(len(s) -1) :
        if (s[i]>=s[i+1]):
            res = False 
    return res 

# 1.5)-----------------------------------------------------------
def palabraMayorA7(lista: [str])->bool:
    res: bool = False
    for palabra in lista : 
        if len(palabra) > 7 :
            res = True
    return res 

# 1.6)-----------------------------------------------------------
# def esPalindromo(texto: str)->bool:  ## Usar metodo replace para Strings,recordar que un string no es una lista(eso pasaba en haskell)

## a.strip()

# 1.7)-----------------------------------------------------------
# ord("A")=65 , ord("Z")=90 , ord("a")=97 , ord("z")=122
def contraseña_segura(contraseña: str)->str:
    longitud: int = len(contraseña)
    res : str 
    if (longitud>8 and contiene_mayuscula(contraseña) and contiene_minuscula(contraseña) and (contiene_numero(contraseña))) :
        res = "VERDE"
    elif (longitud<5):    # ---> Cuidado: Si hubiera escrito acá un if y en la linea61 un else.. (sigue abajo)
        res = "ROJA"       # ese else se mete dentro del if de linea59. Por lo tanto si el resultado es "VERDE"
    else :                   # me devolveria erroneamente un "AMARILLA" como resultado. 
        res = "AMARILLA"
    return res     

## Funciones auxiliares-----------------------
def contiene_minuscula(contraseña: str)->bool:
    res: bool = False 
    for letra in contraseña :
        if ( ord(letra)>=97 and ord(letra)<=122 ) :   # otra opcion mejor:   if (letra>="a" and letra<="z") :
            res = True
    return res 

def contiene_mayuscula(contraseña: str)->bool:
    res: bool = False 
    for letra in contraseña :
        if ( ord(letra)>=65 and ord(letra)<=90 ) :
            res = True
    return res 

def contiene_numero(contraseña: str)->bool:
    res: bool = False 
    for letra in contraseña :
        if ( ord(letra)>=48 and ord(letra)<=57 ) :
            res = True
    return res  

# 1.8)-----------------------------------------------------------
def saldoActual(movimientos: [(str,int)])->int:
    res: int = 0 
    for saldo in movimientos :
        if saldo[0]=='I' :
            res = res + saldo[1]
        else : res = res - saldo[1]
    return res  

# 1.9)-----------------------------------------------------------
def tiene3VocalesDistintas(palabra: str)->bool:
    res:bool = False
    cantVocalesDistintas: int = 0 
    cantVocalA: int = 0
    cantVocalE: int = 0 
    cantVocalI: int = 0
    cantVocalO: int = 0 
    cantVocalU: int = 0 
    indice_actual: int = 0 
    while (indice_actual < len(palabra) and cantVocalesDistintas<3) :
        if  palabra[indice_actual]=='a' and cantVocalA==0 :
            cantVocalA = 1
            cantVocalesDistintas = cantVocalesDistintas + cantVocalA
        elif palabra[indice_actual]=='e' and cantVocalE==0 :
            cantVocalE = 1
            cantVocalesDistintas = cantVocalesDistintas + cantVocalE
        elif palabra[indice_actual]=='i' and cantVocalI==0 :
            cantVocalI = 1
            cantVocalesDistintas = cantVocalesDistintas + cantVocalI
        elif palabra[indice_actual]=='o' and cantVocalO==0 :
            cantVocalO = 1
            cantVocalesDistintas = cantVocalesDistintas + cantVocalO
        elif palabra[indice_actual]=='u' and cantVocalU==0 :
            cantVocalU = 1
            cantVocalesDistintas = cantVocalesDistintas + cantVocalU
        indice_actual += 1 
    if cantVocalesDistintas == 3 :
        res = True
    return res 
     
# Ejercicio5-------------------------------------------------------------------------------------------------------------------
# 5.1)-----------------------------------------------------------
def perteneceACadaUno(s: [[int]], e: int)->bool:
    resFinal: bool = True 
    for elemento in s :
        resElemento: bool = False
        if pertenece2(elemento, e) : 
           resElemento = True   
        resFinal = resFinal and resElemento 
    return resFinal              

def perteneceACadaUno1(s: [[int]], e: int)->[bool]:
    resFinal:[bool] = [] 
    for elemento in s :
        resElemento: bool = False
        if pertenece2(elemento, e) : 
           resElemento = True   
        resFinal.append(resElemento)
    return resFinal              

# print(perteneceACadaUno1([[1,2,3],[4,2,6],[1,8,2]],7))


