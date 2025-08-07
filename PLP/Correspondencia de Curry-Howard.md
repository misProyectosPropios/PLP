Hay una regla uno a uno entre la deducción natural y el cálculo $\lambda$. 

Esto quiere decir que existen tanto una interpretación tanto lógica como de conjuntos (cálculo $\lambda$). 

Reglas de tipado

![[Pasted image 20250728195152.png]]

Sistemas de tipos para calculo lambda

![[Pasted image 20250728195419.png]]

+ Ignoremos los t´erminos
+ Las reglas de tipado se corresponden con reglas de deducci´on
natural.

### Correspondencia Curry - Howard
Curry y Feys observaron que si se lee el tipo τ → σ como una
implicación τ ⇒ σ:

> la regla de tipado de la aplicación de una función es la regla
> modus ponens


$$Fórmulas ↔ Tipos$$
$$Demostraciones ↔ Términos$$
>Un juicio ⊢ σ es derivable si y sólo si el tipo σ está habitado,
> esto es, existe un término M tal que ⊢ M : τ es derivable

