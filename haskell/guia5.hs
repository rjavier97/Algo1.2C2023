-- Ejercicio1)

--a)
--longitud :: [t] -> Integer
--longitud (x:xs) | (x:xs)==[] = 0     -- no funciona ya que (x:xs) nunca va a ser vacio 
               -- | otherwise = 1 + longitud(tail (x:xs))     
--a)
longitud :: (Eq t) => [t] -> Integer
longitud a | a==[] = 0
           | otherwise = 1 + longitud (tail (a))

longitud1 :: [t] -> Integer
longitud1 [] = 0
longitud1 (x:xs) = 1 + longitud1 xs

longitud2 :: [t] -> Integer
longitud2 lista | null lista = 0
                | otherwise = 1 + longitud2 (tail (lista))

--b)
ultimo :: (Eq t) => [t] -> t                            -- programa que requiere que la lista no sea vacia
ultimo a | (longitud (a) == 1) = head a                 -- por lo tanto, no hay problema para listas vacias
         | otherwise = ultimo (tail (a))                -- ya que nunca se van a ejecutar

ultimo1 :: (Eq t) => [t] -> t
ultimo1 (x:xs) | (longitud (x:xs) == 1) = x       -- programa que toma el ultimo elemento de una lista cualquiera
               | otherwise = ultimo (xs)          -- toma recursivamente la cola de una lista            
                                                  -- hasta que se encuentre con el ultimo elemento
--c)       
principio :: (Eq t) => [t] -> [t]
principio (x:xs) | (longitud (x:xs) == 1) = []        -- programa que devuelve una lista sin el ultimo elemento
                 | otherwise = [x]++principio (xs)

principio1 :: (Eq t) => [t] -> [t]
principio1 (x:xs) | (longitud (x:xs) == 1) = []       -- programa que devuelve una lista sin el ultimo elemento, sin usar concat
                  | otherwise = x:principio1 (xs)

principio11 :: Eq t => [t] -> [t]
principio11 (x:xs) | (x:xs) == (x:[]) = []
                   | otherwise = [x] ++ principio11 (xs)

--d)       Se puede usar la funcion "reverse", que viene predefinida  
reverso :: Eq t => [t] -> [t]
reverso [] = []
reverso a = [ultimo (a)] ++ reverso (principio11 (a))

reverso1 :: (Eq t) => [t] -> [t]                       -- programa que me devuelve una lista invertida
reverso1 (x:xs) | (longitud (x:xs) ==1) = [x]
                | otherwise = [ultimo1 (x:xs)] ++ reverso1 (principio (x:xs))

reverso2 :: (Eq t) => [t] -> [t]                       -- programa que me devuelve una lista invertida, sin usar concat
reverso2 (x:xs) | (longitud (x:xs) ==1) = [x]
                | otherwise = (ultimo1 (x:xs)) : reverso2 (principio (x:xs))

--Ejercicio2--------------------------------------------------------------------------------------------------------------------
--a)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = (e==x) || pertenece e xs

--b) 
todosIguales :: Eq t => [t] -> Bool
todosIguales (x:[]) = True
todosIguales (y:(x:xs)) = y==x && todosIguales (y:xs)

--c)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:[]) = True
todosDistintos (y:(x:xs)) = (not (pertenece y (x:xs)) ) && todosDistintos (x:xs)

--d) 
hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos a = not (todosDistintos a)

--e)
quitar :: (Eq t) => t -> [t] -> [t]
quitar e (xs) = eliminaPrimeraAparicion e (xs) []

eliminaPrimeraAparicion :: (Eq t) => t -> [t] -> [t] -> [t] 
eliminaPrimeraAparicion e [] a = a 
eliminaPrimeraAparicion e (x:xs) a | (e /= x) = eliminaPrimeraAparicion e xs (a++[x])  
                                   | otherwise = a ++ xs 
 
--f)
quitarTodos :: (Eq t) => t -> [t] -> [t] 
quitarTodos e (xs) = eliminaTodasApariciones e xs []

eliminaTodasApariciones :: (Eq t) => t -> [t] -> [t] -> [t]       
eliminaTodasApariciones _ [] a = a
eliminaTodasApariciones e (x:xs) a | (e /= x) = eliminaTodasApariciones e xs (a++[x])  
                                   | otherwise = eliminaTodasApariciones e xs a

--g)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos xs = eliminarRepetidosAux xs []

eliminarRepetidosAux :: (Eq t) => [t] -> [t] -> [t]
eliminarRepetidosAux [] a = a
eliminarRepetidosAux (x:xs) a | (quitarTodos x xs) == xs = eliminarRepetidosAux xs (a++[x])
                              | otherwise = eliminarRepetidosAux (quitarTodos x xs) (a++[x]) 

--h) 
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = estaIncluido xs ys && estaIncluido ys xs 

estaIncluido :: (Eq t) => [t] -> [t] -> Bool
estaIncluido xs ys | (xs==[]) = True  -- * ya que un conjunto vacio esta incluido en cualquier otro conjunto (conjunto/lista)
                   | (ys==[]) = False  
                   | otherwise = pertenece (head xs) ys && estaIncluido (tail xs) ys 

estaIncluido1 :: (Eq t) => [t] -> [t] -> Bool
estaIncluido1 [] [] = True                  ----  * ver que si la primer lista es vacia, el resultado es True
estaIncluido1 (x:xs) [] = False
estaIncluido1 [] (y:ys) = True              ----  * ver que si la primer lista es vacia, el resultado es True
estaIncluido1 (x:xs) (y:ys) = pertenece x (y:ys) && estaIncluido1 xs (y:ys) 

--i)
capicua :: (Eq t) => [t] -> Bool 
capicua xs = xs == reverse xs 

--Ejercicio3--------------------------------------------------------------------------------------------------------------------
--a)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0 
sumatoria (x:xs) = x + sumatoria xs  

--b)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs 
                                          
--c)
maximo :: (Eq t, Ord t) => [t] -> t
maximo (x:[]) = x 
maximo (x:xs) | (x >= (head xs)) = maximo (x:(tail xs))
              | otherwise = maximo ((head xs):(tail xs))

--d) 
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x+n):(sumarN n xs)

--e)
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs) 

--f)
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo xs = sumarN (ultimo xs) xs

--g)
pares :: [Integer] -> [Integer]
pares [] = []
pares xs = sacarImpares xs []

sacarImpares :: [Integer] -> [Integer] -> [Integer]
sacarImpares [] a = a
sacarImpares (x:xs) a | (mod x 2)==0 = sacarImpares xs (a++[x])
                      | otherwise = sacarImpares xs a 
                    
--h)
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n xs = multiplosDeNAux n xs []

multiplosDeNAux :: Integer -> [Integer] -> [Integer] -> [Integer]
multiplosDeNAux n [] a = a
multiplosDeNAux n (x:xs) a | (mod x n)==0 = multiplosDeNAux n xs (a++[x])

--i)
ordenar :: [Integer] -> [Integer]
ordenar xs = ordenarAux xs []

ordenarAux :: [Integer] -> [Integer] -> [Integer]
ordenarAux [] a = a
ordenarAux xs a = ordenarAux (quitar (minimum xs) xs) (a++[minimum xs])

--Ejemplo: ordenar [3,1,2] [] -> ordenar [3,2] [1] -> ordenar [3] [1,2] -> ordenar [] [1,2,3] -> [1,2,3] 
--Ejemplo: ordenar [2,1] [] -> ordenar [2] [1] -> ordenar [] [1,2] -> [1,2] 

--Ejercicio4--------------------------------------------------------------------------------------------------------------------

