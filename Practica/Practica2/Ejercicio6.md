Dadas las siguientes funciones:

```haskell
     nub :: Eq a => [a] -> [a]
{N0} nub [] = []
{N1} nub (x:xs) = x : filter (\y -> x /= y) (nub xs)

     union :: Eq a => [a] -> [a] -> [a]
{U0} union xs ys = nub (xs++ys)

     intersect :: Eq a => [a] -> [a] -> [a]
{I0} intersect xs ys = filter (\e -> elem e ys) xs
```

Indicar si las siguientes propiedades son verdaderas o falsas. Si son verdaderas, realizar una demostración. Si son falsas, presentar un contraejemplo.

1. `Eq a => ∀ xs::[a] . ∀ e::a . ∀ p::a -> Bool . elem e xs && p e = elem e (filter p xs)`
2. `Eq a => ∀ xs::[a] . ∀ e::a . elem e xs = elem e (nub xs)`
3. `Eq a => ∀ xs::[a] . ∀ ys::[a] . ∀ e::a . elem e (union xs ys) = (elem e xs) || (elem e ys)`
4. `Eq a => ∀ xs::[a] . ∀ ys::[a] . ∀ e::a . elem e (intersect xs ys) = (elem e xs) && (elem e ys)`
5. `Eq a => ∀ xs::[a] . ∀ ys::[a] . length (union xs ys) = length xs + length ys`
6. `Eq a => ∀ xs::[a] . ∀ ys::[a] . length (union xs ys) ≤ length xs + length ys`

---
## Respuestas