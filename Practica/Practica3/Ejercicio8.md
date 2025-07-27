Si $[τ_1, \dots , τ_n]$ es una lista de fórmulas, definimos la notación $[τ_1, \dots , τ_n ⇒^* σ]$ inductivamente

$$ ([]) ⇒^* σ = σ $$
$$([τ_1, τ_2, \dots , τ_n] ⇒^* σ) = τ_1 ⇒ ([τ_2, \dots , τ_n] ⇒^* σ)$$

Probar por inducción en n que $τ_1, \dots , τ_n ⊢ σ$ es válido si y sólo si $⊢ [τ_1, \dots , τ_n] ⇒^* σ$ es válido.

---
## Respuestas
$\Rightarrow)$ 