Definir las siguientes funciones:
1. `valorAbsoluto :: Float → Float`, que dado un número devuelve su valor absoluto.
2. `bisiesto :: Int → Bool`, que dado un número que representa un año, indica si el mismo es bisiesto.
3. `factorial :: Int → Int`, definida únicamente para enteros positivos, que computa el factorial.
4. `cantDivisoresPrimos :: Int → Int`, que dado un entero positivo devuelve la cantidad de divisores primos

---
## Respuestas
1. 
```haskell
valorAbsoluto :: Float → Float
valorAbsoluto x | x < 0 = (-1) * x
				| otherwise = x	
```
2. 
```haskell
bisiesto :: Int → Bool
```
3. 
```haskell
factorial :: Int → Int
factorial 0 = 1
factorial x = x * factorial (x - 1) 
```
4. 
```haskell
cantDivisoresPrimos :: Int → Int
cantDivisoresPrimos x = cantDivPrimosAux x (x - 1)

cantDivPrimosAux :: Int -> Int -> Int
cantDivPrimosAux _ 1 = 0
cantDivPrimosAux x y | x % y == 0 && esPrimo y = 1 + cantDivPrimosAux x (y -1)
					 | otherwise = cantDivPrimosAux x (y -1)

esPrimo :: Int -> Bool


esPrimoAux :: Int -> Int -> Bool
esPrimoAux _ 1 = True
esPrimoAux x y = 
```