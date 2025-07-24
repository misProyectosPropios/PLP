Definir las siguientes funciones sobre listas:

1. `limpiar :: String → String → String`, que elimina todas las apariciones de cualquier carácter de la primera cadena en la segunda. Por ejemplo, limpiar ‘‘susto’’ ‘‘puerta’’ evalúa a ‘‘pera’’. Nota: `String` es un renombre de `[Char]`. La notación ‘‘hola’’ es equivalente a `[‘h’,‘o’,‘l’,‘a’]` y a `‘h’:‘o’:‘l’:‘a’:[].`
2. `difPromedio :: [Float] → [Float]` que dada una lista de números devuelve la diferencia de cada uno con el promedio general. Por ejemplo, `difPromedio [2, 3, 4]` evalúa a `[-1, 0, 1]`.
3. `todosIguales :: [Int] → Bool` que indica si una lista de enteros tiene todos sus elementos iguales.

---
## Respuestas
1. 
```haskell
limpiar :: String -> String -> String
limpiar [] lista = lista
limpiar (x:xs) lista = limpiar xs (sacarElemDeList lista x)

sacarElemDeList :: [a] -> a -> [a] 
sacarElemDeList [] _ = []
sacarElemDeList (x:xs]) | x == a = sacarElemDeList xs
                        | otherwise = x : sacarElemDeList xs
```
2. 
```haskell
difPromedio :: [Float] -> [Float]
difPromedio lista = sacarACadaElementoN lista (promedio lista)

sacarACadaElementoN :: (Num a) => [a] -> a -> [a]
sacarACadaElementoN [] _ = []
sacarACadaElementoN (x:xs) val = (x - val) : sacarACadaElementoN xs val

promedio :: (Num a) => [a] -> Float
promedio lista = (sumList lista) / (length lista)

sumList :: (Num a) => [a] -> a
sumList [] = []
sumList (x:xs) = x + sumList xs


```
3. 
```haskell
todosIguales :: [Int] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales [x] = True
todosIguales (x1:x2:xs) | x1 == x2 = todosIguales (x2:xs)
						| otherwisw = False
```