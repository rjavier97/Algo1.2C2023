import random
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
## Usar metodo replace para Strings,recordar que un string no es una lista(eso pasaba en haskell)
def esPalindromo(texto: str)->bool: 
    listaTexto: list[str] = texto.split()    ## Con el metodo split convierto un texto en una lista de palabras
    textoAplanado: str = ''.join(listaTexto) 
    textoInverso: str = ''.join(list(reversed(texto)))  ##El método str.join(lista) es usado para unir todos los elementos
    listaTextoInverso: list[str] = textoInverso.split()  #de una lista con un espefico string str in Python.
    textoInversoAplanado: str = ''.join(listaTextoInverso)
    print(texto)
    res: bool =  textoAplanado.lower() == textoInversoAplanado.lower()  ## con Lower transformo todo el texto en minuscula
    return res 

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

# Ejercicio2-------------------------------------------------------------------------------------------------------------------
# 2.1)-----------------------------------------------------------
def listaPosicionesParesInout(lista: [int])->[int]:##La especificacion dice que lista es INOUT, por lo tanto debo modificarla
    for i in range (0,len(lista),2) :    ## es decir, lista es un parametro de entrada y salida
        lista[i] = 0                  ## ingreso una lista y devuelvo esa misma lista pero modificada 
    return lista

# 2.2)-----------------------------------------------------------
def listaPosicionesParesIn(lista: [int])->[int]:  ##La especificacion dice que lista es IN, por lo tanto no debo modificarla
    res: list[int] = lista.copy()     ## con el metodo copy() no modifico el parametro lista
    for i in range (0,len(res),2) :   
        res[i] = 0 
    print(lista) ## no hace falta esta linea. Es solo para comprobar que lista != res , y que lista no se modifico 
    return res   ## probar con este ej: listaPosicionesParesIn([0,1,2,3,4])

# 2.3)-----------------------------------------------------------
def sinVocalesNiEspacios(cadenaDeChars: [chr])->[chr]:  ## cadenaDeChars es un parametro IN, por lo tanto no lo modifico 
    res: list[chr] = cadenaDeChars.copy()
    vocales: list[chr] = ['a','e','i','o','u']
    for i in range(0, len(cadenaDeChars), 1) : 
        letra: chr = cadenaDeChars[i]
        if letra in vocales :
            res.remove(letra)
    print(cadenaDeChars)  # no hace falta esta linea.Es solo para comprobar que cadenaDeChars != res , y que cadenaDeChars no se modifico 
    return res 
# sinVocalesNiEspacios(['b', 'c', 'd', 'a', 'f', 'e', 'o'])

# 2.4)-----------------------------------------------------------
def reemplazaVocales(s: [chr])->[chr] :    ## s es un parametro IN
    res: list[chr] = s.copy()
    vocales: list[chr] = ['a','e','i','o','u']
    for i in range(len(s)) :
        letra:chr = s[i]
        if letra in vocales :
            res[i] = '_' 
    print(s)
    return res 
# reemplazaVocales(['b', 'c', 'd', 'a', 'f', 'e', 'o'])

# 2.5)-----------------------------------------------------------
def daVueltaStr(s: [chr])->[chr] :  ## s es un parametro IN
    res: list[chr] = s.copy()
    res = list(reversed(res))
    # print(s)
    return res 

def daVueltaStr1(s: [chr])->[chr] :   ## s es un parametro IN
    res: list[chr] = s.copy()
    res.clear()
    for i in range(len(s)-1,-1,-1):
        letra:chr = s[i]
        res.append(letra)
    print(s)
    return res
# daVueltaStr1(['a', 'b'])
        
# 2.6)-----------------------------------------------------------
def eliminarRepetidos(s: [chr])->[str]:  ## s es un parametro IN
    res: list[chr] = s.copy()
    res = list(reversed(res))
    for letra in res :
        cantidadApariciones: int = res.count(letra)
        if cantidadApariciones > 1 :
            for i in range (1,cantidadApariciones) :
                res.remove(letra)
    print(s)
    res = list(reversed(res))
    return res 
# eliminarRepetidos(['a', 'i', 'b', 'c', 'd', 'e', 'i', 'c'])

