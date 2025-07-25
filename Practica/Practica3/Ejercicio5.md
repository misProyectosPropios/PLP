Demostrar en deducción natural que las siguientes fórmulas son teoremas **sin usar principios de razonamiento clásico**s salvo que se indique lo contrario. Recordemos que una fórmula σ es un teorema si y sólo si vale ⊢ σ

1. `(ρ ⇒ σ ⇒ τ ) ⇒ (ρ ⇒ σ) ⇒ ρ ⇒ τ`
2. `⊢(ρ ⇒ ⊥) ⇒ ¬ρ`
3. `ρ ⇒ ¬¬ρ`

---
## Respuestas
1. 

```mermaid
flowchart TD

    n1@{ label: "<span style=\"padding-left:\">$ (ρ ⇒ σ ⇒ τ )</span><span style=\"padding-left:\"><span style=\"padding-left:\">\\vdash</span></span><span style=\"padding-left:\">(ρ ⇒ σ) ⇒ ρ ⇒ τ$</span>" } --> n2["$$\vdash (ρ ⇒ σ ⇒ τ ) ⇒ (ρ ⇒ σ) ⇒ ρ ⇒ τ$$"]

    n3@{ label: "<span style=\"padding-left:\"><span style=\"padding-left:\">$ (ρ ⇒ σ ⇒ τ )</span><span style=\"padding-left:\">(ρ ⇒ σ)</span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">\\vdash</span></span><span style=\"padding-left:\"></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\">ρ ⇒ τ$</span></span>" } --> n1

    n4@{ label: "<span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">$ (ρ ⇒ σ ⇒ τ )</span><span style=\"padding-left:\">,(ρ ⇒ σ),</span></span><span style=\"padding-left:\"><span style=\"padding-left:\">ρ</span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">\\vdash</span></span></span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">⇒ τ$</span></span></span>" } --> n3

    n5@{ label: "<span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">$ (ρ ⇒ σ ⇒ τ )</span><span style=\"padding-left:\">,(ρ ⇒ σ),</span></span><span style=\"padding-left:\"><span style=\"padding-left:\">ρ</span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">\\vdash</span></span></span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">⇒</span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">ρ ⇒ σ</span></span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">=&gt; τ$</span></span></span></span>" } --> n4

    n6@{ label: "<span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">$ (ρ ⇒ σ ⇒ τ )</span><span style=\"padding-left:\">,(ρ ⇒ σ),</span></span><span style=\"padding-left:\"><span style=\"padding-left:\">ρ</span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">\\vdash</span></span></span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">⇒</span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">ρ ⇒ σ</span></span></span></span></span><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\"><span style=\"padding-left:\">$</span></span></span></span></span>" } --> n4

  

    n1@{ shape: text}

    n3@{ shape: text}

    n4@{ shape: text}

    n5@{ shape: text}

    n6@{ shape: text}
```

2. 
```mermaid
flowchart BT
 x5["(ρ ⇒ ⊥), p ⊢  ⇒  ρ"]
 x4["(ρ ⇒ ⊥), p ⊢  ⇒ ¬ρ"]
 x3["(ρ ⇒ ⊥), p ⊢  ⇒ ⊥"]
 x2["(ρ ⇒ ⊥) ⊢  ⇒ ¬ρ"]
 x1["\vdash (ρ ⇒ ⊥) ⇒ ¬ρ"]
 
 x1 --- x2
 x2 --- x3
 x3 --- x4
 x3 --- x5
```
3. 
```mermaid
flowchart BT
x1["⊢ρ ⇒ ¬¬ρ"]
x2["ρ ⊢ ¬¬ρ"]
x3["ρ, ¬ρ ⊢ ⊥"]
x4["ρ, ¬ρ ⊢ ρ"]
x5["ρ, ¬ρ ⊢ ¬ρ"]

x1 --- x2
x2 --- x3
x3 --- x4
x3 --- x5
```
4. 
```mermaid
flowchart BT
x1["⊢ ¬¬¬ρ ⇒ ¬ρ"]
x2["¬¬¬ρ ⊢ ¬ρ"]
x3["¬¬¬ρ,ρ ⊢ ⊥"]
x4["¬¬¬ρ,ρ ⊢ ¬¬ρ"]
x5["¬¬¬ρ,ρ ⊢ ¬¬¬ρ"]
x6["¬¬¬ρ,ρ ⊢ ρ"]

x1 --- x2
x2 --- x3
x3 --- x4
x3 --- x5
x4 --- x6
```

6. 

```mermaid
flowchart BT
x1[" ⊢ (ρ ⇒ σ) ⇒ (¬σ ⇒ ¬ρ)"]
x2[" (ρ ⇒ σ), ¬σ ⊢  ¬ρ"]
x3[" (ρ ⇒ σ), ¬σ, ρ ⊢ ⊥"]
x4[" (ρ ⇒ σ), ¬σ, ρ ⊢ ρ"]
x5[" (ρ ⇒ σ), ¬σ, ρ ⊢ ¬ρ"]
x6[" (ρ ⇒ σ), ¬σ, ρ ⊢ ρ ⇒ σ"]
x7[" (ρ ⇒ σ), ¬σ, ρ ⊢ ¬σ"]

x1 --- x2
x2 --- x3
x3 --- x4
x3 --- x5
x5 --- x6
x5 --- x7
```

