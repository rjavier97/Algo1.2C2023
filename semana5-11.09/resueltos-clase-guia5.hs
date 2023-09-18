hayRepetidos :: Eq a => [a] -> Bool
hayRepetidos xs | xs == [] = False
                | tail(xs) == [] = False
                | otherwise = (pertenece (head(xs)) (tail(xs))) || (hayRepetidos (tail(xs)))

pertenece :: Eq a => a -> [a] -> Bool
pertenece x xs | xs == [] = False
               | x == head(xs) = True
               | otherwise = pertenece x (tail(xs))



maximo :: Ord a => [a] -> a
maximo (x:xs) | xs == [] = x
              | x > head(xs) = maximo (x: (tail xs))
              | otherwise = maximo ((head xs): (tail xs))


maximo2 :: Ord a => [a] -> a
maximo2 [x] = x
maximo2 (x:y:xs)| x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)



ordenar :: Ord a => [a] -> [a]
ordenar [] = []
ordenar xs = ordenar ((quitar (max_xs) xs)) ++ [max_xs]
             where max_xs = maximo xs



ordenar2 :: Ord a => [a] -> [a]
ordenar2 [] = []
ordenar2 xs = agregarAtras max_xs (ordenar2 (quitar max_xs xs))
              where max_xs = maximo xs


agregarAtras :: a -> [a] -> [a]
agregarAtras elem [] = [elem]
agregarAtras elem (primero:cola) = primero:(agregarAtras elem cola)


quitar :: Eq a => a -> [a] -> [a]
quitar x [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y: (quitar x ys)



descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (factorizacion x) : descomponerEnPrimos xs

factorizacion :: Int -> [Int]
factorizacion n = primosQueDividenDesde 2 n

primosQueDividenDesde :: Int -> Int -> [Int]
primosQueDividenDesde d n | d > n = []
                          | esPrimo d && mod n d == 0 = d : primosQueDividenDesde d (div n d)
                          | otherwise = primosQueDividenDesde (d+1) n

esPrimo :: Int -> Bool
esPrimo n = cantidadDivisoresHasta n n == 2

cantidadDivisoresHasta :: Int -> Int -> Int
cantidadDivisoresHasta n 1 = 1
cantidadDivisoresHasta n d | mod n d == 0 = 1 + cantidadDivisoresHasta n (d-1)
                           | otherwise = cantidadDivisoresHasta n (d-1)                




{--
Probando las funciones
--}

tests_repetidos = [test_sin_repetidos, test_con_repetidos_1, test_con_repetidos_2, test_1elemento_repetidos,test_vacio_repetidos]

test_sin_repetidos = hayRepetidos [1,2,3,4] == False
test_con_repetidos_1 = hayRepetidos [1,2,3,1] == True
test_con_repetidos_2 = hayRepetidos [1,2,3,1,4] == True
test_1elemento_repetidos = hayRepetidos [1] == False
test_vacio_repetidos = hayRepetidos @Integer [] == False

test_pertenece_true_1 = pertenece 1 [1,2,3] == True
test_pertenece_true_2 = pertenece 1 [2,1,3] == True
test_pertenece_false_1 = pertenece 7 [2,1,3] == False
test_pertenece_vacio = pertenece 1 [] == False
                           