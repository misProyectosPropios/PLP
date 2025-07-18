1. Definir la función `curry`, que dada una función de dos argumentos, devuelve su equivalente currificada
2. Definir la función `uncurry`, que dada una función currificada de dos argumentos, devuelve su versión no currificada equivalente. Es la inversa de la anterior
3. Se podría definir una función `curryN`, que tome una función de un número arbitrario de argumentos y devuelva su versión currificada? Sugerencia: pensar cuál sería el tipo de la función.


---
## Respuestas
1. 
```haskell
curry :: ((a, b) -> c) -> a -> b -> c
curry f a b = f (a, b)
```
2. 
```haskell
uncurry :: (a -> b -> c) -> (a, b) -> c
uncurry f (a, b) = f a b
```
3. No se podría definir una función llamada `curryN`, pues su tipo no se podría definir, ya que al querer implementarlo para un número arbitrario de números sería diferente para cada número de argumentos que se le quiera definir