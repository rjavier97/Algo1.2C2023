from queue import LifoQueue as Pila, Queue as Cola
# from queue import Queue as Cola
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
def cantidad_elementosPila(p: Pila)->int:
    print(p.queue)
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

# Ejercicio13-------------------------------------------------------------------------------------------------------------------
def colaDeEnteros(pila: Pila)->Cola:
    cola = Cola()
    while not pila.empty() :
        cola.put(pila.get())
    print(cola.queue)
    return cola 
# colaDeEnteros(generarNrosAlAzar(4,1,6))

# Ejercicio14-------------------------------------------------------------------------------------------------------------------
def cantidad_elementosCola(cola: Cola)->int:
    print(cola.queue)
    lista:[int] = []
    cantidad: int = 0
    while not cola.empty() :
        lista.append(cola.get())
        cantidad +=1 
    for num in lista :
        cola.put(num)
    print(cola.queue)
    return cantidad

# Ejercicio15-------------------------------------------------------------------------------------------------------------------
def buscar_el_maximo(c: Cola)->int:
    maximo: int = c.get()
    caux: Cola = Cola()
    caux.put(maximo)
    while not c.empty():
        elemento = c.get()
        caux.put(elemento)
        if elemento > maximo :
            maximo = elemento 
    while not caux.empty():
        c.put(caux.get())
    return maximo     

# Ejercicio16-------------------------------------------------------------------------------------------------------------------
# 16.1)-----------------------------------------------------------
def armar_secuencia_de_bingo()->Cola:
    cola: Cola = Cola()
    listaNrosDe0a99: [int] = list(range(0,100))  ## lista de nros del 0 al 99 
    while len(listaNrosDe0a99) != 0 :          ## mientras la lista no sea vacia
        numero: int = random.choice(listaNrosDe0a99)   ## elijo un nro del 0 al 99 al azar de la lista 
        cola.put(numero)     ## ese nro al azar lo agrego a la cola
        listaNrosDe0a99.remove(numero)  ## ese nro lo elimino de la lista de nros del 0 al 99 
    print(cola.queue)
    return cola 

# 16.2)-----------------------------------------------------------
def jugar_carton_de_bingo(carton: [int], bolillero: Cola)-> int:
    cartonaux: [int] = carton.copy()
    bolilleroaux: Cola = Cola()
    print('cartonIN :',carton)
    print('bolilleroIN :',bolillero.queue)
    cantidadJugadas : int = 0 
    while cartonaux != []:
        numero: int = bolillero.get()
        bolilleroaux.put(numero)
        if numero in cartonaux :
            cartonaux.remove(numero)
        cantidadJugadas += 1
    print('cartonOUT: ',carton)
    while not bolillero.empty() :
        bolilleroaux.put(bolillero.get())
    bolillero = bolilleroaux
    print('bolilleroOUT :',bolillero.queue)    
    return cantidadJugadas 
    
# Ejercicio17-------------------------------------------------------------------------------------------------------------------
def n_pacientes_urgentes(c: Cola((int,str,str)) )-> int:
    print('cIN :',c.queue)
    print('cIN :', c)
    pacientesUrgentes: int = 0
    caux: Cola((int,str,str)) = Cola()
    while not c.empty() :
        elemento: (int,str,str) = c.get()
        caux.put(elemento)
        if elemento[0] <= 3 :
            pacientesUrgentes += 1
    while not caux.empty() :        ## aca empiezo a restaurar el parametro 'c' de entrada, para que a la salida no se modifique 
        c.put(caux.get())
    print('cOUT :',c.queue)
    print('cOUT :',c)
    return pacientesUrgentes 

# Ejercicio18-------------------------------------------------------------------------------------------------------------------
def a_clientes(c: Cola((str,int,bool,bool)))->Cola((str,int,bool,bool)): ## a = <queue.Queue object at 0x0000024E818798E0>
    ## ('Javier Suarez', 40851203, True, False), ('Mario Gomez', 40820432, True, True), ('Jose Lopez', 40678123, False, False), 
    # ('Mirta Legrand', 10345123, False, True), ('German Cano', 50678123, True, False), ('Sergio Massa', 34512234, True, True)
    print('cIn :',c.queue)
    caux: Cola((str,int,bool,bool)) = Cola()
    colaPrioridad1: Cola((str,int,bool,bool)) = Cola()
    colaPrioridad2: Cola((str,int,bool,bool)) = Cola()
    colaResto: Cola((str,int,bool, bool)) = Cola()
    colaOrdenada: Cola((str,int,bool,bool)) = Cola()
    while not c.empty() :
        persona: (str,int,bool,bool) = c.get() 
        caux.put(persona)
        if persona[3] :            ## Si es una persona con Prioridad 1, se agrega a la Cola de Prioridad 1
            colaPrioridad1.put(persona)
        elif persona[2] :       ## Si es una persona con Prioridad 2, se agrega a la Cola de Prioridad 2 
            colaPrioridad2.put(persona)
        else :         ## Si la persona no tenia ninguna prioridad, la agrego a una Cola del Resto de personas 
            colaResto.put(persona)  
    while not colaPrioridad1.empty() :   ## Aca paso las personas con prioridad 1 a la Cola Ordenada
        colaOrdenada.put(colaPrioridad1.get())
    while not colaPrioridad2.empty() :   ## Aca paso las personas con prioridad 2 a la Cola Ordenada
        colaOrdenada.put(colaPrioridad2.get()) 
    while not colaResto.empty() :   ## Aca paso las personas que no tenian ninguna prioridad a la Cola Ordenada
        colaOrdenada.put(colaResto.get())
    while not caux.empty() :         ## Aca restauro el parametro c: IN, para que a la salida no se modifique
        c.put(caux.get())
    print('cOUT :',c.queue)
    print('colaOrdenada :',colaOrdenada.queue)
    return colaOrdenada 

