Para crear los fold y rec se sigue un procedimiento mecánico:

Dado un [[Tipos de datos algebraicos]], tenemos unos casos que son:
+ Base
+ Recursivos

Tenemos que hacer que el fold entre en todos sus constructores

Ejemplo:

```haskell

data Prop = Var String | No Prop | Y Prop Prop | O Prop Prop | Imp Prop Prop

foldProp :: (String -> a) -> (a -> a) -> (a -> a -> a) -> (a -> a-> a) (a -> a -> a) -> Prop -> a
foldProp fVar fNo fY fO fImp (Var string) = fVar string
foldProp fVar fNo fY fO fImp (No prop) = fNo (recr prop)
foldProp fVar fNo fY fO fImp (Y prop1 prop2) = fY (recr prop1) (recr prop2)
foldProp fVar fNo fY fO fImp (O prop1 prop2) = fO (recr prop1) (recr prop2)
foldProp fVar fNo fY fO fImp (Imp prop1 prop2) = fImp (recr prop1) (recr prop2)
	where recr = foldProp fVar fNo fY fO fImp

recProp :: (String -> a) -> (Prop -> a -> a) -> (Prop -> Prop -> a -> a -> a) -> (Prop -> Prop -> a -> a-> a) (Prop -> Prop -> a -> a -> a) -> Prop -> a
recProp fVar fNo fY fO fImp (Var string) = fVar string
recProp fVar fNo fY fO fImp (No p1) = fNo prop (recr p1)
recProp fVar fNo fY fO fImp (Y p1 p2) = fY p1 p2 (recr prop1) (recr prop2)
recProp fVar fNo fY fO fImp (O p1 p2) = fO p1 p2 (recr prop1) (recr prop2)
recProp fVar fNo fY fO fImp (Imp p1 p2) = fImp p1 p2 (recr prop1) (recr prop2)
	where recr = recProp fVar fNo fY fO fImp
```

Con este ejemplo se puede ver como sería para  crear un `fold` y `rec` de cualquier tipo algebraico que se cree

## Observaciones:

Se puede crear `foldr` usando `recr`. También se puede de la otra forma, pero no es recomendable.
Para hacerlo, tenemos los mismos tipos que se generarían si lo hiciésemos a mano y después hacemos nuevas funciones tales que hagan lo mismo que las que nos pasaron, pero que reciban `N` parametros demás que los ignores (los tipos recursivos).