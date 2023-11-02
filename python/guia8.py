from queue import LifoQueue as Pila
import random 
# Ejercicio1-------------------------------------------------------------------------------------------------------------------
# 1.1)-----------------------------------------------------------
def contarLineas(nombreArchivo : str)->int:
    archivo = open(nombreArchivo, 'r', encoding="utf-8")
    lineas = archivo.readlines()
    res : int = len(lineas)
    archivo.close()
    return res 

# print(contarLineas("archivo.txt"))

# 1.2)-----------------------------------------------------------
def existePalabra(palabra: str, nombreArchivo: str)->bool:
    archivo = open(nombreArchivo, 'r', encoding='utf-8')
    lineas = archivo.readlines()
    res: bool = False
    for linea in lineas :
        elemento = (((linea.replace('\n','')).replace(',','')).lower()).split(' ') #Saco los caracteres '\n' y ',' y transformo la linea en minuscula
        print(elemento)
        if palabra in elemento :
            res = True 
    archivo.close()
    return res 

# 1.3)-----------------------------------------------------------
def cantidadApariciones(nombreArchivo: str, palabra: str)->int:
    archivo = open(nombreArchivo, 'r', encoding='utf-8')
    contenido = archivo.read()
    print(contenido)
    contenido = (contenido.replace("\n",' ')).replace(',','')
    print(contenido)
    contenido = (contenido.lower()).split(' ')
    print(contenido)
    res = contenido.count(palabra)
    return res 

# Ejercicio2-------------------------------------------------------------------------------------------------------------------
def clonarSinComentarios(nombreArchivo: str):
    archivo = open(nombreArchivo, 'r', encoding='utf-8')
    nuevoArchivoSinComentarios = open('archivoSinComentarios.txt', 'w', encoding='utf-8')
    lineas = archivo.readlines()
    print(lineas)
    for linea in lineas :
        lineaSinEspacios = linea.lstrip() 
        if lineaSinEspacios[0] != '#' :
            nuevoArchivoSinComentarios.write(linea)
    archivo.close()
    nuevoArchivoSinComentarios.close() 
    
# clonarSinComentarios("comentarios.txt")

# Ejercicio3-------------------------------------------------------------------------------------------------------------------
def clonarTextoEnReversa(nombreArchivo: str):
    archivo = open(nombreArchivo, 'r', encoding='utf-8')
    nuevoArchivo = open("reverso.txt", 'w', encoding='utf-8')
    lineas = archivo.readlines()
    print(lineas)
    for i in range(len(lineas)-1,-1,-1) :
        if i == len(lineas)-1 :
            nuevoArchivo.write(lineas[len(lineas)-1]+'\n')
        elif i == 0 :
            nuevoArchivo.write(lineas[0].replace('\n',''))
        else : 
            nuevoArchivo.write(lineas[i])
    archivo.close()
    nuevoArchivo.close()

# clonarTextoEnReversa("ejercicio3.txt")

# archivo = open("reverso.txt", 'r', encoding='utf-8')  ## La funcion seek() sirve para cambiar la posicion del cursor
# lineas = archivo.readlines()                            ## para leer o escribir un archivo en una determinada posicion
# print(lineas)  ## Aca estoy posicionado al final del archivo,
# archivo.seek(0) ## Si esta linea no existe. En la linea 75 voy a printear contenido vacio
# contenido = archivo.read() ## ya que aca estaria leyendo algo que ya no tiene mas caracteres
# print(contenido)

# Ejercicio4-------------------------------------------------------------------------------------------------------------------
def agregarAlFinal(nombreArchivo: str, frase:str):
    archivo = open(nombreArchivo, 'r+', encoding='utf-8')
    lineas = archivo.readlines()
    print(lineas)
    archivo.write(' '+frase)
    archivo.close()

# agregarAlFinal("ejercicio4.txt", "y bastaBaby")
# Primera linea
# Segunda linea
# Tercera linea

