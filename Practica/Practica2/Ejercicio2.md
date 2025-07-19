Demostrar las siguientes igualdades utilizando el principio de extensionalidad funcional

1. `flip . flip = id`
2. `∀ f::(a,b)->c . uncurry (curry f) = f`
3. `flip const = const id`
4. `∀ f::a->b . ∀ g::b->c . ∀ h::c->d . ((h . g) . f) = (h . (g . f))`
con la definición usual de la composición: `(.) f g x = f (g x).`
---
## Respuestas

Definiciones:

```
{f}   flip f x y = f y x
{c}   curry f x y = f (x,y)
{u}   uncurry f (x,y) = f x y
{i}   id x = x
{(.)} (.) f g x = f (g x)
```
1. 
```
Teorema: flip . flip = id

∀ f :: a -> b -> c, ∀ x :: a, ∀ y :: b . flip . flip f x y = (id f) x y 
{(.)} ∀ f :: a -> b -> c, ∀ x :: a, ∀ y :: b . flip (flip f x y) = (id f) x y 
{f}   ∀ f :: a -> b -> c, ∀ x :: a, ∀ y :: b . flip f y x = (id f) x y 
{f}   ∀ f :: a -> b -> c, ∀ x :: a, ∀ y :: b . f x y = (id f) x y
{i}    ∀ f :: a -> b -> c, ∀ x :: a, ∀ y :: b . f x y = f x y
```
1. 