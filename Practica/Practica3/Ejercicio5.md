Demostrar en deducción natural que las siguientes fórmulas son teoremas **sin usar principios de razonamiento clásico**s salvo que se indique lo contrario. Recordemos que una fórmula σ es un teorema si y sólo si vale ⊢ σ

1. *Modus ponens* relativizado:`(ρ ⇒ σ ⇒ τ ) ⇒ (ρ ⇒ σ) ⇒ ρ ⇒ τ`
2. Reducción al absurdo: `⊢(ρ ⇒ ⊥) ⇒ ¬ρ`
3. Introducción de la doble negación: `ρ ⇒ ¬¬ρ`
4. Eliminación de la triple negación: `¬¬¬ρ ⇒ ¬ρ`
5. Contraposición: `(ρ ⇒ σ) ⇒ (¬σ ⇒ ¬ρ)`
6. Adjunción: `((ρ ∧ σ) ⇒ τ ) ⇔ (ρ ⇒ σ ⇒ τ )`
7. de Morgan (I): `¬(ρ ∨ σ) ⇔ (¬ρ ∧ ¬σ)`
8. de Morgan (II): `¬(ρ ∧ σ) ⇔ (¬ρ ∨ ¬σ)`. Para la dirección ⇒ es necesario usar principios de razonamiento clásicos.
9. Conmutatividad (∧): `(ρ ∧ σ) ⇒ (σ ∧ ρ)`
10. Asociatividad (∧): `((ρ ∧ σ) ∧ τ ) ⇔ (ρ ∧ (σ ∧ τ ))`
11. Conmutatividad (∨): `(ρ ∨ σ) ⇒ (σ ∨ ρ)`
12. Asociatividad (∨): `((ρ ∨ σ) ∨ τ ) ⇔ (ρ ∨ (σ ∨ τ ))`
¿Encuentra alguna relación entre teoremas de adjunción, asociatividad y conmutatividad con algunas de las propiedades demostradas en la práctica 2?

---
## Respuestas
1. *Modus ponens* relativizado:

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

2. Reducción al absurdo:
```mermaid
flowchart BT
 x5["(ρ ⇒ ⊥), p ⊢  ⇒  ρ"]
 x4["(ρ ⇒ ⊥), p ⊢  ⇒ ¬ρ"]
 x3["(ρ ⇒ ⊥), p ⊢  ⇒ ⊥"]
 x2["(ρ ⇒ ⊥) ⊢  ⇒ ¬ρ"]
 x1["⊢ (ρ ⇒ ⊥) ⇒ ¬ρ"]
 
 x1 --- x2
 x2 --- x3
 x3 --- x4
 x3 --- x5
```
3. Introducción de la doble negación:
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
4. Eliminación de la triple negación:
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

5. Contraposición

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
6. Adjunción
```mermaid
flowchart BT

x1["⊢((ρ∧σ)⇒τ) ⇒ (ρ⇒σ⇒τ)"]
x2["(ρ∧σ)⇒τ ⊢ ρ⇒σ⇒τ"]
x3["(ρ∧σ)⇒τ, ρ ⊢ σ⇒τ"]
x4["(ρ∧σ)⇒τ, ρ, σ ⊢ τ"]
x5["(ρ∧σ)⇒τ, ρ, σ ⊢ (ρ∧σ) ⇒ τ"]
x6["(ρ∧σ)⇒τ, ρ, σ ⊢ ρ∧σ"]
x7["(ρ∧σ)⇒τ, ρ, σ ⊢ ρ"]
x8["(ρ∧σ)⇒τ, ρ, σ ⊢ σ"]

x1 --- x2
x2 --- x3
x3 --- x4
x4 --- x5
x4 --- x6
x6 --- x7
x6 --- x8
```


7. de Morgan (I):
```mermaid
flowchart BT

x1["⊢¬(ρ ∨ σ) ⇒ (¬ρ ∧ ¬σ)"]

```

```mermaid
flowchart BT

x1["⊢(¬ρ ∧ ¬σ) ⇒ ¬(ρ ∨ σ)"]
x2["¬ρ ∧ ¬σ ⊢ ¬(ρ ∨ σ)"]
x3["¬ρ ∧ ¬σ, ρ ∨ σ ⊢ ⊥"]
x4["¬ρ ∧ ¬σ, ρ ∨ σ ⊢ ρ"]
x5["¬ρ ∧ ¬σ, ρ ∨ σ ⊢ ¬ρ"]
x6["¬ρ ∧ ¬σ, ρ ∨ σ ⊢ ¬ρ ∧ ¬σ"]
x7["¬ρ ∧ ¬σ, ρ ∨ σ ⊢ ρ ∨ σ"]
x8["¬ρ ∧ ¬σ, ρ ∨ σ, ρ ⊢ ρ"]
x9["¬ρ ∧ ¬σ, ρ ∨ σ, σ ⊢ ρ"]
x10["¬ρ ∧ ¬σ, ρ ∨ σ, σ ⊢ ⊥"]
x11["¬ρ ∧ ¬σ, ρ ∨ σ, σ ⊢ σ"]
x12["¬ρ ∧ ¬σ, ρ ∨ σ, σ ⊢ ¬σ"]
x13["¬ρ∧¬σ, ρ∨σ, σ ⊢ ¬ρ∧¬σ"]

x1  --- x2
x2  --- x3
x3  --- x4
x3  --- x5
x5  --- x6
x4  --- x7
x4  --- x8
x4  --- x9
x9  --- x10
x10 --- x11
x10 --- x12
x12 --- x13
```
8. de Morgan (II):
```mermaid
flowchart BT

x1["⊢¬(ρ ∧ σ) ⇒ (¬ρ ∨ ¬σ)"]

```

