-- Guia4: Recursion sobre enteros ----------------------------------------------------
-- Ejercicio1
fibonacci :: Integer -> Integer 
fibonacci n | (n==0) = 0
            | (n==1) = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

{- Ejemplos: fibonacci 2 = fibonacci(2-1) + fibonacci(2-2)
             fibonacci 2 = fibonacci(1) + fibonacci(0)
             fibonacci 2 = 1 + 0 = 1 
             fibonacci 3 = fibonacci(3-1) + fibonacci(3-2) 
             fibonacci 3 = fibonacci(2) + fibonacci(1)
             fibonacci 3 = 1 + 1 = 2 
             fibonacci 4 = fibonacci(3) + fibonacci(2) 
             fibonacci 4 = 2 + 1 = 3 
             fibonacci 5 = fibonacci(4) + fibonacci(3)
             fibonacci 5 = 3 + 2                             -}

-- Ejercicio2
{-Ejemplos:
0.2 -> |0| 
1.6 -> |1| ..... 1.6 - 1 = 0.6   ->    1.6 - 0.6 = 1 (resultado)
2.6 -> |2| ..... 2.6 - 1 = 1.6    ->    1.6 - 1     ->     0.6  - >    2.6 - 0.6 = 2 (resultado) 
3.6 -> |3|
4.6 -> |4|
5.8 -> |5| ..... 5.8 - 1 = 4.8 -> 4.8 - 1  ->  3.8 - 1  ->  2.8 - 1  ->  1.8 - 1 -> 0.8  -> 5.8 - 0.8 = 5 (resultado)   
Conclusion: entre modulo  -}
parteEntera :: Float -> Integer
parteEntera n | (n<1) = 0
              | otherwise = parteEntera (n-1) + 1     -- contempla solo numeros positivos

parteEntera1 :: Float -> Integer
parteEntera1 x | (0<=x && x<1) = 0 
               | (-1<=x) && (x<0) = -1
               | x>=1 = parteEntera1 (x-1) + 1 
               | x < -1 = parteEntera1 (x+1) -1 

parteEntera2 :: Float -> Integer 
parteEntera2 n | 0<=n && n<1 = 0 
               | n>=1 = parteEntera2 (n-1) +1
               | otherwise = parteEntera2 (n+1) -1                                   

--Ejercicio13
sumaInt :: Integer -> Integer -> Integer -> Integer       ----- i^j   con i variando y con j fijo
sumaInt n i j | i==n = i^j                                ----- n es la base, i el limite inferior, j el exponente y limiteSup
              | otherwise = (sumaInt (n-1) i j) + (n^j)         

sumaExt :: Integer -> Integer -> Integer -> Integer       ----- i^m   con i fijo y con j variando
sumaExt n i m | i==m = n^i                                ----- n es la base, i el limite inferior, m el exponente y limiteSup
              | otherwise = (sumaExt n i (m-1)) + n^m       

sumaDoble :: Integer -> Integer -> Integer
sumaDoble n m  | (n==0)||(m==0) = 0 
               | otherwise = (sumaDoble (n-1) m) + (sumaExt n 1 m)


--Ejercicio 4-------------------
{-
contarPalabras :: [Char] -> Integer
contarPalabras 

--funciones auxiliares
quitarEspInicialFinal :: [Char] -> [Char]
quitarEspInicialFinal [] = []
quitarEspInicialFinal x:xs | x==' ' && head(reverse xs)==' ' = tail xs 
                           | x==' ' = xs
                           | (head (reverse xs)) ==' ' = tail (x:xs)
-}