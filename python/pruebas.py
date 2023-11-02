archivo = open('archivo.txt', 'r', encoding="utf-8") #encoding="utf-8" con ese parametro los caracteres especiales se ven bien
lineas = archivo.readlines( )
# print(lineas)
# contenido = archivo.read()
# print(contenido)
# print(archivo)
## <_io.TextIOWrapper name='archivo.txt' mode='r' encoding='utf-8'>
# print(contenido)
# Oid mortales, el grito sagrado
# ¡Libertad! ¡Libertad! ¡Libertad!
# Oid el ruido de rotas cadenas
# Ved en trono a la noble igualdad
# print(len(contenido))
# # 126
# print(contenido[125])
# d  -> es la ultima letra del archivo de texto, es decir igualdaD
# lineas = archivo.readlines()
# print(lineas)
archivo.close()
# se cierra el archivo 