```mermaid
flowchart BT

x1["⊢(¬ρ ∨ ¬σ) ⇒ ¬(ρ ∧ σ)"]
x2["¬ρ ∨ ¬σ ⊢ ¬(ρ ∧ σ)"]
x3["¬ρ ∨ ¬σ, ρ ∧ σ ⊢ ⊥"]
x4["¬ρ ∨ ¬σ, ρ ∧ σ ⊢ ρ"]
x5["¬ρ ∨ ¬σ, ρ ∧ σ ⊢ ¬ρ"]
x6["¬ρ ∨ ¬σ, ρ ∧ σ ⊢ ρ ∧ σ"]
x7["¬ρ ∨ ¬σ, ρ ∧ σ, ρ ⊢ ⊥"]
x8["¬ρ ∨ ¬σ, ρ ∧ σ, ρ ⊢ σ"]
x9["¬ρ ∨ ¬σ, ρ ∧ σ, ρ ⊢ ¬σ"]
x10["¬ρ∨¬σ, ρ∧ σ ⊢ ρ ∧ σ"]
x11["¬ρ∨¬σ, ρ∧σ, ρ, σ ⊢ ⊥"]
x12["¬ρ∨¬σ,ρ∧σ,ρ,σ⊢¬ρ∨¬σ"]
x13["¬ρ∨¬σ, ρ∧σ, ρ, σ, ¬ρ ⊢ ⊥"]
x14["¬ρ∨¬σ, ρ∧σ, ρ, σ, ¬σ ⊢ ⊥"]
x15["¬ρ∨¬σ, ρ∧σ, ρ, σ, ¬σ ⊢ ρ"]
x16["¬ρ∨¬σ, ρ∧σ, ρ, σ, ¬σ ⊢ ¬p"]
x17["¬ρ∨¬σ, ρ∧σ, ρ, σ, ¬σ ⊢ σ"]
x18["¬ρ∨¬σ, ρ∧σ, ρ, σ, ¬σ ⊢ ¬σ"]

x1  --- x2
x2  --- x3
x3  --- x4
x4  --- x6
x3  --- x5
x5  --- x7
x7  --- x8
x7  --- x9
x8  --- x10
x9  --- x11
x11 --- x12
x11 --- x13
x11 --- x14
x13 --- x15
x13 --- x16
x14 --- x17
x14 --- x18
```
9. Conmutatividad
```mermaid
flowchart BT

x1["⊢(ρ ∧ σ) ⇒ (σ ∧ ρ)"]
x2["ρ ∧ σ ⊢ (σ ∧ ρ)"]
x3["ρ ∧ σ ⊢ σ"]
x4["ρ ∧ σ ⊢ ρ"]
x5["ρ ∧ σ ⊢ ρ ∧ σ"]
x6["ρ ∧ σ ⊢ ρ ∧ σ"]

x1 --- x2
x2 --- x3
x2 --- x4
x3 --- x5
x4 --- x6
```

10. Asociatividad
```mermaid
flowchart BT

x1["⊢((ρ∧σ)∧τ)⇒(ρ∧(σ∧τ))"]
x2["(ρ∧σ)∧τ⊢ρ∧(σ∧τ)"]
x3["(ρ∧σ)∧τ⊢ρ"]
x4["(ρ∧σ)∧τ⊢σ∧τ"]
x5["(ρ∧σ)∧τ⊢σ"]
x6["(ρ∧σ)∧τ⊢τ"]
x7["(ρ∧σ)∧τ⊢ρ∧σ"]
x8["(ρ∧σ)∧τ⊢ρ∧σ"]
x9["(ρ∧σ)∧τ⊢(ρ∧σ)∧τ"]
x10["(ρ∧σ)∧τ⊢(ρ∧σ)∧τ"]
x11["(ρ∧σ)∧τ⊢(ρ∧σ)∧τ"]
x1 --- x2
x2 --- x3
x2 --- x4
x3 --- x7
x4 --- x5
x4 --- x6
x5 --- x8
x6 --- x9
x7 --- x10
x8 --- x11
```


