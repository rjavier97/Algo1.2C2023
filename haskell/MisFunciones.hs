module MisFunciones where

fib :: Int -> Int 
fib 0 = 0
fib 1 = 1 
fib n = fib (n-1) + fib (n-1) 

{- Formato de un caso de test en HUnit -}

-- El nombre del archivo debe coincidir con el nombre del modulo -- 


-- ”Nombre del test ” ˜: <res obtenido> ˜?= <res esperado>

{- Ejemplos:
” El doble de 4 es 8” ˜: (doble 4) ˜?= 8 
” Maximo repetido ” ˜: (maximo [ 2 , 7 , 3 , 7 , 4 ] ) ˜?= 7
” esPar de impar ” ˜: ( esPar 5 ) ˜?= False    
-}

{-} Crear test unitarios para la funcioon fib: Int -> Int que
devuelve el i-esimo numero de Fibonacci 

problema fib (n: Z) : Z {
requiere: { n ≥ 0 }
asegura: { res = f ib(n) }
-}      



