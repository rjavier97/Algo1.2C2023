doubleMe x = x + x

-- Guia 3, Ejercicio 1
-- a)
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- c)
h :: Integer -> Integer
h n = f (g(n))

k :: Integer -> Integer
k n = g (f(n))

-- Ejercicio 2
-- a)
absoluto :: Integer -> Integer
absoluto n = abs n

-- b)
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m | (abs n)>=(abs m) = n
                   | otherwise = m

-- c)
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | (x>=y && x>=z) = x
              | (y>=z) = y
              | otherwise = z

-- d)
algunoEs0 :: Float -> Float -> Bool
algunoEs0 n m = (n==0 || m==0)

algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM 0 m = True
algunoEs0PM n 0 = True
algunoEs0PM _ _ = False

-- e)
ambosSon0 :: Float -> Float -> Bool
ambosSon0 n m = (n==0 && m==0)

ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ _ = False

-- f)
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo x y = ((x<=3)&&(y<=3)) || ((x>3)&&(x<=7))&&((y>3)&&(y<=7)) || ((x>7)&&(y>7))

-- g)    
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | (x==y) && (y==z) = x
                    | (x==y) = x+z
                    | (y==z) = x+y
                    | otherwise = x+y+z

-- h)
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y = ((mod x y)==0)

-- i) 
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10


digitoUnidades1 ::  Integer -> Integer
digitoUnidades1 n | n<10 = n
                  | otherwise = digitoUnidades1 (n-10)  
                        
-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas n | n<10 = 0
                | otherwise = digitoUnidades (div (n-(digitoUnidades n)) 10)
                
{- Ejercicio 3
a.a + a.b.k = 0  -> a + b.k = 0 (se puede dividir por a, ya que a nunca es cero) ->  bk=-a   ->   k = -a/b
es decir, k es entero si a es divisible por b, y entonces su resto será 0
es decir, mod a b = 0  -}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y = (x/=0)&&(y/=0)&&(mod x y == 0)

-- Ejercicio 4
--a)
prodInt :: (Integer, Integer) -> (Integer, Integer) -> Integer 
prodInt (a,b) (c,d) = a*c + b*d

--b)
todoMenor1 :: (Float, Float) -> (Float, Float) -> Bool
todoMenor1 (a,b) (c,d) = (a<=c)&&(b<=d)
                                                                -- Va Float en vez de Integer, ya que son Reales
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor v w = ((fst v)<=(fst w))&&((snd v)<=(snd w))

--c) d = raiz(a**2 + b**2) -> d = raiz( (x1-x2)**2 + (y1-y2)**2 ) , con v=(x1,x2) y w=(y1,y2) 
distanciaPuntos :: (Float, Float) -> (Float,Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt( (a-c)**2 + (b-d)**2 )

--d)
sumaTerna :: (Integer,Integer,Integer) -> Integer
sumaTerna (a,b,c) = a+b+c

--e) 
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | (mod a n ==0)&&(mod b n ==0)&&(mod c n ==0) = a+b+c
                             | (mod a n ==0)&&(mod b n /=0)&&(mod c n /=0) = a
                             | (mod a n ==0)&&(mod b n ==0)&&(mod c n /=0) = a+b
                             | (mod a n ==0)&&(mod b n /=0)&&(mod c n ==0) = a+c
                             | (mod a n /=0)&&(mod b n ==0)&&(mod c n /=0) = b
                             | (mod a n /=0)&&(mod b n ==0)&&(mod c n ==0) = b+c
                             | (mod a n /=0)&&(mod b n /=0)&&(mod c n ==0) = c
                             | otherwise = 0  
{-}
sumarSoloMultiplos1 :: (Integer, Integer, Integer) -> Integer -> Integer   
sumarSoloMultiplos1 (a,b,c) n | (n>=1)&&(mod a n ==0) = a + sumarSoloMultiplos1 (b,a,c)        
-}

--f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a,b,c) | (mod a 2 == 0) =1
                     | (mod b 2 == 0) =2
                     | (mod c 2 == 0) =3 
                     | otherwise = 4

--g)
crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)          

--h) 
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a) 

-- Guia4: Recursion sobre enteros --------------------------
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
             fibonacci 5 = 3 + 2 = 5
             fibonacci 6 = fibonacci(5) + fibonacci(4)
             fibonacci 6 = 5 + 3 = 8                         -}

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
              | otherwise = parteEntera (n-1) + 1 

parteEntera1 :: Float -> Integer
parteEntera1 x | (0<=x && x<1) = 0 
               | (-1<=x) && (x<0) = -1
               | x>1 = parteEntera (x-1) + 1 
               | x < -1 = parteEntera(x+1) -1 

parteEntera2 :: Float -> Integer 
parteEntera2 n | 0<=n && n<1 = 0 
               | x>1 = parteEntera2 (n-1) +1
               | otherwise = parteEntera2 (n+1) -1                               



