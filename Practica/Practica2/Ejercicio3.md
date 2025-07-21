Considerar las siguientes funciones:

```haskell
     length :: [a] -> Int
{L0} length [] = 0
{L1} length (x:xs) = 1 + length xs

     duplicar :: [a] -> [a]
{D0} duplicar [] = []
{D1} duplicar (x:xs) = x : x : duplicar xs

      (++) :: [a] -> [a] -> [a]
{++0} [] ++ ys = ys
{++1} (x:xs) ++ ys = x : (xs ++ ys)

     append :: [a] -> [a] -> [a]
{A0} append xs ys = foldr (:) ys xs

     ponerAlFinal :: a -> [a] -> [a]
{P0} ponerAlFinal x = foldr (:) (x:[])

	 reverse :: [a] -> [a]
{R0} reverse = foldl (flip (:)) []
```

Demostrar las siguientes propiedades:
i. `∀ xs::[a] . length (duplicar xs) = 2 * length xs`
ii. `∀ xs::[a] . ∀ ys::[a] . length (xs ++ ys) = length xs + length ys`
iii. `∀ xs::[a] . ∀ x::a . append [x] xs = x:xs`
iv. `∀ xs::[a] . ∀ f::(a->b) . length (map f xs) = length xs`
v. `∀ xs::[a] . ∀ p::a->Bool . ∀ e::a . ((elem e (filter p xs)) ⇒ (elem e xs))` (asumiendo `Eq a`)
vi. `∀ xs::[a] . ∀ x::a . ponerAlFinal x xs = xs ++ (x:[])`
vii. `reverse = foldr (\x rec -> rec ++ (x:[])) []`
viii. `∀ xs::[a] . ∀ x::a . head (reverse (ponerAlFinal x xs)) = x`

---
## Respuestas

1. 
```
Teorema: ∀ xs::[a] . length (duplicar xs) = 2 * length xs

El predicado unario para este teorema:
P(xs) = ∀ xs::[a] . length (duplicar xs) = 2 * length xs

Usando inducción estructural sobre listas, demostraremos el caso base ([]) y el paso inductivo (x:xs) suponiendo que se cumple para xs

Caso base:

P([]) = 
         length (duplicar []) = 2 * length []
{D0}     length [] = 2 * length []
{L0}     0 = 2 * length []
{L0}     0 = 2 * 0
{Prop *} 0 = 0

Paso inductivo:

HI = ∀ xs::[a] . length (duplicar xs) = 2 * length xs

∀ x::a, ∀ xs::[a]
P(x:xs) = 
        length (duplicar x:xs) = 2 * (length x:xs)
{D1}    length (x : x : duplicar xs) = 2 * (length x : xs)
{L1}    1 + length (x : duplicar xs) = 2 * (length x : xs)
{L1}    1 + 1 + length (duplicar xs) = 2 * (length x : xs)
{L1}    2 + length (duplicar xs) = 2 * (1 + length xs)
{HI}    2 + 2 * length xs = 2 * (1 + length xs)
{*}     2 + 2 * length xs = 2 + 2 * length xs
```

 2. 
```

Teorema: ∀ xs::[a] . ∀ ys::[a] . length (xs ++ ys) = length xs + length ys

El predicado unario para este teorema:
	P(xs) = ∀ xs::[a] length (xs ++ ys) = length xs + length ys

Usando la inducción estructural sobre listas

Caso base 

P([]) = 
         length ([] ++ ys) = length [] + length ys
{++0}    length ys = length [] + length ys
{L0}     length ys = 0 + length ys
{Prop+}  length ys = length ys

Paso inductivo

HI = ∀ xs::[a] . length (xs ++ ys) = length xs + length ys

∀ x::a, ∀ xs::[a]
P(x:xs) = 
	   length (x:xs ++ ys) = length x:xs + length ys
{++1}  length (x : (xs ++ ys)) = length x:xs + length ys
{L1}   1 + length (xs ++ ys) = length x:xs + length ys
{L1}   1 + length (xs ++ ys) = 1 + length xs + length ys
{HI}   1 + length xs + length ys = 1 + length xs + length ys
```

3. a
```

```
4. 





# Formato
```

Teorema: 

El predicado unario para este teorema:
	P(xs) = 

Usando la inducción estructural sobre listas

Caso base 

P([]) = 
         
Paso inductivo

HI = 

∀ x::a, ∀ xs::[a]
P(x:xs) = 
	   
```