# Ejercicio5-------------------------------------------------------------------------------------------------------------------
def agregarAlPrincipio(nombreArchivo: str, frase: str):
    archivo = open(nombreArchivo, 'r+', encoding='utf-8')
    lineas = archivo.readlines()
    lineas[0] = frase+' '+lineas[0]  ## Aca la lista de lineas ya se modifico, (modifique solo la primer linea)
    archivo.close()
    archivo = open(nombreArchivo, 'w', encoding='utf-8') #Vuelvo a abrir el archivo para sobreescribir el contenido que hay
    archivo.writelines(lineas)  ## desde la posicion 0, sabiendo que ahora el archivo va a estar vacio 
    archivo.close()

# agregarAlPrincipio("ejercicio5.txt", "Soy el mejor")

# Ejercicio7-------------------------------------------------------------------------------------------------------------------
def promedioEstudiante(nombreArchivo: str, lu: str)->float:
    archivo = open("ejercicio7.csv", 'r', encoding='utf-8')
    contenido = archivo.read()
    print(contenido)
    lineas = contenido.split('\n')
    print(lineas)
    cantidadNotas = 0
    suma: int = 0
    promedioFinal : float = 0
    for i in range(len(lineas)) :
        if lu in lineas[i] :
            elemento = lineas[i].split(',')
            cantidadNotas = cantidadNotas + 1
            suma = suma + int(elemento[3].strip(' '))
    promedioFinal = suma / cantidadNotas
    archivo.close()
    print(promedioFinal)
    return promedioFinal

# promedioEstudiante("ejercicio7.csv", "123/20")

# Ejercicio8-------------------------------------------------------------------------------------------------------------------
## Metodos de pila: 
# apilar: ingresa un elemento a la cola: pila.put(elemento) [1]->[1,2]->[1,2,3]
# desapilar: devuelve y quita el ultimo elemento insertado: pila.get() [1,2,3]->[1,2]->[1]
# tope: devuelve (sin sacar) el ultimo elemento insertado
# vacia: retorna verdadero si esta vacia: pila.empty()

def generarNrosAlAzar(n:int, desde:int, hasta:int)->Pila:
    pila = Pila()
    for i in range(n) :
        pila.put(random.randint(desde, hasta))
    print(pila.queue)
    return pila 
# generarNrosAlAzar(4, 1, 8)

# Ejercicio9-------------------------------------------------------------------------------------------------------------------
def cantidadElementos(p: Pila)->int:
    lista: [int] = []
    cantidad: int = 0             # pila = [1,2,3]
    while not p.empty() :
       lista.append(p.get())      # lista = [3,2,1]
       cantidad = cantidad + 1
    for i in range(len(lista)-1,-1,-1):    # pila=[1] -> pila=[1,2] -> pila=[1,2,3]
        p.put(lista[i])
    print(p.queue)
    return cantidad 

# print(cantidadElementos(generarNrosAlAzar(4,1,6)))

# Ejercicio10-------------------------------------------------------------------------------------------------------------------
def buscarElMaximo(p: Pila)->int:
    print(p.queue)
    maximo: int = p.get()
    lista: [int] = [maximo] 
    numero: int = 0
    while not p.empty() :
        numero = p.get()
        lista.append(numero)
        if numero > maximo :
            maximo = numero 
    for i in range(len(lista)-1,-1,-1):
        p.put(lista[i])
    print(p.queue)
    return maximo
# print(buscarElMaximo(generarNrosAlAzar(0,1,7)))            

# Ejercicio11-------------------------------------------------------------------------------------------------------------------
# def esta_bien_balanceada(s:str)->bool:

# Ejercicio12-------------------------------------------------------------------------------------------------------------------
def evaluar_expresion(expresion: str)->int:
    pila = Pila()
    operadores: [str] = ['+', '-', '*', '/']
    listaTokens = expresion.split(' ')
    res: int = 0 
    for token in listaTokens :
        if  not (token in operadores) :
            pila.put(int(token))
        elif token == '+' :
            res = pila.get() + pila.get()
            pila.put(res)
        elif token == '-' : 
            ultimoNumero = pila.get()
            res = pila.get() - ultimoNumero
            pila.put(res)
        elif token == '*' :
            res = pila.get() * pila.get()
            pila.put(res)
        elif token == '/' :
            ultimoNumero = pila.get()
            res = pila.get() / ultimoNumero
            pila.put(res)
    print(pila.queue)
    return pila.get()
# print(evaluar_expresion("3 4 - 5 * 4 /"))
