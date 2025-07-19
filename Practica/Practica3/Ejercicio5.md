Demostrar en deducción natural que las siguientes fórmulas son teoremas **sin usar principios de razonamiento clásico**s salvo que se indique lo contrario. Recordemos que una fórmula σ es un teorema si y sólo si vale ⊢ σ

1. (ρ ⇒ σ ⇒ τ ) ⇒ (ρ ⇒ σ) ⇒ ρ ⇒ τ

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

3. 

4. 
