Dadas las definiciones usuales de foldr y foldl, demostrar las siguientes propiedades

1. `∀f::a->b->b . ∀ z::b . ∀ xs, ys::[a] . foldr f z (xs ++ ys) = foldr f (foldr f z ys) xs`
2. `∀ f::b->a->b . ∀ z::b . ∀ xs, ys::[a] . foldl f z (xs ++ ys) = foldl f (foldl f z xs) ys`

---
## Respuestas

