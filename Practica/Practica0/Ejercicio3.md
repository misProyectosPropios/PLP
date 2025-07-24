Contamos con los tipos Maybe y Either definidos como sigue:

```haskell
data Maybe a = Nothing | Just a
data Either a b = Left a | Right b
```

1. Definir la función `inverso :: Float → Maybe Float` que dado un número devuelve su inverso multiplicativo si está definido, o Nothing en caso contrario.
2. Definir la función `aEntero :: Either Int Bool → Int` que convierte a entero una expresión que puede ser booleana o entera. En el caso de los booleanos, el entero que corresponde es 0 para False y 1 para True.

---
## Respuestas
1. 
```haskell
inverso :: Float -> Maybe Float
inverso 0 = Nothing
inverso x = Maybe (1 / x)
```
2. 
```haskell
aEntero :: Either Int Bool -> Int
aEntero Left x = x
aEntero Right True = 1
aEntero Right False = 1
```