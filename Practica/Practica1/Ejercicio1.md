Considerar las siguientes definiciones de funciones:


1. 
```haskell
max2 (x, y) | x >= y = x
		  | otherwise = y
```
2. 
```haskell
normaVectorial (x, y) = sqrt (x^2 + y^2)
```
3. 
```haskell
subtract = flip (-)
```
4. 
```haskell
predecesor = subtract 1
```
5. 
```haskell
evaluarEnCero = \f -> f 0
```
6. 
```haskell
dosVeces = \f -> f . f
```
7. 
```haskell
flipAll = map flip
```
8. 
```haskell
flipRaro = flip flip
```

1. ¿Cuál es el tipo de cada función? (Suponer que todos los números son de tipo Float)?
2. Indicar cuáles de las funciones anteriores no están currificadas. Para cada una de ellas, definir la función currificada correspondiente. Recordar dar el tipo de la función.

---
## Respuestas 

1. El tipo de esta función es: `(float, float) -> float`. 
   No está currificada. 
   La versión currificada sería:
   `float -> float -> float`
2. El tipo de esta función es `(float, float) -> float`
   No está currificada
   La versión currificada sería:
   `float -> float -> float
3. Sabemos los tipos de:
	1. `flip :: (a -> b -> c) -> b -> a -> c`
	   `(-) :: float -> float -> float` (asumimos float)
	   En substract, aplicamos al "primer parámetro", pues 
	   `(a -> b -> c) -> (b -> (a -> c)) = (a -> b -> c) -> b -> a -> c`
	   
	   Entonces, al aplicarle el `(-)` queda: `float -> float -> float`
	   
	   Ya está currificada la función
4. La función `subtract :: float -> float -> float`
   Al hacerle la aplicación, queda: `float -> float`
   Ya está currificada
5. Es una lambda, que es del tipo `float -> a`
   Entonces, la función va a tener el tipo `(float -> a) -> a`
   Está currificada
6. Su tipo es: `(float -> float) -> float -> float`
   Está currificada
7. Hagamos todo el desarrollo:
```
flipAll = map flip

Tipos que sabemos
map  :: (a -> b) -> [a] -> [b]
flip :: (a -> b -> c) -> b -> a -> c

map flip
(a -> b) -> [a] -> [b] 
(a -> b -> c) -> b -> a -> c
Sabemos que:
  (a -> b -> c) -> b -> a -> c = (a -> b -> c) -> (b -> (a -> c))
Por lo tanto, al recibir (a -> b),
  a = (a -> b -> c)
  b = (b -> (a -> c))

Entonces, la función quedaría:
 [a -> b -> c] -> [b -> a -> c] 
```
8. Hagamos el desarrollo
```
flip flip

Tipos que sabemos
(a -> b -> c) -> b -> a -> c

Sabemos además que:

(a -> b -> c) -> b -> a -> c = (a -> b -> c) -> b -> (a -> c)

Con esta información podemos resolverlo:

flip recibe una  función, en este caso flip, y tenemos que asignarlo de 
alguna forma que quede bien de alguna forma

(a -> b -> c) con la función(a -> b -> c) -> b -> (a -> c)
a = (a -> b -> c)
b = b
c = a -> c

b -> (a -> b -> c) -> a -> c
```