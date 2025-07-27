Mostrar que cualquier fórmula de la lógica proposicional que utilice los conectivos ¬ (negación), ∧ (conjunción), ∨ (disyunción), ⇒ (implicación) puede reescribirse a otra fórmula equivalente que usa sólo los conectivos ¬ y ∨. Sugerencia: hacer inducción en la estructura de la fórmula.

---
## Respuesta

>Propiedad (P) =  cualquier fórmula de la lógica proposicional que utilice los conectivos ¬ (negación), ∧ (conjunción), ∨ (disyunción), ⇒ (implicación) puede reescribirse a otra fórmula equivalente que usa sólo los conectivos ¬ y ∨

Hagamos inducción sobre la estructura de la fórmula

La estructura de las fórmulas es: 

```haskell
τ, σ, ρ, . . . ::= P | (τ ∧ σ) | (τ ⇒ σ) | (τ ∨ σ) | ⊥ | ¬τ
```


### Casos base
Los casos bases de la inducción:
+ `P`
+ `⊥`
Queremos mostrar que la fórmula solo utilize conectivos  ¬ y ∨. 
Estos casos bases trivialmente cumplen P
### Casos inductivos

Los casos inductivos:
1. `(τ ∨ σ)`
2. `¬τ`
3. `(τ ∧ σ)` 
4. `(τ ⇒ σ)

Asumimos que tanto `τ` como `σ` cumplen P 
1. Lo cumple, pues tanto `τ` como `σ` cumple P y al unirlos con un `∨`, se sigue cumpliendo P
2. Lo cumple, pues `τ` cumple P y al agregarle un `¬`, se sigue cumpliendo P
3. Queremos ver si podemos reescribir `(τ ∧ σ)` en otra fórmula  equivalente, pero solo usando `τ`, `σ`, `¬` y `∨`
   Propongo `(τ ∧ σ) ≡ ¬(¬τ∨¬σ)`

|  σ  |  τ  | (τ ∧ σ) | ¬(¬τ∨¬σ) |
| :-: | :-: | :-----: | :------: |
|  F  |  F  |    F    |    F     |
|  F  |  V  |    F    |    F     |
|  V  |  F  |    F    |    F     |
|  V  |  V  |    V    |    V     |
4. Queremos ver si podemos reescribir `(τ ⇒ σ)` en otra fórmula  equivalente, pero solo usando solamente `τ`, `σ`, `¬` y `∨`
   Propongo `(τ ⇒ σ) ≡ (¬τ ∨ σ)

|  σ  |  τ  | (τ ⇒ σ) | (¬τ ∨ σ) |
| :-: | :-: | :-----: | :------: |
|  F  |  F  |    V    |    V     |
|  F  |  V  |    V    |    V     |
|  V  |  F  |    F    |    F     |
|  V  |  V  |    V    |    V     |
Como vimos para todos los casos que podemos reescribir a cada formula para que cumpla P, podemos concluir que todas las fórmulas lógicas son equivalentes a una fórmula que tenga solamente como conectores a la `¬` y `∨`.