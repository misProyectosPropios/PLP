Sean las siguientes cláusulas (en forma clausal), donde `suma` y `par` son predicados, `suc` es una función y `cero` una constante

1. `{¬suma(X, Y, Z), suma(X, suc(Y), suc(Z))}`
2. `{suma(X, cero, X)}` 
3. `{¬suma(X, X, Y ), par(Y)}`

Demostrar utilizando resolución que suponiendo (1), (2), (3) se puede probar `par(suc(suc(cero)))`. Si es posible, aplicar resolución SLD. 
En caso contrario, utilizar resolución general. Mostrar en cada aplicación de la regla de resolución la sustitución utilizada.

---
## Respuestas

```
Interpretación de las clausulas:
1. suma(X,Y,Z) => suma(X, suc(Y ), suc(Z))
 x + y = z, entonces x + (1 + y) = (1 + z)
2. suma(X, cero, X)
 x + 0 = x
3. suma(X,X,Y) => par(Y)
 x + x = y, entonces y es par
4. par(suc(suc(cero)))
 Que suc(suc(cero)) es un número par

Plan: sé que si un número (Y) es par, entonces es lo mismo que haya un 
número X tal que 2X = Y. Sé que ese número va 1 + 1. Y sé que ese número es 
el sucesor de cero. Y que su suma tiene que generar uno menos el otro
Y, como despues tenemos el valor cero, podremos terminar la demostración

Pasos:

5. (4 y 3) 
   {Y := suc(suc(cero))}
	{¬suma(X, X, suc(suc(cero)))}
6. (5 y 1)
   {Z := suc(cero), Y := suc(cero)}   {¬suma(X, Y, Z), suma(X, suc(Y ), suc(Z))}
    {¬suma(suc(X), suc(X), suc(suc(cero))}
7. (6 y 1)
   {X := suc(X), Y := X, Z := suc(cero)}
    {¬suma(suc(X), X, suc(cero)}
8. (6 y 2)
   {X := cero}
    {}
```