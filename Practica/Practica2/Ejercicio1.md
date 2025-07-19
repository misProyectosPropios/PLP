Sean las siguientes definiciones de funciones:

```haskell
{i}  intercambiar (x,y) = (y,x)
{eL} espejar (Left x) = Right x
{eR} espejar (Right x) = Left x
{aI} asociarI (x,(y,z)) = ((x,y),z)
{aD} asociarD ((x,y),z)) = (x,(y,z))
{f}  flip f x y = f y x
{c}  curry f x y = f (x,y)
{u}  uncurry f (x,y) = f x y
```

Demostrar las siguientes igualdades usando los lemas de generación cuando sea necesario

1. `∀ p::(a,b) . intercambiar (intercambiar p) = p`
2. `∀ p::(a,(b,c)) . asociarD (asociarI p) = p`
3. `∀ p::Either a b . espejar (espejar p) = p`
4. `∀ f::a->b->c . ∀ x::a . ∀ y::b . flip (flip f) x y = f x y`
5. `∀ f::a->b->c . ∀ x::a . ∀ y::b . curry (uncurry f) x y = f x y`
---
## Respuestas

> Aclaración: pide usarlo haciendo lemas de generación
1.  
```
Teorema: ∀ p :: (a,b) intercambiar (intercambiar p) = p

Por principio de inducción sobre pares, basta probar 
∀a ∀b (a,b) :: (x,y) intercambiar (intercambiar (a,b)) = (a,b)

    ∀a ∀b (a,b) :: (x,y) . intercambiar (intercambiar (a,b)) = (a,b)
{i} ∀a ∀b (a,b) :: (x,y) . intercambiar (b,a) = (a,b)
{i} ∀a ∀b (a,b) :: (x,y) . (a,b) = (a,b)
```

2. 
```
Teorema: ∀ p::(a,(b,c)) . asociarD (asociarI p) = p

Por principio de inducción sobre pares, basta probar
∀a ∀d (a,d) :: (x, (b,c)) . asociarD (asociarI (a,d)) = (a,d)

Por principio de inducción sobre pares, basta probar
     ∀a ∀b ∀c (a,(b,c)) :: (x, (y,z)) . asociarD (asociarI (a,(b,c))) = (a,(b,c))
{aI} ∀a ∀b ∀c (a,(b,c)) :: (x, (y,z)) . asociarD ((a,b),c) =  (a,(b,c))
{aD} ∀a ∀b ∀c (a,(b,c)) :: (x, (y,z)) . (a,(b,c)) =  (a,(b,c))
```

3. 
```
Teorema: ∀ p::Either a b . espejar (espejar p) = p

Por lemas de generación para sumas
+ p bien ∃x :: a. e = Left x
+ o bien ∃y :: b. e = Right y

1) Caso Left x
     ∀ Left x:: Either a b . espejar (espejar Left x) = Left x
{eL} ∀ Left x:: Either a b . espejar (Right y) = Left x
{eR} ∀ Left x:: Either a b . Left x = Left x

2) Caso Right y
     ∀ Right y:: Either a b . espejar (espejar Right y) = Right y
{eR} ∀ Right y:: Either a b . espejar (Left x) = Right y
{eL} ∀ Right y:: Either a b . Right y = Right y

Como vimos que ambos casos son correctos, podemos afirmar que el teorema es verdadero
```

4. 
```
Teorema: ∀ f::a->b->c . ∀ x::a . ∀ y::b . flip (flip f) x y = f x y

    ∀ f::a->b->c . ∀ x::a . ∀ y::b . flip (flip f) x y = f x y
{f} ∀ f::a->b->c . ∀ x::a . ∀ y::b . flip f y x = f x y
{f} ∀ f::a->b->c . ∀ x::a . ∀ y::b . f x y = f x y
```

5.  
```
Teorema: ∀ f::a->b->c . ∀ x::a . ∀ y::b . curry (uncurry f) x y = f x y

    ∀ f::a->b->c . ∀ x::a . ∀ y::b . curry (uncurry f) x y = f x y
{c} ∀ f::a->b->c . ∀ x::a . ∀ y::b . uncurry f (x,y) = f x y
{u} ∀ f::a->b->c . ∀ x::a . ∀ y::b . f x y = f x y
```