# Ejercicio19------------------------------------------------------------------------------------------------------------------
def agrupar_por_longitud(nombreArchivo: str)->dict:
    archivo = open(nombreArchivo, 'r', encoding='utf-8')
    contenido = archivo.read().lower()
    archivo.close()
    sinSaltosDelinea: str = contenido.replace('\n', ' ').replace(',','')
    print(sinSaltosDelinea)
    listaPalabras: [str] = sinSaltosDelinea.split()
    print(listaPalabras)
    dict = {}
    for palabra in listaPalabras :  ## en este for creo el diccionario solucion pero desordenado
        longitud_en_letras = len(palabra)
        if not longitud_en_letras in dict :
            dict[longitud_en_letras]=1
        else : dict[longitud_en_letras] = dict[longitud_en_letras] + 1
    print(dict) ## {7: 3, 5: 3}
    diccionarioOrd = {}
    for i in range(len(dict)) :      ## en este for ordeno el diccionario solucion de menor a mayor 
        minimo = min(dict.keys())
        diccionarioOrd[minimo]=dict[minimo]
        del(dict[minimo])
    print(diccionarioOrd)
    return diccionarioOrd
# agrupar_por_longitud('ejercicio5.txt')

# Ejercicio20------------------------------------------------------------------------------------------------------------------
def promedioDeTodosLosEstudiantes(nombreArchivo: str)->dict:
    archivo = open("ejercicio7.csv", 'r', encoding='utf-8')
    contenido = archivo.read()
    print(contenido)
    lineas = contenido.split('\n')
    print(lineas)
    dict = {}
    for i in range(len(lineas)) :
        lista: [str,str,str,float] = lineas[i].replace(' ','').split(',')
        if not lista[0] in dict :
            dict[lista[0]] = int(lista[3])
        else : 
            dict[lista[0]] = dict[lista[0]] + int(lista[3]) 
    print(dict)
    for i in range(len(dict)) :
        libretaUniversitaria = list(dict.keys())[i]
        cantidadNotas: int = contenido.count(libretaUniversitaria)
        dict[libretaUniversitaria] = dict[libretaUniversitaria] / cantidadNotas
    print(dict)
    archivo.close()
    return dict

# promedioEstudiante("ejercicio7.csv", "123/20")

# Ejercicio21------------------------------------------------------------------------------------------------------------------
def la_palabra_mas_frecuente(nombre_archivo: str)->str:
    archivo = open(nombre_archivo, 'r', encoding='utf-8')
    contenido = archivo.read()
    print(contenido)
    textoSinSaltosDeLinea = contenido.replace('\n', ' ').replace(',','').lower()
    print(textoSinSaltosDeLinea)
    listaPalabras = textoSinSaltosDeLinea.split()
    print(listaPalabras)
    dict = {}
    while listaPalabras != [] :
        apariciones = listaPalabras.count(listaPalabras[0])
        dict[listaPalabras[0]] = apariciones
        listaPalabras = (' '.join(listaPalabras).replace(listaPalabras[0],'')).split()
    print(dict)
    palabraFrecuente : str
    maximo = max(dict.values())
    print(maximo)
    for clave in dict :
        if dict[clave] == maximo :
            palabraFrecuente = clave 
    print (palabraFrecuente)
    return palabraFrecuente
# la_palabra_mas_frecuente('ejercicio5.txt')

# Ejercicio22------------------------------------------------------------------------------------------------------------------
# 22.1)-----------------------------------------------------------



# 22.2)-----------------------------------------------------------



# 22.3)-----------------------------------------------------------



# 22.4)-----------------------------------------------------------






# Ejercicio23------------------------------------------------------------------------------------------------------------------
# 23.1)-----------------------------------------------------------



# 23.2)-----------------------------------------------------------



# 23.3)-----------------------------------------------------------



# 23.4)-----------------------------------------------------------




    

    


