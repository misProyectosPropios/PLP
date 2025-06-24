desde(X,X).
desde(X,Y) :- var(Y), N is X+1, desde(N,Y).

%
desdeInstanciado(X,Y) :- X =< Y.

desdeReversible(X,Y) :- var(Y), desde(X,Y).
desdeReversible(X,Y) :- nonvar(Y), desdeInstanciado(X,Y).

vacio(Nil).

raiz(bin(_, V, _), V).

altura(Nil, 0).
altura(bin(Izq, _, Der), Alt) :- var(Alt), altura(Izq, AltIzq), altura(Der, AltDer), max() Alt is 1 + Maximo.

cantidadDeNodos(Nil, 0).
cantidadDeNodos(bin(Izq, _, Der), CantNodos ) :- cantidadDeNodos(Izq, NodosIzq), cantidadDeNodos(Der, NodosDer), CantNodos is NodosIzq + NodosDer.

