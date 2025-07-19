[[Notación]]

Determinar qué expresiones son sintácticamente válidas (es decir, pueden ser generadas con las gramáticas presentadas) y determinar a qué categoría pertenecen (expresiones de términos o expresiones de tipos)

1.  x
2. x x
3. M
4. M M
5. true false
6. true succ(false true)
7. λx.isZero(x)
8. λx : σ. succ(x)
9. λx : Bool. succ(x)
10. λx : if true then Bool else Nat. x
11. σ
12. Bool
13. Bool → Bool
14. Bool → Bool → Nat
15. (Bool → Bool) → Nat
16. succ true
17. λx : Bool. if zero then true else zero succ(true)
---
## Respuestas

1. Si, término
2. Si término
3. No
4. No
5. Si, término
6. Sí, término
7. Si, término
8. No
9. Si, término
10. No
11. No
12. Si, tipo
13. Si, tipo
14. Si, tipo
15. Si, tipo
16. No
17. Si