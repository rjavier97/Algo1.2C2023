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
sumaImparesDesde n i k | n<k = 0    -- es 0 porque quiere decir que ya conté mas de los primeros n numeros impares
                       | n==1 = 1   -- es decir, voy a contar hasta n==k, una vez que me paso (n<k),dejo de contar,por eso vale 0 
                       | otherwise = i + sumaImparesDesde n (i+2) (k+1)         -- k = contador de vueltas                        
-- la linea n==1 = 1, si se elimina no modifica el programa, ya que se contempla en el otherwise

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

f2Generico :: Float -> Integer -> Integer -> Float      ----- Funcion f2 generica, para cualquier q, i y j 
f2Generico q i j | (j<i)||(q==0) = 0                         ---- donde q=base,                            
                 | otherwise = (f2Generico q i (j-1)) + q^j  ---- donde i= desde donde va la sumatoria (limite inferior)
                                                             ---- donde j= hasta donde va la sumatoria (limite superior)
                                                             ---- i y j pueden depender de n, como en f3 y f4
--a) 
f1 :: Integer -> Integer                  -- Funcion f1 que pedia el ejercicio, usando f2Generico 
f1 n = truncate (f2Generico 2 0 n)      -- y Truncate para transformar el resultado Float de f2Generico en Integer

f11 :: Integer -> Integer                 
f11 0 = 1                                 -- Otra opcion (esto habia pensado primero)
f11 n = 2^n + f11 (n-1) 

--b)
f2 :: Integer -> Float -> Float      -- funcion que pedia el ejercicio
f2 n q = f2Generico q 1 n 

f2Aux :: Float -> Integer -> Integer -> Float
f2Aux q i n | i==n = q^i                        --- primer intento de sumatoria q^i generica, sin variable j (limite sup)
            | otherwise = (f2Aux q i (n-1)) + q^n   

--c)
f3 :: Integer -> Float -> Float     
f3 n q = f2Generico q 1 (2*n)  

{- Otra forma de pensarlo
Sumatoria q^i con i=1 hasta j=2n  ←-|-→ Sumatoria q^(i+n) con i=1-n hasta j=n ←-|-→ 
Sumatoria (q^i)*(q^n) con i=1-n hasta j=n ←-|-→ (q^n)* Sumatoria q^i con i=1-n hasta j=n
-}                                       

--d)
f4 :: Integer -> Float -> Float 
f4 n q = f2Generico q n (2*n)      -- el 2º parametro representa a i, el 3º parametro representa a j

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
sucesionAn :: Integer -> Float
sucesionAn n | n==1 = 2
             | otherwise = 2 + (1 / sucesionAn (n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesionAn n) - 1        
            
--Ejercicio13--------------------------------------------------------------------------------------------------------------------
sumaInt :: Integer -> Integer -> Integer -> Integer       ----- i^j   con i variando y con j fijo
sumaInt n i j | i==n = i^j                                ----- n es la base y el limiteSup, i el limite inferior, j el exponente
              | otherwise = (sumaInt (n-1) i j) + (n^j)         

sumaExt :: Integer -> Integer -> Integer -> Integer       ----- i^m   con i fijo y con m variando
sumaExt n i m | i==m = n^i                                ----- n es la base, i el limite inferior, m el exponente y limiteSup
              | otherwise = (sumaExt n i (m-1)) + n^m       

sumaDoble :: Integer -> Integer -> Integer
sumaDoble n m  | (n==0)||(m==0) = 0 
               | otherwise = (sumaDoble (n-1) m) + (sumaExt n 1 m)

--Ejercicio14--------------------------------------------------------------------------------------------------------------------
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m | (n==0) = 0 
                    | otherwise = (sumaPotenciasAux q n 1 m) + (sumaPotencias q (n-1) m)

sumaPotenciasAux :: Integer -> Integer -> Integer -> Integer -> Integer     -- Sumatoria q^(k+i) , con q y k fijo,   
sumaPotenciasAux q k i j | (j<i)||(q==0) = 0                -- i= limite inferior, j=limite superior (i,j variando)                                                            -
                         | otherwise = q^(k+j) + (sumaPotenciasAux q k i (j-1))   

--Ejercicio15--------------------------------------------------------------------------------------------------------------------
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m | n==0 = 0 
                   | otherwise = (sumaRacionalesAux n 1 m) + sumaRacionales (n-1) m  

sumaRacionalesAux :: Integer -> Integer -> Integer -> Float
sumaRacionalesAux p i j | j<i = 0 
                        | otherwise = ((fromIntegral p)/(fromIntegral j)) + sumaRacionalesAux p i (j-1)

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
--Ejercicio16--------------------------------------------------------------------------------------------------------------------
--a)
menorDivisor :: Integer ->Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n i | (n==1) = 1
                      | (mod n i == 0) = i
                      | otherwise = menorDivisorDesde n (i+1)  
  
