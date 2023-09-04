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


digitoUnidades1 :: Integer -> Integer
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
--b)
todoMenor1 :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor1 (a,b) (c,d) = (a<=c)&&(b<=d)

todoMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor v w = ((fst v)<=(fst w))&&((snd v)<=(snd w))