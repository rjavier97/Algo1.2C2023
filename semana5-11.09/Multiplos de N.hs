module MultiplosDeN where

-- La funcion que queremos probar
multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)  
 | n == 0 && x == 0 = [0] 
 | n /= 0 && mod x n == 0 = x : pasoRecursivo 
 | otherwise = pasoRecursivo
 where pasoRecursivo = multiplosDeN n xs