--b)
esPrimo :: Integer -> Bool
esPrimo n = (menorDivisor n)==n 

--c)
sonCoprimos :: Integer -> Integer -> Bool                    -- si ambos numeros no tienen divisores en comun mayores estrictos que 1 
sonCoprimos n m | n==1||m==1 = True
                | otherwise = sonCoprimosDesde n m 2 

sonCoprimosDesde :: Integer -> Integer -> Integer ->  Bool
sonCoprimosDesde n m i | i>(esMenor n m) = True
                       | otherwise = (mod (esMayor n m) (menorDivisorDesde (esMenor n m) i) /= 0)&&(sonCoprimosDesde n m (i+1) ) 

esMenor :: Integer -> Integer -> Integer
esMenor n m | n<=m = n 
            | otherwise = m 

--d)
nEsimoPrimo :: Integer -> Integer 
nEsimoPrimo n = nEsimoPrimoDesde n 2 1 

nEsimoPrimoDesde :: Integer -> Integer -> Integer -> Integer          -- n: nEsimoPrimo 
nEsimoPrimoDesde n i k | (n==k)&&(esPrimo i) = i                      -- i: numero que voy sumando de a 1 para ver si esPrimo o no
                       | esPrimo i = nEsimoPrimoDesde n (i+1) (k+1)   -- k: contador de numeros primos 
                       | otherwise = nEsimoPrimoDesde n (i+1) k  

--Ejercicio17--------------------------------------------------------------------------------------------------------------------
esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n i | n<fibonacci(i) = False
                   | (n == fibonacci(i)) = True
                   | otherwise = esFibonacciAux n (i+1)
                
esFibonacci :: Integer -> Bool        
esFibonacci n = esFibonacciAux n 0     

--Ejercicio18: Use 6 funcionesAuxiliares-----------------------------------------------------------------------------------------

{-Estrategia: hacer una funcion que vaya viendo el iesimo digito par de un numero n cualquiera  
luego comparar cada iesimo numero par, y ver si es mas grande que el otro o no , por ultimo, devolver el mas grande iteradamente -}
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = mayorDigitoParDesde n 1  

mayorDigitoParDesde :: Integer -> Integer -> Integer            --- 1234567
mayorDigitoParDesde n i | i>cantDigitos n = -1  
                        | otherwise = esMayor (iesimoPar n i) (mayorDigitoParDesde n (i+1))

iesimoPar :: Integer -> Integer -> Integer 
iesimoPar n i = iesimoParAux n 1 1 i 

iesimoParAux :: Integer -> Integer -> Integer -> Integer -> Integer                       -- n: numero cualquiera
iesimoParAux n k i j | i>cantDigitos n = -1                                              -- k acumulador de digitos pares
                     | ( mod (iesimoDigito n i) 2 == 0)&&(k==j) = iesimoDigito n i     -- i: indice de posicion del digito que se recorre
                     | ( mod (iesimoDigito n i) 2 == 0) = iesimoParAux n (k+1) (i+1) j   -- j: iesimo digito par de un numero
                     | otherwise = iesimoParAux n k (i+1) j 
-- Por ejemplo: iesimoParAux 1234 1 1 2 = 4 
-- Significa: Del numero 1234, dame el segundo digito que sea par. El 4º parametro j (2), es el j-esimoDigitoPar de un numero 