```mermaid
flowchart BT

x1["⊢(ρ∧(σ∧τ))⇒((ρ∧σ)∧τ)"]
x2["ρ∧(σ∧τ)⊢(ρ∧σ)∧τ"]
x3["ρ∧(σ∧τ)⊢ρ∧σ"]
x4["ρ∧(σ∧τ)⊢τ"]
x5["ρ∧(σ∧τ)⊢σ∧τ"]
x6["ρ∧(σ∧τ)⊢ρ∧(σ∧τ)"]
x7["ρ∧(σ∧τ)⊢p"]
x8["ρ∧(σ∧τ)⊢σ"]
x9["ρ∧(σ∧τ)⊢ρ∧(σ∧τ)"]
x10["ρ∧(σ∧τ)⊢σ∧τ"]
x11["ρ∧(σ∧τ)⊢ρ∧(σ∧τ)"]
x1 --- x2
x2 --- x3
x2 --- x4
x4 --- x5
x5 --- x6
x3 --- x7
x3 --- x8
x7 --- x9
x8 --- x10
x10 --- x11
```
11. Conmutatividad
```mermaid
flowchart BT

x1["⊢(ρ ∨ σ) ⇒ (σ ∨ ρ)"]
x2["ρ ∨ σ ⊢σ ∨ ρ"]
x3["ρ ∨ σ ⊢ ρ ∨ σ"]
x4["ρ ∨ σ, ρ ⊢ σ ∨ ρ"]
x5["ρ ∨ σ, σ ⊢ σ ∨ ρ"]
x6["ρ ∨ σ, ρ ⊢ ρ"]
x7["ρ ∨ σ, σ ⊢ σ"]

x1 --- x2
x2 --- x3
x2 --- x4
x2 --- x5
x4 --- x6
x5 --- x7
```
12. Asociatividad
```mermaid
    flowchart BT
    
x1["⊢((ρ ∨ σ) ∨ τ ) ⇒ (ρ ∨ (σ ∨ τ ))"]
x2["(ρ ∨ σ) ∨ τ ⊢ ρ ∨ (σ ∨ τ )"]
x3["(ρ ∨ σ) ∨ τ ⊢ (ρ ∨ σ) ∨ τ "]
x4["(ρ ∨ σ) ∨ τ, ρ ∨ σ ⊢ ρ ∨ (σ ∨ τ )"]
x5["(ρ ∨ σ) ∨ τ, τ ⊢ ρ ∨ (σ ∨ τ )"]
x6["(ρ ∨ σ) ∨ τ, ρ ∨ σ ⊢ ρ ∨ σ"]
x7["(ρ ∨ σ) ∨ τ, ρ ∨ σ, ρ ⊢ ρ ∨ (σ ∨ τ )"]
x8["(ρ ∨ σ) ∨ τ, ρ ∨ σ, σ ⊢ ρ ∨ (σ ∨ τ )"]
x9["(ρ ∨ σ) ∨ τ, τ ⊢ σ ∨ τ"]
x10["(ρ ∨ σ) ∨ τ, τ ⊢ τ"]
x11["(ρ ∨ σ) ∨ τ, ρ ∨ σ, ρ ⊢ ρ"]
x12["(ρ ∨ σ) ∨ τ, ρ ∨ σ, σ ⊢ σ ∨ τ"]
x13["(ρ ∨ σ) ∨ τ, ρ ∨ σ, σ ⊢ σ"]

x1  --- x2
x2  --- x3
x2  --- x4
x2  --- x5

x4  --- x6
x4  --- x7
x4  --- x8

x5  --- x9
x9  --- x10

x7  --- x11
x8  --- x12
x12 --- x13
```

```mermaid
    flowchart BT
    
x1["⊢(ρ ∨ (σ ∨ τ )) ⇒ ((ρ ∨ σ) ∨ τ )"]
x2["ρ ∨ (σ ∨ τ) ⊢ (ρ ∨ σ) ∨ τ "]
x3["ρ ∨ (σ ∨ τ) ⊢ ρ ∨ (σ ∨ τ) "]
x4["ρ ∨ (σ ∨ τ), ρ ⊢ (ρ ∨ σ) ∨ τ "]
x5["ρ ∨ (σ ∨ τ), σ ∨ τ ⊢ (ρ ∨ σ) ∨ τ "]
x6["ρ ∨ (σ ∨ τ), ρ ⊢ ρ ∨ σ"]
x7["ρ ∨ (σ ∨ τ), ρ ⊢ ρ"]
x8["ρ ∨ (σ ∨ τ), σ ∨ τ ⊢ σ ∨ τ "]
x9["ρ ∨ (σ ∨ τ), σ ∨ τ, σ ⊢ (ρ ∨ σ) ∨ τ "]
x10["ρ ∨ (σ ∨ τ), σ ∨ τ, τ ⊢ (ρ ∨ σ) ∨ τ "]
x11["ρ ∨ (σ ∨ τ), σ ∨ τ, τ ⊢ τ "]
x12["ρ ∨ (σ ∨ τ), σ ∨ τ, σ ⊢ ρ ∨ σ"]
x13["ρ ∨ (σ ∨ τ), σ ∨ τ, σ ⊢ σ"]

x1 --- x2

x2 --- x3
x2 --- x4
x2 --- x5

x4 --- x6
x6 --- x7

x5 --- x8
x5 --- x9
x5 --- x10

x9 --- x12
x12 --- x13

x10 --- x11
```
