Sean τ , σ, ρ y ζ proposiciones tales que τ ⇒ σ es tautología y ρ ⇒ ζ es contradicción. Determinar si las siguientes proposiciones son tautologías, contradicciones o contingencias y demostrarlo:
1. `(τ ⇒ σ) ∨ (ρ ⇒ ζ)`
2. `(τ ⇒ ρ) ∨ (σ ⇒ ζ)`
3. `(ρ ⇒ σ) ∨ (ζ ⇒ σ)`

---
## Respuestas

Suponiendo que 
+ `τ ⇒ σ` es tautología
+ `ρ ⇒ ζ` es contradicción
1. **Tautología**
Demostración:
```
(τ ⇒ σ) ∨ (ρ ⇒ ζ)

Como τ ⇒ σ es tautología, siempre es V. Podemos decir basicamente que es V siempre
Con esto nos basta para ver que es V

V ∨ (ρ ⇒ ζ)
V
```
2. **Contingencia**
Demostración
```
(τ ⇒ ρ) ∨ (σ ⇒ ζ)


Como ρ ⇒ ζ, sabemos que
+ ρ es V y ζ, F

(τ ⇒ V) ∨ (σ ⇒ F)
τ ∨ σ

Como τ ⇒ σ, sabemos que:
+ τ es F y σ, F
+ τ es F y σ, V
+ τ es V y σ, V

Como τ, σ pueden ser F, siendo la fórmula que queda F y sabiendo además que
puede generarse V (en caso de que τ o σ sea V).
```
3. **Tautología**
Demostración
```
(ρ ⇒ σ) ∨ (ζ ⇒ σ)

Como ρ ⇒ ζ, sabemos que
+ ρ es V y ζ, F

σ ∨ (F ⇒ σ)
σ ∨ V
V
```
