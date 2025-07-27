Demostrar las siguientes propiedades utilizando inducción estructural sobre listas, lemas de generación y el principio de extensionalidad funcional.

1. `reverse . reverse = id`
2. `append = (++)`
3. `map id = id`
4. `∀ f::a->b . ∀ g::b->c . map (g . f) = map g . map f`
5. `∀ f::a->b . ∀ p::b->Bool . map f . filter (p . f) = filter p . map f`
6. `∀ f::a->b . ∀ e::a . ∀ xs::[a] . ((elem e xs) ⇒ (elem (f e) (map f xs)))`

---
## Respuestas
Definiciones útiles
```haskell
     reverse :: [a] -> [a]
{R0} reverse [] = []
{R1} reverse (x:xs) = (reverse xs) ++ [x]

{(.)} (.) f g x = f (g x)

{I0} id x = x

      (++) :: [a] -> [a] -> [a]
{++0} [] ++ ys = ys
{++1} (x:xs) ++ ys = x : (xs ++ ys)

     append :: [a] -> [a] -> [a]
{A0} append xs ys = foldr (:) ys xs

      foldr :: (a -> b -> b) -> b -> [a] -> b 
{FR0} foldr f z [] = z 
{FR1} foldr f z (x:xs) = f x (foldr f z xs)
```

1. 
```
Teorema: `reverse . reverse = id`

Por principio de extensionalidad funcional, 

(∀xs :: [a]. reverse . reverse xs = id xs => reverse . reverse = id

El predicado unario para este teorema:

∀xs :: [a] P(xs) = reverse . reverse xs = id xs	 

Usando la inducción estructural sobre listas

Caso base 

P([]) = 
       reverse . reverse [] = id []
{(.)}  reverse (reverse []) = id []
{R0}   reverse [] = id []
{R0}   [] = id []
{I0}   [] = []

Paso inductivo

Qvq P(xs) => P(x:xs)

HI ∀xs : [a] P(xs) = reverse . reverse xs = id xs

∀ x::a, ∀ xs::[a]
P(x:xs) = 
         reverse . reverse (x:xs) = id x:xs
{I}	     reverse . reverse (x:xs) = x:xs
{(.)}    reverse (reverse (x:xs)) = x:xs
{(.)}    reverse (reverse xs ++ [x]) = x:xs
{(.)}    reverse (reverse xs ++ [x]) = x:xs
{L1}     reverse [x] ++ reverse (reverse xs) =  x:xs
{R1}     reverse [] ++[x] ++ reverse (reverse xs) =  x:xs
{R0}     [] ++ [x] ++ reverse (reverse xs) =  x:xs
{++0}    [x] ++ reverse (reverse xs) =  x:xs
{++1}    x : ([] ++ reverse (reverse xs)) =  x:xs
{++0}    x : (reverse (reverse xs)) =  x:xs
{(.)}    x : (reverse . reverse xs) =  x:xs
{HI}    x : (id xs) =  x:xs
{I}    x : xs =  x:xs

Lema L1: reverse (xs ++ ys) = reverse ys ++ reverse xs

TODO: demostrarlo
```

2. 

```

Teorema: append = (++)

Por el principio de extensionalidad funcional
∀xs :: [a], ∀ys :: [a] append xs ys = (++) xs ys 
=> append = (++)


El predicado unario para este teorema:
∀xs :: [a]	P(xs) = ∀ys :: [a] append xs ys = (++) xs ys 

Usando la inducción estructural sobre listas

Caso base 

P([]) = 
∀ys :: [a] append [] ys = (++) [] ys 

Los ∀ys :: [a] estarán, pero los evito de escribir por cuestiones prácticas
{A0}  foldr (:) ys [] = (++) [] ys 
{++0} foldr (:) ys [] = ys
{FR0} ys = ys

Paso inductivo

HI = ∀ys :: [a] append xs ys = (++) xs ys 

∀ x::a, ∀ xs::[a] ∀ys :: [a]
P(x:xs) = 
	   append x:xs ys = (++) x:xs ys
{A0}   foldr (:) ys x:xs = (++) x:xs ys 
{++0}  foldr (:) ys x:xs = x : ((++) xs ys)
{FR1}  x : (foldr (:) ys xs) = x : ((++) xs ys)
{HI}   x : (foldr (:) ys xs) = x : append xs ys
{A0}   x : (foldr (:) ys xs) = x : (foldr (:) ys xs)
```

