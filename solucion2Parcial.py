# Ejercicio 1
def intercalar(s1: list, s2: list) -> list:
    res : list = []
    for i in range(0,len(s1)):
        res.append(s1[i])
        res.append(s2[i])
    return res

# Ejercicio 2
def pos_nesima_aparicion(s: list, n: int, elem: int) -> int:
    res : int = 0
    contador : int = 0
    posiciones : list = []
    for i in range(0,len(s)):
        if s[i] == elem:
            contador += 1
            posiciones.append(i)
    if contador < n:
        res = -1
    else:
        res = posiciones[n-1]
    return res


# Ejercicio 3
def matriz_espejada(m: list) -> bool:
    res : bool = True
    for fila in m:
        reverso : list = []
        for elemento in fila:
            reverso.insert(0,elemento)
        if fila != reverso:
            res = False
            break
    return res

# Ejercicio 4
def cuenta_posiciones_por_caballo(caballos: list, carreras: dict) -> dict:
    res = dict()
    for caballo in caballos:
        res[caballo] = [0]*len(caballos)
    print(res)
    for v in carreras.values():
        for i in range(len(v)):
            res[v[i]][i] += 1
    return res

Tu parcial fue recibido correctamente.
Tu comprobante es: wZQBwLdu
Por favor cerra tu browser. 