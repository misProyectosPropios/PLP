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
	   En substract, aplicamos al "primer parametro", pues 
	   `(a -> b -> c) -> (b -> (a -> c)) = (a -> b -> c) -> b -> a -> c`
	   
	   Entonces, al aplicarle el `(-)` queda: `float -> float -> float`


subtract = flip (-)

flip: (a -> b -> c) -> b -> a -> c
				f                 x           y

(-)
float -> float -> float
substrace :: float -> float -> float (lo que faltaría por aplicar)