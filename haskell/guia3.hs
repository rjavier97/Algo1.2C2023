-- Guia3: Ejercicio 1--------------------------------------------------------------------------------------------------------------------
-- a)
fx :: Integer -> Integer
fx 1 = 8
fx 4 = 131
fx 16 = 16

-- b)
{-
Especificacion semiformal: 
problema gn (n:Z) : Z {                        |      problema gn (n:Z) : Z {                       
    requiere: { (n=8)∨(n=16)∨(n=131) }         |          requiere: { (n=8)∨(n=16)∨(n=131) }
    asegura: { (res=16 ↔ n es 8) }             |          asegura: { (n=8 → res=16) ∧ (n=16 → res=4) ∧ (n=131 → res=1) }
    asegura: { (res=4 ↔ n es 16) }             |      }
    asegura: { (res=1 ↔ n es 131) }            |         
}  
-}
gx :: Integer -> Integer
gx 8 = 16
gx 16 = 4
gx 131 = 1

-- c)
h :: Integer -> Integer
h n = fx (gx(n))

k :: Integer -> Integer
k n = gx (fx(n))

-- Ejercicio 2--------------------------------------------------------------------------------------------------------------------
-- a)
{-
Especificacion: 
problema absoluto (n:Z) : Z {             |           problema absoluto (n:Z) : Z {                 
    requiere: { True }                    |               requiere: { True } 
    asegura: { res= |n| }                 |               asegura: { (n<0 → res=(-1)*n) ∧ (n≥0 → res=n)  }    
}                                         |           }
-}
absoluto :: Integer -> Integer
absoluto n = abs n

-- b)
{-
Especificacion: 
problema maximoAbsoluto (n:Z, m:Z) : Z {                            
    requiere: { True }                                    
    asegura: { ((absoluto(n) ≥ absoluto(m)) → res=n) ∧ ((absoluto(n) < absoluto(m)) → res=m) }                 
}                                                      
-}
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m | (abs n)>=(abs m) = n
                   | otherwise = m

-- c)
{-
Especificacion: 
problema maximo3 (x:Z, y:Z, z:Z) : Z {                            
    requiere: { True }                                    
    asegura: { ((x≥y)∧(x≥z) → res=x) ∧ ((y≥x)∧(y≥z) → res=y) ∧ ((z≥x)∧(z≥y) → res=z) }                 
}                                                      
-}
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | (x>=y && x>=z) = x
              | (y>=z) = y
              | otherwise = z

-- d)
{-
Especificacion: 
problema algunoEs0 (x:Q, y:Q) : Bool {                            
    requiere: { True }                                    
    asegura: { (res=true) ↔ ((x=0)∨(y=0)) }                 
}                                                      
-}
algunoEs0 :: Float -> Float -> Bool
algunoEs0 n m = (n==0 || m==0)

algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM 0 m = True
algunoEs0PM n 0 = True
algunoEs0PM _ _ = False

-- e)
{-
Especificacion: 
problema ambosSon0 (n:Q, m:Q) : Bool {                            
    requiere: { True }                                    
    asegura: { (res=true) ↔ ((x=0)∧(y=0)) }                 
}                                                      
-}
ambosSon0 :: Float -> Float -> Bool
ambosSon0 n m = (n==0 && m==0)

ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ _ = False

-- f)
{-
Especificacion: 
problema mismoIntervalo (n:R, m:R) : Bool {                            
    requiere: { True }                                    
    asegura: { (res=true) ↔ ( ((x≤3)∧(y≤3)) ∨ ((x>3)∧(y>3)∧(x≤7)∧(y≤7)) ∨ ((x>7)∧(y>7)) ) }                 
}                                                      
-}
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo x y = ((x<=3)&&(y<=3)) || ((x>3)&&(x<=7))&&((y>3)&&(y<=7)) || ((x>7)&&(y>7))

-- g)    
{-
Especificacion: 
problema sumaDistintos (x:Z, y:Z, z:Z) : Z {                            
    requiere: { True }                                    
    asegura: {( ((x≠y)∧(x≠z)∧(y≠z))→res=x+y+z) ∧ ( (((x=y)∧(y≠z))∨((x≠y)∧(y=z)))→res=x+z) ∧ ( ((x≠y)∧(x=z))→res=x+y) ∧ ( ((x=y)∧(y=z))→res=x)}                 
}                                                      
-}
sumaDistintos :: Integer -> Integer -> Integer -> Integer  --- Cuando hay algun numero repetido lo sumo una sola vez
sumaDistintos x y z | (x==y)&&(y==z) = x     -- Caso por ej: 2 2 2 
                    | (x==y)||(y==z) = x+z   -- Caso por ej: 1 2 2 ..ó.. 2 2 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                    | (x==z) = x+y           -- Caso por ej: 2 1 2 
                    | otherwise = x+y+z      -- Caso por ej: 1 2 3                                                                                                                           

-- h)
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y = ((mod x y)==0)

-- i) 
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10


digitoUnidades1 ::  Integer -> Integer
digitoUnidades1 n | n<10 = n
                  | otherwise = digitoUnidades1 (n-10)               

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div (n-(digitoUnidades n)) 10  --- tambien con poner = div n 10 , se elimina(o saca) el ultimo digito
                        
