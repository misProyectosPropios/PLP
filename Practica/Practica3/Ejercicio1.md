Determinar el valor de verdad de las siguientes proposiciones (fórmulas):

1. `(¬P ∨ Q)`
2. `(P ∨ (S ∧ T) ∨ Q)`
3. `¬(Q ∨ S)`
4. `(¬P ∨ S) ⇔ (¬P ∧ ¬S)`
5. `((P ∨ S) ∧ (T ∨ Q))`
6. `(((P ∨ S) ∧ (T ∨ Q)) ⇔ (P ∨ (S ∧ T) ∨ Q))` 
7. `(¬Q ∧ ¬S)`
cuando el valor de verdad de P y Q es V, mientras que el de S y T es F.

---
## Respuestas

1.a
```
(¬P ∨ Q) {p := V, Q := V, S := F, T := F}
(¬V ∨ V)
(F ∨ V) 
V
```
2. a
```
(P ∨ (S ∧ T) ∨ Q) {p := V, Q := V, S := F, T := F}
(V ∨ (F ∧ F) ∨ V)
(V ∨ F ∨ V)
V
```
3. a
```
¬(Q ∨ S) {p := V, Q := V, S := F, T := F}
¬(V ∨ F)
¬V
F
```
4. a
```
((¬P ∨ S) ⇒ (¬P ∧ ¬S)) ∧ ((¬P ∧ ¬S) ⇒ (¬P ∨ S)) {p := V, Q := V, S := F, T := F}
((¬V ∨ F) ⇒ (¬V ∧ ¬F)) ∧ ((¬V ∧ ¬F) ⇒ (¬V ∨ F))
((F ∨ F) ⇒ (F ∧ V)) ∧ ((F ∧ V) ⇒ (F ∨ F))
((F ∨ F) ⇒ F) ∧ ((F ∧ V) ⇒ (F ∨ F))
(F ⇒ F) ∧ (F ⇒ F)
V ∧ V
V
```
5. 
```
((P ∨ S) ∧ (T ∨ Q)) {p := V, Q := V, S := F, T := F}
((V ∨ F) ∧ (F ∨ V))
(V ∧ V)
V
```
6. 
```
TODO (mucho texto)
```
7. 
```
(¬Q ∧ ¬S) {p := V, Q := V, S := F, T := F}
(¬V ∧ ¬F)
(F ∧ V)
F
```