# Ejercicio3-------------------------------------------------------------------------------------------------------------------
def aprobado(listaNotas: [int])->int :
    sumaTotalNotas: int = 0 
    todasAprobadas: bool = True
    res: int 
    for nota in listaNotas :          ## con este for ya tengo la sumaTotalNotas
        sumaTotalNotas = sumaTotalNotas + nota
        if nota >= 4 :
            todasAprobadas = todasAprobadas and True
        else : 
            todasAprobadas = False
    promedio: int = sumaTotalNotas / len(listaNotas)
    if todasAprobadas and (promedio>=7) :
        res = 1
    elif todasAprobadas and (promedio>=4):
        res = 2
    else :
        res = 3
    return res 
    
# Ejercicio4-------------------------------------------------------------------------------------------------------------------
# 4.1)-----------------------------------------------------------
def listaDeEstudiantes ()->[str]:
    res: [str] = []
    nombreEstudiante = input("Ingrese el nombre del estudiante, cuando termine ingrese 'listo': ")
    while (nombreEstudiante != "listo"):
        res.append(nombreEstudiante)
        nombreEstudiante = input("Ingrese el nombre del estudiante: ")
    return res 

# 4.2)-----------------------------------------------------------
def historialMonederoElectronico()->[(str,int)]:
    res: [(str,int)] = []
    cargarDescontar: str = (input("Ingrese 'C' para cargar créditos, 'D' para descontar créditos o 'X' para terminar: ")).upper()
    if cargarDescontar == 'X' :
        res = res
    else :     ## Input solo puede recibir un argumento, por eso se usa la letra f para poder incluir variables
        montoDeOperacion: int = int(input(f"Ingrese el monto de la operación {cargarDescontar}: "))
    while (cargarDescontar != 'X') :
        res.append((cargarDescontar, montoDeOperacion)) 
        cargarDescontar: str = (input("Ingrese 'C' para cargar créditos, 'D' para descontar créditos o 'X' para terminar: ")).upper()
        if cargarDescontar != 'X' :
            montoDeOperacion: int = int(input(f"Ingrese el monto de la operación {cargarDescontar}: "))
    print('¡Gracias!')
    return res 

def historialMonederoElectronico1()->[(str,int)]:
    res: [(str,int)] = []
    next: bool = True
    while (next) :
        cargarDescontar: str = (input("Ingrese 'C' para cargar créditos, 'D' para descontar créditos o 'X' para terminar: ")).upper()
        if cargarDescontar != 'X' :
            montoDeOperacion: int = int(input(f"Ingrese el monto de la operación {cargarDescontar}: "))
            res.append((cargarDescontar, montoDeOperacion))
        else :
            next = False 
    return res 

# 4.3)-----------------------------------------------------------
def juego7ymedio()->[int]:
    cartas: [int] = [1,2,3,4,5,6,7,10,11,12]
    sumaTotal: int = 0
    cartaRandom: int = random.choice(cartas)
    historialDeCartas: [int] = [cartaRandom]
    if cartaRandom in [10,11,12] : 
        sumaTotal = 0.5
    else : 
        sumaTotal = cartaRandom
    next: bool = True
    print("Bienvenido, su primera carta es: "+str(cartaRandom)) 
    while (next) :
        juego: str = input("Si desea sacar otra carta presione 'c', si desea plantarse presione 'x' : ")
        if juego != 'x' : 
            cartaRandom = random.choice(cartas)
            if cartaRandom in [10,11,12] :
                sumaTotal = sumaTotal + 0.5
            else: 
                sumaTotal = sumaTotal + cartaRandom
            print("Usted ha sacado un",cartaRandom,"y suma hasta ahora:",sumaTotal)
            if sumaTotal > 7.5 :
                print("Usted ha perdido")
                next = False 
            historialDeCartas.append(cartaRandom)
        else :
            next = False
    return historialDeCartas 

# Ejercicio5-------------------------------------------------------------------------------------------------------------------
# 5.1)-----------------------------------------------------------
def perteneceACadaUno(s: [[int]], e: int)->[bool]:
    resFinal:[bool] = [] 
    for elemento in s :
        if pertenece2(elemento, e) : 
           resFinal.append(True) 
        else:
            resFinal.append(False)    
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

# def perteneceACadaUnoOtroEj(s: [[int]], e: int)->bool:
#     resFinal: bool = True 
#     for elemento in s :
#         resElemento: bool = False
#         if pertenece2(elemento, e) : 
#            resElemento = True   
#         resFinal = resFinal and resElemento 
#     return resFinal   


