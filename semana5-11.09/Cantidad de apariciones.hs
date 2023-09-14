import Test.HUnit

-- La funcion que queremos probar
cantidadDeApariciones :: [Int] -> Int -> Int
cantidadDeApariciones [] _ = 0
cantidadDeApariciones (x:xs) e 
 | x == e = 1 + pasoRecursivo 
 | otherwise = pasoRecursivo
 where pasoRecursivo = cantidadDeApariciones xs e

-- Las pruebas unitarias
testSuiteCantidadApariciones = test [
    "eNoPertenece" ~: 0 ~?= (cantidadDeApariciones [1,2,3] 4),
    "ePertenece" ~: 3 ~?= (cantidadDeApariciones [1,2,(-2),4,(-2),1,(-2)] (-2))
    ]

-- Correr todas las pruebas
correrTests = runTestTT testSuiteCantidadApariciones