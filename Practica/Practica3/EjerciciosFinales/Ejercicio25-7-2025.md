Se define un nuevo conectivo binario $\oplus$ con las siguientes reglas de introducción y eliminación

	$$\frac{\Gamma, \neg \tau, \neg\sigma \vdash \bot} 
	{\Gamma\vdash\tau\oplus\sigma}\oplus i$$
$$\frac{\Gamma \vdash \tau\oplus\sigma \qquad 
\Gamma,\tau\vdash \bot  \qquad
\Gamma, \sigma \vdash\bot
}
       {\Gamma \vdash \bot} \oplus e$$
   Dar las derivaciones para los siguientes secuentes
   1. $\tau \lor \sigma \vdash \tau\oplus\sigma$ 
   2. $\tau\oplus\sigma\vdash\tau\lor\sigma$ 

---
## Respuestas
1. 
```mermaid

flowchart BT

x1["τ ∨ σ ⊢ τ ⊕ σ"] 
x2["τ ∨ σ, ¬τ, ¬σ ⊢ ⊥"]
x3["τ ∨ σ, ¬τ, ¬σ ⊢ τ ∨ σ"]
x4["τ ∨ σ, ¬τ, ¬σ, τ ⊢ ⊥"]
x5["τ ∨ σ, ¬τ, ¬σ, σ ⊢ ⊥"]
x6["τ ∨ σ, ¬τ, ¬σ, τ ⊢ τ"]
x7["τ ∨ σ, ¬τ, ¬σ, τ ⊢ ¬τ"]
x8["τ ∨ σ, ¬τ, ¬σ, σ ⊢ σ"]
x9["τ ∨ σ, ¬τ, ¬σ, σ ⊢ ¬σ"]

x1 --- x2

x2 --- x3
x2 --- x4
x2 --- x5

x4 --- x6
x4 --- x7

x5 --- x8
x5 --- x9
```

2. 
```mermaid

flowchart BT

x1["τ ⊕ σ ⊢ τ ∨ σ"] 
x2["τ ⊕ σ ⊢ τ ∨ ¬τ"]
x3["τ ⊕ σ,τ ⊢ τ ∨ σ"]
x4["τ ⊕ σ,¬τ ⊢ τ ∨ σ"]
x5["τ ⊕ σ,τ ⊢ τ"]
x6["τ ⊕ σ,¬τ ⊢ σ ∨ ¬σ"]
x7["τ ⊕ σ,¬τ, σ ⊢ τ ∨ σ"]
x8["τ ⊕ σ,¬τ, ¬σ ⊢ τ ∨ σ"]
x9["τ ⊕ σ,¬τ, σ ⊢ σ"]
x10["τ ⊕ σ,¬τ, ¬σ ⊢ ⊥"]
x11["τ ⊕ σ,¬τ, ¬σ ⊢ τ ⊕ σ"]
x12["τ ⊕ σ,¬τ, ¬σ, τ ⊢ ⊥"]
x13["τ ⊕ σ,¬τ, ¬σ, σ ⊢ ⊥"]

x14["τ ⊕ σ,¬τ, ¬σ, τ ⊢ τ"]
x15["τ ⊕ σ,¬τ, ¬σ, τ ⊢ ¬τ"]
x16["τ ⊕ σ,¬τ, ¬σ, σ ⊢ σ"]
x17["τ ⊕ σ,¬τ, ¬σ, σ ⊢ ¬σ"]

x1  --- x2
x1  --- x3
x1  --- x4

x3  --- x5

x4  --- x6
x4  --- x7
x4  --- x8

x7  --- x9

x8  --- x10
x10 --- x11
x10 --- x12
x10 --- x13

x12 --- x14
x12 --- x15

x13 --- x16
x13 --- x17
```
