En este ejercicio usaremos el método de resolución para demostrar una propiedad de las relaciones binarias; a saber, que una relación no vacía no puede ser a la vez irreflexiva, simétrica y transitiva.

Para esto se demostrará la propiedad deseada para una relación arbitraria $R$.

Dadas las siguientes definiciones:

1. $R$ es irreflexiva: `∀X.¬R(X, X)`
2. $R$ es simétrica: `∀X.∀Y.(R(X, Y ) ⇒ R(Y, X))`
3. $R$ es transitiva: `∀X.∀Y.∀Z.((R(X, Y ) ∧ R(Y, Z)) ⇒ R(X, Z))`
4. $R$ es vacía: `∀X.¬∃Y.R(X, Y )`

Utilizando resolución, demostrar que si $R$ cumple las propiedades 1 a 3, entonces es vacía. Indicar si el método de resolución utilizado es o no SLD (Y justificar).

---
### Respuestas
Primero, qué quiero demostrar?
Demostrar que si $R$ cumple las propiedades 1 a 3, entonces es vacía

$$∀X.¬∃Y.R(X,Y)$$

Negado:
$$¬∀X.¬∃Y.R(X,Y)$$

Pasando la negación "hacia dentro"
$$∃X.∃Y.R(X,Y)$$

Skolemización (preserva satisfactibilidad, pero no validez):

$$R(a,b)$$

Ahora, necesito las otras clausulas:

1. `∀X.¬R(X, X)
	1. Forma clausal: `{¬R(X, X)}`
2. `∀X.∀Y.(R(X, Y) ⇒ R(Y, X))`
	1. `∀X.∀Y. (¬R(X, Y) ∨  R(Y, X))`
	2. `{¬(R(X, Y), R(Y, X)}`
3. `∀X.∀Y.∀Z.((R(X, Y) ∧ R(Y, Z)) ⇒ R(X, Z))`
	1. `∀X.∀Y.∀Z.(¬(R(X, Y) ∧ R(Y, Z)) ∨ R(X, Z))`
	2. `∀X.∀Y.∀Z.(¬R(X, Y) ∨ ¬R(Y, Z) ∨ R(X, Z))`
	3. `{¬R(X, Y), ¬R(Y, Z), R(X, Z)}`

```
Recopilando todas las clausulas:
1. {¬R(X, X)}                     Irreflexiva   
2. {¬(R(X, Y), R(Y, X)}           Simetrica
3. {¬R(X, Y), ¬R(Y, Z), R(X, Z)}  Transitiva
4. {R(a,b)}                       Vacia

Plan:

Parto de que es irreflexiva. Si es irreflexiva, no hay ninguna relación 
consigo mismo,
```