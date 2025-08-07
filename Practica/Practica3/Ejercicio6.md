Demostrar en deducción natural que vale `⊢ σ` para cada una de las siguientes fórmulas. Para estas fórmulas es imprescindible usar **lógica clásica**:

1. Absurdo clásico: `(¬τ ⇒ ⊥) ⇒ τ`
2. Ley de Peirce: `((τ ⇒ ρ) ⇒ τ ) ⇒ τ`
3. Tercero excluido: `τ ∨ ¬τ`
4. Consecuencia milagrosa: `(¬τ ⇒ τ ) ⇒ τ`
5. Contraposición clásica: `(¬ρ ⇒ ¬τ ) ⇒ (τ ⇒ ρ)`
6. Análisis de casos: `(τ ⇒ ρ) ⇒ (¬τ ⇒ ρ) ⇒ ρ`
7. Implicación vs. disyunción: `(τ ⇒ ρ) ⇔ (¬τ ∨ ρ)`

---
## Respuestas
1.  Absurdo clásico: `(¬τ ⇒ ⊥) ⇒ τ
```mermaid
flowchart BT
x1["⊢(¬τ ⇒ ⊥) ⇒ τ"]
x2["¬τ ⇒ ⊥ ⊢ τ"]
x3["¬τ ⇒ ⊥, ¬τ ⊢ ⊥"]
x4["¬τ ⇒ ⊥, ¬τ ⊢ ¬τ ⇒ ⊥"]
x5["¬τ ⇒ ⊥, ¬τ ⊢ ¬τ"]

x1 --- x2
x2 --- x3
x3 --- x4
x3 --- x5
```
2. Tercero excluido: `τ ∨ ¬τ`
```mermaid
flowchart BT
x1["⊢τ ∨ ¬τ"]
```
3. Consecuencia milagrosa: `(¬τ ⇒ τ ) ⇒ τ`
```mermaid
flowchart BT
x1["⊢"]
```
4. Contraposición clásica: `(¬ρ ⇒ ¬τ ) ⇒ (τ ⇒ ρ)`
```mermaid
flowchart BT
x1["⊢"]
```
5. Análisis de casos: `(τ ⇒ ρ) ⇒ (¬τ ⇒ ρ) ⇒ ρ`
```mermaid
flowchart BT
x1["⊢"]
```
6. Implicación vs. disyunción: `(τ ⇒ ρ) ⇔ (¬τ ∨ ρ)
```mermaid
flowchart BT
x1["⊢"]
```
