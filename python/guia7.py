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
    for i in range(0, longitud, 1):
        if (s[i] == e) :
            pertenece = True
    return pertenece    

def perteneceGenerico(s:[any], e:any)->bool:
    pertenece: bool = False
    longitud: int = len(s)
    for i in range(0, longitud, 1):
        if (s[i] == e) :
            pertenece = True
    return pertenece    

# 1.3)-----------------------------------------------------------
def suma_total(s: [int])->int:
    total: int = 0
    indice_actual: int = 0
    longitud: int = len(s)
    while(indice_actual < longitud) :
        valor_actual: int = s[indice_actual]
        total = total + valor_actual
        indice_actual += 1
    return total 

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

print(perteneceACadaUno1([[1,2,3],[4,2,6],[1,8,2]],7))