esMayor :: Integer -> Integer -> Integer
esMayor n m | n>=m = n 
            | otherwise = m 

--Ejercicio18: Otra forma de resolverlo sin usar funcionesAuxiliares--------------------------------------------------------------
mayorDigitoPar1 :: Integer -> Integer 
mayorDigitoPar1 n | (n<10)&&(mod n 2 == 0) = n 
                  | (n<10) = -1
                  | (mod n 10 == 8)||(mayorDigitoPar1 (div n 10) ==8) = 8  
                  | (mod n 10 == 6)||(mayorDigitoPar1 (div n 10) ==6) = 6
                  | (mod n 10 == 4)||(mayorDigitoPar1 (div n 10) ==4) = 4
                  | (mod n 10 == 2)||(mayorDigitoPar1 (div n 10) ==2) = 2
                  | (mod n 10 == 0)||(mayorDigitoPar1 (div n 10) ==0) = 0
                  | otherwise = -1 

-- Otra forma de hacerlo, usando solo una funcionAuxiliar. Es misma idea de mayorDigitoPar1 pero mas corto, sin tantas guardas 
-- y menor tiempo en devolver resultado. 
mayorDigitoPar11 :: Integer -> Integer
mayorDigitoPar11 n = mayorDigitoPar11Aux n 8 

mayorDigitoPar11Aux :: Integer -> Integer -> Integer
mayorDigitoPar11Aux n i | (n==0)||(i<0) = -1               
                        | (mod n 10 == i)||(mayorDigitoPar11Aux (div n 10) i ==i) = i
                        | otherwise = mayorDigitoPar11Aux n (i-2)     

--Ejercicio19--------------------------------------------------------------------------------------------------------------------
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosDesde n 1 

--Funciones auxiliares---------------------
esSumaInicialDePrimosDesde :: Integer -> Integer -> Bool
esSumaInicialDePrimosDesde n i | (sumaInicialDeNPrimos i > n) = False 
                               | otherwise = (sumaInicialDeNPrimos i == n) || esSumaInicialDePrimosDesde n (i+1)  

sumaInicialDeNPrimos :: Integer -> Integer
sumaInicialDeNPrimos n = sumaInicialDeNPrimosDesde n 1   

sumaInicialDeNPrimosDesde :: Integer -> Integer -> Integer
sumaInicialDeNPrimosDesde n i | i>n = 0 
                              | otherwise = (nEsimoPrimo i) + sumaInicialDeNPrimosDesde n (i+1) 
                            
--Ejercicio21--------------------------------------------------------------------------------------------------------------------
pitagoras :: Integer -> Integer -> Integer -> Integer 
pitagoras m n r = pitagorasAux m n r 0 0

pitagorasAux :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer 
pitagorasAux m n r q k | ((m<r)&&(n<r)) && (q>mayor) = k    -- caso donde m y n sean mas chicos que r                  
                       | (m<r)&&(n<r)&&(q<= mayor)&&( menor <= cateto ) = pitagorasAux m n r (q+1) (k+(menor +1))   -- caso donde m y n sean mas chicos que r
                       | (m<r)&&(n<r)&&(q<= mayor)&&( menor > cateto) = pitagorasAux m n r (q+1) (k+(cateto +1))  -- caso donde m y n sean mas chicos que r
                       | ((m>=r)||(n>=r)) && (((q^2)>(r^2))||(q>menor)) = k           -- caso donde m o n sean mayores/iguales que r
                       | otherwise = pitagorasAux m n r (q+1) (k+ (cateto +1))     -- caso donde m o n sean mayores/iguales que r
                         where cateto = truncate (sqrt(fromIntegral(r^2 - q^2)))   
                               menor = esMenor m n   
                               mayor = esMayor m n                                                   
-- m y n son los catetos de un triangulo 
-- r es la hipotenusa
-- Q  0≤ Q ≤ mayor              , mayor = esMayor m n 
-- k contador de pares (p,q)              