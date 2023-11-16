# Ejercicio 1 --------------------------------------------------------
"""
problema acomodar (in s: seq⟨String⟩) : seq⟨String⟩ {
  requiere: { Todos los elementos de s son o bien "LLA" o bien "UP"}
  asegura: {|res| = |s|}
  asegura: { Todos los elementos de res son o bien "LLA" o bien "UP"}
  asegura: {res contiene la misma cantidad de elementos "UP" que s}
  asegura: {res contiene todas las apariciones de "UP" antes de las apariciones de "LLA"}
}
Por ejemplo, dada
s = ["LLA", "UP", "LLA", "LLA", "UP"]
se debería devolver res = ["UP", "UP", "LLA", "LLA", "LLA"]
"""
def acomodar(s1: list) -> list:     
    res:[str] = []
    listaUP:[str] = []
    listaLLA:[str] = []
    for elemento in s1 :
        if elemento == 'UP' :
            listaUP.append('UP')
        else :
            listaLLA.append('LLA')
    res = listaUP + listaLLA
    return res 

# Ejercicio 2 --------------------------------------------------------
"""
problema pos_umbral (in s: seq⟨Z⟩, in u: Z) : Z {
  requiere: u ≥ 0
  asegura: {res=-1 si el umbral no se supera en ningún momento }
  asegura: {Si el umbral se supera en algún momento, res es la primera posición tal que la sumatoria de los 
    primeros res+1 elementos (considerando solo aquellos que son positivos) es estrictamente mayor que el umbral u }
}
Por ejemplo, dadas
s = [1,-2,0,5,-7,3]
u = 5
se debería devolver res = 3
"""
def pos_umbral(s: list, u: int) -> int:
    res : int = 0 
    suma: int = 0 
    for i in range(len(s)):
        if suma <= u and s[i]>=0 :
            suma = suma + s[i]
            res = i 
    if suma <= u :
        res = -1        
    return res 

# Ejercicio 3 --------------------------------------------------------
"""
problema columnas_repetidas(in mat:seq⟨seq⟨Z⟩⟩ ) : Bool {
  requiere: {|mat| > 0}
  requiere: {todos los elementos de mat tienen igual longitud m, con m > 0 (los elementos de mat son secuencias)}
  requiere: {todos los elementos de mat tienen longitud par (la cantidad de columnas de la matriz es par)}
  asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a las últimas m/2 columnas}
}
Por ejemplo, dada la matriz
m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
se debería devolver res = true
TIP: para dividir un número entero x por 2 y obtener como resultado un número entero puede utilizarse la siguiente 
instrucción: int(x/2)
"""
def columnas_repetidas(m: list) -> bool:
    compararColumnas: int = int(len(m[0])/2)
    res: bool = True
    for fila in m :
        for i in range(compararColumnas) :
            if fila[i] != fila[i+compararColumnas] :
                res = False
    return res 

# Ejercicio 4 --------------------------------------------------------
""" 
problema cuenta_posiciones_por_nacion(in naciones: seq⟨String⟩, in torneos: dict⟨Z,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
  requiere: {naciones no tiene elementos repetidos}
  requiere: {Los valores del diccionario torneos son permutaciones de la lista naciones (es decir, tienen exactamente 
            los mismos elementos que naciones, en cualquier orden posible)}
  asegura: {res tiene como claves los elementos de naciones}
  asegura: {El valor en res de una nación es una lista de |naciones| elementos que indica en la posición i cuántas veces 
            salió esa nación en la i-ésima posición.}
}
Por ejemplo, dados
naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0], "sud": [0,2,0,0]}
"""
def cuenta_posiciones_por_nacion(naciones: list, torneos: dict) -> dict:
    lista_ceros = [0]*len(naciones) 
    res:dict = {}
    for pais in naciones :       ## Aca me armo el esqueleto del diccionario resultado. Solo queda ir modificando las values 
        res[pais] = lista_ceros.copy()
    resultado = res.copy() 
    for clave in res :               ## Aca voy a ir modificando el diccionario resultado
        for elemento in list(torneos.values()) :
            for i in range(len(elemento)) :
                if elemento[i] == clave :
                    resultado[clave][i] = resultado[clave][i] + 1
    return resultado