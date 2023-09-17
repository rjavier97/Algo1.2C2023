doubleMe x = x + x

f22 :: Float -> Float 
f22 n | n == 1 = 15
      | n == -1 = -15

f6 :: Float -> Int -> Bool
f6 a b = truncate a == b     
-- truncate: funcion que toma la parte entera de un numero real . Aca se leeria: (truncate a) == b 


f2Generico :: Float -> Integer -> Integer -> Float  --- Funcion f2 generica, para cualquier q, i, j 
f2Generico q i j | (j<i)||(q==0) = 0                          ---- donde q=base 
                 | otherwise = (f2Generico q i (j-1)) + q^j   ---- donde i= desde donde va la sumatoria (limite inferior)
                                                              ---- donde j= hasta donde va la sumatoria (limite superior)
                                                              ---- i y j pueden depender de n, como en f3 y f4

--------------------------------------------------------------------------------------------------------------
f1 :: Integer -> Integer                  -- Funcion f1 que pedia el ejercicio, usando f2Generico 
f1 n = truncate (f2Generico 2 0 n)                     
--------------------------------------------------------------------------------------------------------------
f2 :: Integer -> Float -> Float      -- funcion que pedia el ejercicio
f2 n q = f2Generico q 1 n 
--------------------------------------------------------------------------------------------------------------
f3 :: Integer -> Float -> Float     
f3 n q = f2Generico q 1 (2*n)  
--------------------------------------------------------------------------------------------------------------
f4 :: Integer -> Float -> Float 
f4 n q = f2Generico q n (2*n) 