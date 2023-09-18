module TestDeMisFunciones where 
    import Test.HUnit
    import MisFunciones

-- Casos de test 

run = runTestTT tests 

tests = test [ 
    " Caso base 1: fib 0" ~: (fib 0) ~?= 0, 
    " Caso base 2: fib 1" ~: (fib 1) ~?= 1,
    " Caso recursivo 1: fib 2" ~: (fib 2) ~?= 1 
]