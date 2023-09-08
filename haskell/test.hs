doubleMe x = x + x

f2 :: Float -> Float 
f2 n | n == 1 = 15
     | n == -1 = -15

f6 :: Float -> Int -> Bool
f6 a b = truncate a == b     
-- truncate: funcion que toma la parte entera de un numero real . Aca se leeria: (truncate a) == b 