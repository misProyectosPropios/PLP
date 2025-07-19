Considerar las siguientes funciones:
1. 
```haskell
elementosEnPosicionesPares :: [a] -> [a]
elementosEnPosicionesPares [] = []
elementosEnPosicionesPares (x:xs) = if null xs
									then [x]
									else x : elementosEnPosicionesPares (tail xs)
```
2. 
```haskell
entrelazar :: [a] -> [a] -> [a]
entrelazar [] = id
entrelazar (x:xs) = \ys -> if null ys
							then x : entrelazar xs []
							else x : head ys : entrelazar xs (tail ys)
```

Indicar si la recursión utilizada en cada una de ellas es o no estructural. Si lo es, reescribirla utilizando `foldr`.
En caso contrario, explicar el motivo.


---
## Respuestas

1. No es estructural su recursión, pues utiliza la función `null xs`, que rompe la recursión estructural.
2. Si, es recursión estructural

```haskell
entrelazar = foldr (\x acc y -> if null y                                                                  then x : acc []
                                else x : head y : acc (tail y)) (const [])
```