Dados

```
{A0} alt f g [] = [] 
{A1} alt f g (x:xs) = f x : alt g f xs

{.} (.) f g x = f (g x).
```

Demostrar `alt g1 g2 . alt f1 f2 = alt (g1 . f1) (g2 . f2)`

---
## Respuestas

```
Teorema: alt g1 g2 . alt f1 f2 = alt (g1 . f1) (g2 . f2)

Por Principio de extensionalidad funcional, si probamos que 
∀ xs :: [a]. alt g1 g2 . alt f1 f2 xs = alt (g1 . f1) (g2 . f2) xs, entonces alt g1 g2 . alt f1 f2 = alt (g1 . f1) (g2 . f2) va a ser verdadero

Entonces probemos la nueva ecuación.

∀ xs :: [a]. alt g1 g2 . alt f1 f2 xs = alt (g1 . f1) (g2 . f2) xs

El predicado unario es:
P(xs) = ∀ xs :: [a]. alt g1 g2 . alt f1 f2 xs = alt (g1 . f1) (g2 . f2) xs

Usemos inducción estructural sobre listas. 

Caso base:
P([]) = 
       alt g1 g2 . alt f1 f2 [] = alt (g1 . f1) (g2 . f2) []
{(.)}  alt g1 g2 (alt f1 f2 []) = alt (g1 . f1) (g2 . f2) []
{A0}   alt g1 g2 (alt f1 f2 []) = []
{A0}   alt g1 g2 [] = []
{A0}   [] = []

Paso inductivo:

HI = ∀ xs :: [a]. alt g1 g2 . alt f1 f2 xs = alt (g1 . f1) (g2 . f2) xs

∀ x::a, ∀ xs::[a]
P(x:xs) =
        alt g1 g2 . alt f1 f2 (x:xs) = alt (g1 . f1) (g2 . f2) (x:xs)
{(.)}   alt g1 g2 (alt f1 f2 (x:xs)) = alt (g1 . f1) (g2 . f2) (x:xs)
{A1}    alt g1 g2 (f1 x : alt f2 f1 xs) = alt (g1 . f1) (g2 . f2) (x:xs)
{A1}    alt g1 g2 (f1 x : alt f2 f1 xs) = (g1 . f1) x : alt (g2 . f2) (g1 . f1) xs
{(.)}   alt g1 g2 (f1 x : alt f2 f1 xs) = g1 (f1 x) : alt (g2 . f2) (g1 . f1) xs
{A1} g1 (f1 x) : alt g2 g1 (alt f2 f1 xs) = g1 (f1 x) : alt (g2 . f2) (g1 . f1) xs

Por lema de generación de listas, xs o es una [] o es un (y : ys)

Separemos en casos:

Caso: []
     g1 (f1 x) : alt g2 g1 (alt f2 f1 []) = g1 (f1 x) : alt (g2 . f2) (g1 . f1) []
{A0} g1 (f1 x) : [] = g1 (f1 x) : alt (g2 . f2) (g1 . f1) []
{A0} g1 (f1 x) : [] = g1 (f1 x) : []

Caso (y:ys)
       g1 (f1 x) : alt g2 g1 (alt f2 f1 y:ys) = g1 (f1 x) : alt (g2 . f2) (g1 . f1) y:ys
{A1}   g1 (f1 x) : alt g2 g1 (f2 y : alt f1 f2 ys) = g1 (f1 x) : alt (g2 . f2) (g1 . f1) y:ys
{A1}   g1 (f1 x) : g2 (f2 y):alt g1 g2 (alt f1 f2 ys) = g1 (f1 x):alt (g2 . f2) (g1 . f1) y:ys
{(.)}  g1 (f1 x) : g2 (f2 y): alt g1 g2 . alt f1 f2 ys = g1 (f1 x):alt (g2 . f2) (g1 . f1) y:ys
{HI}   g1 (f1 x):g2 (f2 y): alt (g1.f1) (g2.f2) xs = g1 (f1 x):alt (g2 . f2) (g1 . f1) y:ys
{A1}   g1 (f1 x):g2 (f2 y): alt (g1.f1) (g2.f2) xs = g1 (f1 x): (g2 . f2) y : alt (g2 . f2) (g1 . f1) ys
{(.)}  g1 (f1 x):g2 (f2 y): alt (g1.f1) (g2.f2) xs = g1 (f1 x): g2 (f1 y) : alt (g2 . f2) (g1 . f1) ys
```

