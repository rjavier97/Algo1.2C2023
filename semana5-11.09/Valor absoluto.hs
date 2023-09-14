import Test.HUnit

-- La funcion que queremos probar
valorAbsoluto :: Int -> Int
valorAbsoluto x | x >= 0 = x
                | otherwise = -x


-- Las pruebas unitarias
testSuiteValorAbs = test [
    "casoPositivo" ~: 1 ~?= (valorAbsoluto 1),
    "casoNegativo" ~: 5 ~?= (valorAbsoluto (-5)),
    "casoCero" ~: 0 ~?= (valorAbsoluto 0)
    ]

-- Corre todas las pruebas
correrTests = runTestTT testSuiteValorAbs