-- Ejercicio1)

--a)
--longitud :: [t] -> Integer
--longitud (x:xs) | (x:xs)==[] = 0     -- no funciona ya que (x:xs) nunca va a ser vacio 
               -- | otherwise = 1 + longitud(tail (x:xs))     
--a)
longitud :: (Eq t) => [t] -> Integer
longitud a | a==[] = 0            
           | otherwise = 1 + longitud(tail (a))  

longitud1 :: [t] -> Integer
longitud1 [] = 0
longitud1 (x:xs) = 1 + longitud1 xs          

longitud2 :: [t] -> Integer
longitud2 lista | null lista = 0
                | otherwise = 1 + longitud2 (tail(lista))

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
                 | otherwise = [x]++principio(xs)

principio1 :: (Eq t) => [t] -> [t]                       
principio1 (x:xs) | (longitud (x:xs) == 1) = []       -- programa que devuelve una lista sin el ultimo elemento, sin usar concat
                 | otherwise = x:principio1(xs)                 

--d)       Se puede usar la funcion "reverse", que viene predefinida  
reverso :: (Eq t) => [t] -> [t]                       -- programa que me devuelve una lista invertida
reverso (x:xs) | (longitud(x:xs) ==1) = [x]
               | otherwise = [ultimo1(x:xs)]++reverso(principio(x:xs))

reverso1 :: (Eq t) => [t] -> [t]                       -- programa que me devuelve una lista invertida, sin usar concat
reverso1 (x:xs) | (longitud(x:xs) ==1) = [x]
                | otherwise = (ultimo1(x:xs)):reverso(principio(x:xs))   

--Ejercicio2---------------------
--a)
pertenece :: (Eq t) => t -> [t] -> Bool        
pertenece _ [] = False
pertenece e (x:xs) = (e==x) || pertenece e xs        

--f)
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos x [y] | x==y = []
quitarTodos x (y:ys) = ys++quitarTodos x (tail ys)


