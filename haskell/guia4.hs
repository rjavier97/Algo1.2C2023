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

--Ejercicio3--------------------------------------------------------------------------------------------------------------------
esDivisible :: Integer -> Integer -> Bool   
esDivisible a b | (a<b) = False
                | (a-b)==0 = True                      -- el ejercicio pedia NO USAR mod ni div
                | otherwise = esDivisible (a-b) b 

--Ejercicio4--------------------------------------------------------------------------------------------------------------------
sumaImpares :: Integer -> Integer
sumaImpares n = sumaImparesDesde n 1 1 

--FuncionesAuxiliares
esImpar :: Integer -> Bool
esImpar n = (mod n 2) /= 0

sumaImparesDesde :: Integer -> Integer -> Integer -> Integer
sumaImparesDesde n i k | n<k = 0
                       | n==1 = 1    
                       | otherwise = i + sumaImparesDesde n (i+2) (k+1)         -- k = contador de vueltas                        
    
--Ejercicio5--------------------------------------------------------------------------------------------------------------------
medioFact :: Integer -> Integer       -- Programa que dado n ∈ N calcula n!! = n(n−2)(n−4).....
medioFact n | n==0 || n==1 = 1 
            | otherwise = n*(medioFact (n-2))

--Ejercicio6--------------------------------------------------------------------------------------------------------------------
sumaDigitos :: Integer -> Integer
sumaDigitos n | n<10 = n                                  --- con (mod n 10) tengo el digito de las unidades: 125→5
              | otherwise = (mod n 10) + sumaDigitos (div n 10)    --- con (div n 10) saco el ultimo digito de un numero: 125→12

--Ejercicio7--------------------------------------------------------------------------------------------------------------------
todosDigitosIguales :: Integer -> Bool      --  determina si todos los dígitos de un numero natural son iguales
todosDigitosIguales n | n<10 = True
                      | otherwise = ((mod n 10)==(mod (div n 10) 10)) && (todosDigitosIguales (div n 10))           
-- (mod (div n 10) 10) lo que hace es darme el DigitoDecenas, es decir, el anteultimo numero  

--Ejercicio8--------------------------------------------------------------------------------------------------------------------
iesimoDigito :: Integer -> Integer -> Integer    -- dado un n ∈ N≥0 y un i ∈ N menor o igual a la cantidad de dígitos de n,
iesimoDigito n i = mod (div n (10^(cantDigitos(n) - i))) 10                       -- devuelve el i-ésimo dígito de n.

iesimoDigito1 :: Integer -> Integer -> Integer
iesimoDigito1 n i | (n>=0)&&(i>=1)&&(i<=cantDigitos(n)) = mod (div n (10^(cantDigitos(n) - i))) 10  
                  | otherwise = undefined       -- Otra opcion usando el Requiere de la especificacion

--funcion auxiliar cantDigitos
cantDigitos :: Integer -> Integer
cantDigitos n | n<10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

--Ejercicio9--------------------------------------------------------------------------------------------------------------------
esCapicua :: Integer -> Bool 
esCapicua n = extremosIguales n 1

-- Funcion auxiliar extremosIguales,  que me va comparando los extremos de un numero, empezando por el indice i 
extremosIguales :: Integer -> Integer -> Bool
extremosIguales n i | n<10 || (i>cantDigitos(n)) = True
                    | otherwise = (mod n 10)==(iesimoDigito n i) && (extremosIguales (div n 10) (i+1))             

--Ejercicio10--------------------------------------------------------------------------------------------------------------------
--Funcion Auxiliar f2Generico, a partir de esta funcion se puede resolver automaticamente a), b), c) y d)

f2Generico :: Float -> Integer -> Integer -> Integer -> Float      ----- Funcion f2 generica, para cualquier q, n, i y j 
f2Generico q n i j | (j<i)||(q==0) = 0                           --- donde q=base, n= valor que le da forma a i o j, como en f3
                   | i==j = q^i                                 ---- donde i= desde donde va la sumatoria (limite inferior)
                   | otherwise = (f2Generico q n i (j-1)) + q^j  ---- donde j= hasta donde va la sumatoria (limite superior)

--a) 
f1 :: Integer -> Integer                  -- Funcion f1 que pedia el ejercicio, usando f2Generico 
f1 n = truncate (f2Generico 2 n 0 n)      -- y Truncate para transformar el resultado Float de f2Generico en Integer

f11 :: Integer -> Integer                 
f11 0 = 1                                 -- Otra opcion (esto habia pensado primero)
f11 n = 2^n + f11 (n-1) 

--b)
f2 :: Integer -> Float -> Float      -- funcion que pedia el ejercicio
f2 n q = f2Generico q n 1 n 

f2Aux :: Float -> Integer -> Integer -> Float
f2Aux q i n | i==n = q^i                        --- primer intento de sumatoria q^i generica, sin variable j (limite sup)
            | otherwise = (f2Aux q i (n-1)) + q^n   

--c)
f3 :: Integer -> Float -> Float     
f3 n q = f2Generico q n 1 (2*n)  

{- Otra forma de pensarlo
Sumatoria q^i con i=1 hasta j=2n  ←-|-→ Sumatoria q^(i+n) con i=1-n hasta j=n ←-|-→ 
Sumatoria (q^i)*(q^n) con i=1-n hasta j=n ←-|-→ (q^n)* Sumatoria q^i con i=1-n hasta j=n
-}                                       

--d)
f4 :: Integer -> Float -> Float 
f4 n q = f2Generico q n n (2*n)      -- el 3º parametro representa a i, el 4º parametro representa a j

--Ejercicio11--------------------------------------------------------------------------------------------------------------------
--a)
--Funcion Auxiliar factorial
factorial :: Float -> Float
factorial n | n==0 = 1
            | otherwise = n*factorial(n-1)

-- fromIntegral :: Int -> Float      funcion predefinida en el Preludio de Haskell
eAprox :: Integer -> Float
eAprox n | n==0 = 1
         | otherwise = (1 / factorial(fromIntegral n)) + eAprox(n-1)  

--b)
e :: Float
e = eAprox 10 

--Ejercicio12--------------------------------------------------------------------------------------------------------------------
raizDe2Aprox :: Integer -> Float

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