-- j)
digitoDecenas :: Integer -> Integer
digitoDecenas n | n<10 = 0
                | otherwise = digitoUnidades (sacarUltimoDigito n) -- tambien con poner = (mod (div n 10) 10) alcanza
                -- otherwise = mod (div n 10) 10
{- Ejercicio 3--------------------------------------------------------------------------------------------------------------------
a.a + a.b.k = 0  -> a + b.k = 0 (se puede dividir por a, ya que a nunca es cero) ->  bk=-a   ->   k = -a/b
es decir, k es entero si a es divisible por b, y entonces su resto será 0
es decir, mod a b = 0  -}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y = (x/=0)&&(y/=0)&&(mod x y == 0)

-- Ejercicio 4--------------------------------------------------------------------------------------------------------------------
--a)
prodInt :: (Integer, Integer) -> (Integer, Integer) -> Integer 
prodInt (a,b) (c,d) = a*c + b*d

--b)
todoMenor1 :: (Float, Float) -> (Float, Float) -> Bool
todoMenor1 (a,b) (c,d) = (a<=c)&&(b<=d)
                                                                -- Va Float en vez de Integer, ya que son Reales
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor v w = ((fst v)<=(fst w))&&((snd v)<=(snd w))

--c) d = raiz(a**2 + b**2) -> d = raiz( (x1-x2)**2 + (y1-y2)**2 ) , con v=(x1,x2) y w=(y1,y2) 
distanciaPuntos :: (Float, Float) -> (Float,Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt( (a-c)**2 + (b-d)**2 )

--d)
sumaTerna :: (Integer,Integer,Integer) -> Integer
sumaTerna (a,b,c) = a+b+c

--e) 
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | (mod a n ==0)&&(mod b n ==0)&&(mod c n ==0) = a+b+c
                             | (mod a n ==0)&&(mod b n /=0)&&(mod c n /=0) = a
                             | (mod a n ==0)&&(mod b n ==0)&&(mod c n /=0) = a+b
                             | (mod a n ==0)&&(mod b n /=0)&&(mod c n ==0) = a+c
                             | (mod a n /=0)&&(mod b n ==0)&&(mod c n /=0) = b
                             | (mod a n /=0)&&(mod b n ==0)&&(mod c n ==0) = b+c
                             | (mod a n /=0)&&(mod b n /=0)&&(mod c n ==0) = c
                             | otherwise = 0  
{-}
sumarSoloMultiplos1 :: (Integer, Integer, Integer) -> Integer -> Integer   
sumarSoloMultiplos1 (a,b,c) n | (n>=1)&&(mod a n ==0) = a + sumarSoloMultiplos1 (b,a,c)        
-}

--f)
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a,b,c) | (mod a 2 == 0) =1
                     | (mod b 2 == 0) =2
                     | (mod c 2 == 0) =3 
                     | otherwise = 4

--g)
crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)          

--h) 
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a) 

--Ejercicio 5--------------------------------------------------------------------------------------------------------------------
--funciones auxiliares f y g , para resolver problema todosMenores
f :: Integer -> Integer 
f n | n<=7 = n^2 
    | otherwise = 2*n -1 

g :: Integer -> Integer 
g n | (mod n 2 == 0) = div n 2 
    | otherwise = 3*n +1   

todosMenores :: (Integer, Integer, Integer) -> Bool 
todosMenores (n1, n2, n3) = ((f n1)>(g n1)) && ((f n2)>(g n2)) && ((f n3)>(g n3))

--Ejercicio 6--------------------------------------------------------------------------------------------------------------------
-- Programa que me dice si un año es bisiesto o no
bisiesto :: Integer -> Bool
bisiesto n = not ( (mod n 4 /=0) || ((mod n 100 ==0)&&(mod n 400 /= 0)) )   -- version que pedia el ejercicio
{- ( (mod n 100 ==0)&&(mod n 400 /= 0) ) si en vez de esa expresion hubiese sido,
( (mod n 100 ==0)&&(mod n 400 == 0) ), alcanzaba con solo poner (mod n 400 ==0),
ya que (mod n 400 ==0) implica que (mod n 100 == 0), pero no al revés  -}

bisiesto1 :: Integer -> Bool
bisiesto1 n = (mod n 4 ==0) && (mod n 400 /= 0)   -- no funciona

bisiesto2 :: Integer -> Bool
bisiesto2 n = (mod n 4 ==0) && ( (mod n 100 /=0)||(mod n 400 == 0) )   -- otra version (use regla de DeMorgan)

bisiesto3 :: Integer -> Bool
bisiesto3 n = (mod n 400 == 0) || ( (mod n 4 ==0)&&(mod n 100 /=0) ) -- otra version(aca use la aclaracion que hice en bisiesto n)

{- Conclusion: 1) si un año es bisiesto entonces es divisible por 4
               2) si un año es divisible por 400 entonces es bisiesto -}

--Ejercicio 7--------------------------------------------------------------------------------------------------------------------
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (vx, vy, vz) (wx, wy, wz) = abs(vx-wx) + abs(vy-wy) + abs(vz-wz) 

