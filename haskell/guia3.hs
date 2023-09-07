-- Guia3: Ejercicio 1-------------------------------------------------
-- a)
fx :: Integer -> Integer
fx 1 = 8
fx 4 = 131
fx 16 = 16

-- b)
gx :: Integer -> Integer
gx 8 = 16
gx 16 = 4
gx 131 = 1

-- c)
h :: Integer -> Integer
h n = fx (gx(n))

k :: Integer -> Integer
k n = gx (fx(n))

-- Ejercicio 2------------------------------------------------
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

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div (n-(digitoUnidades n)) 10
                        
-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas n | n<10 = 0
                | otherwise = digitoUnidades (sacarUltimoDigito n)

{- Ejercicio 3------------------------------------------------
a.a + a.b.k = 0  -> a + b.k = 0 (se puede dividir por a, ya que a nunca es cero) ->  bk=-a   ->   k = -a/b
es decir, k es entero si a es divisible por b, y entonces su resto será 0
es decir, mod a b = 0  -}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y = (x/=0)&&(y/=0)&&(mod x y == 0)

-- Ejercicio 4-------------------------------------------------
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

--Ejercicio 5------------------------------------------------
--funciones auxiliares f y g , para resolver problema todosMenores
f :: Integer -> Integer 
f n | n<=7 = n^2 
    | otherwise = 2*n -1 

g :: Integer -> Integer 
g n | (mod n 2 == 0) = div n 2 
    | otherwise = 3*n +1   

todosMenores :: (Integer, Integer, Integer) -> Bool 
todosMenores (n1, n2, n3) = ((f n1)>(g n1)) && ((f n2)>(g n2)) && ((f n3)>(g n3))

--Ejercicio 6--------------------------------------------------
-- Programa que me dice si un año es bisiesto o no
bisiesto :: Integer -> Bool
bisiesto n = not ( (mod n 4 /=0) || ((mod n 100 ==0)&&(mod n 400 /= 0)) )   -- version que pedia el ejercicio
{- ( (mod n 100 ==0)&&(mod n 400 /= 0) ) si en vez de esa expresion hubiese sido,
( (mod n 100 ==0)&&(mod n 400 == 0) ), alcanzaba con solo poner (mod n 400 ==0),
ya que (mod n 400 ==0) implica que (mod n 100 == 0), pero no al revés  -}

bisiesto1 :: Integer -> Bool
bisiesto1 n = (mod n 4 ==0) && (mod n 400 /= 0)   -- no funciona

bisiesto2 :: Integer -> Bool
bisiesto2 n = (mod n 4 ==0) && ( (mod n 100 /=0)||(mod n 400 == 0) )   -- otra version (use regla de DeMorgan)

bisiesto3 :: Integer -> Bool
bisiesto3 n = (mod n 400 == 0) || ( (mod n 4 ==0)&&(mod n 100 /=0) ) -- otra version(aca use la aclaracion que hice en bisiesto n)

{- Conclusion: 1) si un año es bisiesto entonces es divisible por 4
               2) si un año es divisible por 400 entonces es bisiesto -}



