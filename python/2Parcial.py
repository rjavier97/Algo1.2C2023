def matriz_espejada(m: list)->bool:
    res: bool = True 
    for fila in m :
        if fila != fila[::-1] :
            res = False 
    return res 

print(matriz_espejada([[1,2,2,1],[1,0,0,1]]))
