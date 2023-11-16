def matriz_espejada(m: list)->bool:
    res: bool = True 
    for fila in m :
        if fila != fila[::-1] :
            res = False 
    return res 

# print(matriz_espejada([[1,2,2,1],[1,0,0,1]]))


def columnas_repetidas(m:list)->bool:
    res: bool = True
    columnas: int = int(len(m[0])/2)
    for fila in m :
        for i in range(columnas):
            if fila[i] != fila[i+columnas] :
                res = False
    return res 

# print(columnas_repetidas([ [1,3], [1,3] ]) )
# print(columnas_repetidas([ [1,3,1,3],[0,3,0,3] ]))
# print(columnas_repetidas([ [2,5,3,2,5,3],[0,1,4,0,1,8] ]))

# [1 3]         [1 3 1 3]     [2 5 3 2 5 3 ]     
# [1 3]         [0 3 0 3]     [0 1 4 0 1 8 ]
# False           True            False 

