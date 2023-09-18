--Práctica 4 - Ejercicio 13 	f(n,m)
 
sumatoriaDoble :: Int -> Int -> Int 
sumatoriaDoble 0 _ = 0
sumatoriaDoble x y = sumatoriaDoble (x-1) y + sumatoriaInterna x y 

sumatoriaInterna :: Int -> Int -> Int 
sumatoriaInterna _ 0 = 0
sumatoriaInterna x y = x ^ y + sumatoriaInterna x (y-1)

test_sumatoria_1 = sumatoriaDoble 2 10 == 2056
test_sumatoria_2 = sumatoriaDoble 1 10 == 10
tests = [test_sumatoria_1, test_sumatoria_2]