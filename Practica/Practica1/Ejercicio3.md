1. Redefinir usando `foldr` las funciones `sum`, `elem`, `(++)`, `filter` y `map`
2. Definir la función `mejorSegún :: (a -> a -> Bool) -> [a] -> a`, que devuelve el máximo elemento de la lista según una función de comparación, utilizando `foldr1`. Por ejemplo, `maximum = mejorSegún (>)`.
3. Definir la función `sumasParciales :: Num a => [a] -> [a]`, que dada una lista de números devuelve otra de la misma longitud, que tiene en cada posición la suma parcial de los elementos de la lista original desde la cabeza hasta la posición actual. Por ejemplo, `sumasParciales [1,4,-1,0,5] ; [1,5,4,4,9]`
4. Definir la función `sumaAlt`, que realiza la suma alternada de los elementos de una lista. Es decir, da como resultado: el primer elemento, menos el segundo, más el tercero, menos el cuarto, etc. Usar `foldr`
5. Hacer lo mismo que en el punto anterior, pero en sentido inverso (el último elemento menos el anteúltimo, etc.). Pensar qué esquema de recursión conviene usar en este caso

---
## Respuestas

1. 
```haskell
{- Versión sin foldr-}
sum [] = 0
sum [x:xs] = x + sum xs

{- Versión usando foldr-}
sum = foldr (+) 0
```

```haskell
{- Versión sin foldr-}
elem :: Eq a => [a] -> Bool
elem [] _ = False
	elem [x:xs] y | x == y = True
			  | otherwise = elem xs y

{- Versión usando foldr-}
elem :: Eq a => [a] -> Bool
elem lista elemento = foldr (\x acc -> acc || x == elemento ) False lista
```

```haskell
{- Versión sin foldr-}
(++) :: [a] -> [a] -> [a]
[] ++ y = y
(x:xs) ++ y = x : ((++) xs y)

{- Versión usando foldr-}
(++) x y = foldr (\x acc -> x : acc) y x
```

```haskell
{- Versión sin foldr-}
filter :: (a -> Bool) -> [a] -> [a]
filter p [] = []
filter p (x : xs) = if p x
					then x : filter p xs
					else filter p xs

{- Versión usando foldr-}
filter :: (a -> Bool) -> [a] -> [a]
filter p = foldr (\x acc -> if p x 
							then x : acc 
							else acc) []
```

```haskell
{- Versión sin foldr-}
map :: (a -> b) -> [a] -> [b]
map f [] = []
map f (x : xs) = f x : map f xs

{- Versión usando foldr-}
map f = foldr (\x acc -> f x : acc) []
```



2. 
```haskell
mejorSegún :: (a -> a -> Bool) -> [a] -> a
```