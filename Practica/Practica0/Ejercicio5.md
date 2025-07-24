Dado el siguiente modelo para árboles binarios:
```haskell
data AB a = Nil | Bin (AB a) a (AB a)
```
definir las siguientes funciones:

1. `vacioAB :: AB a → Bool` que indica si un árbol es vacío (i.e. no tiene nodos).
2. `negacionAB :: AB Bool → AB Bool` que dado un árbol de booleanos construye otro formado por la negación de cada uno de los nodos.
3. `productoAB :: AB Int → Int` que calcula el producto de todos los nodos del árbol.

---
## Respuestas
1. 
```haskell
vacioAB :: AB a -> Bool
vacioAB Nil = True
vacioAB _ = False
```
2.  
```haskell
negacionAB :: AB Bool -> AB Bool
negacionAB Nil = Nil
negacionAB (Bin i v d) = Bin (negacionAB i) (not v) (negacionAB d)
```
3.  
```haskell
productoAB :: AB Bool -> Bool
productoAB Nil = 1
productoAB (Bin i v d) = v * productoAB i * productoAB d
```