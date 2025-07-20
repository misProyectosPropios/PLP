Dar una derivación o explicar por qué no es posible dar una derivación para cada uno de los siguientes juicios de tipado:
1. $\vdash \text{if true then zero else succ(zero) : Nat}$`
2. $\text{x : Nat, y : Bool } \vdash \text{ if true then false else (λz : Bool. z) true : Bool}$ 
3. $\vdash \text{ if λx : Bool. x then zero else succ(zero) : Nat}$
4. $\text{ x : Bool → Nat, y : Bool}\vdash \text{x y : Nat}$

---
## Respuestas

1. Funciona 
   #TODO hacer derivación
2. Va a funcionar bien, aunque el x y el y no influyen en el contexto
   #TODO hacer derivación
3. Va a fallar, pues la condición del if no es un bool
4. Va a fallar, pues es una aplicación y x no lo es