--Ejercicio 8--------------------------------------------------------------------------------------------------------------------
sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos n = (mod n 10) + (mod (div n 10) 10)

comparar :: Integer -> Integer -> Integer 
comparar n m | (sumaUltimosDosDigitos n) < (sumaUltimosDosDigitos m) = 1
             | (sumaUltimosDosDigitos n) > (sumaUltimosDosDigitos m) = -1
             | otherwise = 0 

--Ejercicio9--------------------------------------------------------------------------------------------------------------------
--A partir de las siguientes implementaciones en Haskell,describir en lenguaje natural que hacen y especificarlas semiformalmente
--A tener en cuenta: alt+29= ↔ , alt+26= → , alt+27= ←, alt+142= Ž ,otros simbolos: ℤ , ℝ , ∧ , ∨ , ¬ , ⇔, ∀, ∃, ∃! ,≠ ,≤ , ≥ , ∈
{-
a)
f1 :: Float -> Float 
f1 n | n==0 = 1
     | otherwise = 0

Lenguaje natural: a partir de cualquier numero real, determina si ese numero es 0 o no, si es 0 el programa devuelve 1, y si es cualquier
otro numero devuelve 0. 
Especificacion semiformal:
problema esCero (n:R) : ℝ {                            |        problema esCero (n:R) : ℝ {                       
    requiere: {True}                                   |             requiere: {True}
    asegura: { (res=1 ↔ n es 0) }                      |             asegura: { (n=0 → res=1) ∧ (n≠0 → res=0) }
    asegura: { (res=0 ↔ n no es igual a 0) }           |        }   
}                                                      |
-----------------------------------------------------------------------------------------------------
b)
f2 :: Float -> Float 
f2 n | n == 1 = 15
     | n == -1 = -15

Lenguaje natural: es un programa que me describe una funcion parcial, cuyos valores del Dominio son unicamente 
1 y -1 . Si elijo evaluar f2 en 1, el programa me devuelve 15. Si elijo evaluar f2 en -1, el programa me devuelve -15
Especificacion semiformal: 
problema parcialF2 (n:R) : ℝ {                 |        problema parcialF2 (n:R) : ℝ {                       
    requiere: { (n=1)∨(n=-1) }                 |             requiere: { (n=1)∨(n=-1) }
    asegura: { (res=15 ↔ n es 1) }             |             asegura: { (n=1 → res=15) ∧ (n=-1 → res=-15) }
    asegura: { (res=-15 ↔ n es -1) }           |        }   
}  
-----------------------------------------------------------------------------------------------------
c)
f3 :: Float -> Float
f3 n | n <= 9 = 7
     | n >= 3 = 5

Lenguaje natural: es un programa que me describe que si elijo Reales menores o iguales a 9, obtengo como resultado 7
                 y si elijo Reales mayores o iguales a 3, obtengo como resultado 5
                 es un programa en el que si cambio el orden de las guardas, obtengo un resultado diferente. 
Especificacion semiformal: 
problema parcialF3 (n:R) : ℝ {             |        problema parcialF3 (n:R) : ℝ {                       
    requiere: {True}                       |             requiere: {True}
    asegura: { (res=7 ↔ n≤9) }             |             asegura: { n≤9 → res=7) ∧ (n≥3 → res=5) }
    asegura: { (res=5 ↔ n≥3) }             |        }   
}                   
-----------------------------------------------------------------------------------------------------
d) 
f4 :: Float -> Float -> Float
f4 x y = ( x + y )/2

Lenguaje natural: es un programa que me describe una funcion que toma 2 numeros reales cualesquiera 
                  los suma entre si, y luego lo divide por 2, y me retorna el resultado de esa operacion
Especificacion semiformal: 
problema funcionF4 (a: ℝ, b: ℝ) : ℝ {                              
    requiere: {True}                         
    asegura: { res= (a+b)/2 }                                 
} 
-----------------------------------------------------------------------------------------------------
e)
f5 :: (Float, Float ) -> Float
f5 (x , y ) = ( x + y )/2

Lenguaje natural: programa que me describe una funcion que toma un par de numeros pertenecientes a R^2,
                 luego suma el valor de la coordenada x con el valor de la coordenada y, a ese resultado lo divido por 2
                 el resultado de hacer toda esa operacion, es el valor que me devuelve el programa. 
Especificacion semiformal: 
problema funcionF5 ( (a,b): ℝxℝ ) : ℝ {                              
    requiere: {True}                         
    asegura: { res= (a+b)/2 }                     
}
-----------------------------------------------------------------------------------------------------
f)
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b

Lenguaje natural:  programa que toma 2 valores: uno real y uno entero y los compara. A partir de alli me indica
                   si la parte entera del numero real es igual al numero entero. Si ambas partes enteras 
                   son iguales el programa me devolvera Verdadero, sino me devolvera Falso. 
Especificacion semiformal: 
problema comparaParteEntera (n: ℝ, m: ℤ) : Bool {                              
    requiere: {True}                         
    asegura: { res=True ↔ [n]=[m] }                              
}

-}
