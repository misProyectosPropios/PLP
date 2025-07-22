## Resolución para lógica proposicional

### Método de resolución

Entrada: una fórmula σ de la lógica proposicional.
Salida: un booleano que indica si σ es válida.

+ Escribir $\neg \sigma$  como un conjunto $\mathcal{C}$ de clausulas.
  (Pasar a forma clausal).
+ Buscar una refutación de $\mathcal{C}$.
+ Una refutación de $\mathcal{C}$ es una derivación de $\mathcal{C} \vdash \bot$.

Si se encuentra una refutación de $\mathcal{C}$:  
 Vale $\neg \sigma \vdash \bot$. Es decir, $\neg \sigma$ es insatisfactible/contradicción.  
 Luego vale $\vdash \sigma$. Es decir, $\sigma$ es válida/tautología.

Si no se encuentra una refutación de $\mathcal{C}$:  
 No vale $\neg \sigma \vdash \bot$. Es decir, $\sigma$ es satisfactible.  
 Luego no vale $\vdash \sigma$. Es decir, $\sigma$ no es válida.
### Definiciones

#### forma normal negada (NNF)
#### forma normal conjuntiva (CNF)

### Refutación

#### Algoritmo

### Corrección del algoritmo


## Resolución para lógica de primer orden

### Algoritmo para conversión de fórmulas

#### Skoleminización

La skolemnización preserva la satisfactibilidad, pero no la validez. 
>Para la resolución no nos importa eso, pues queremos ver que es insatisfactible su negación, no nos fijamos directamente si es válida o no

##### Ejemplo que no cumple la validez

|        Valida         | Inválida        |
| :-------------------: | :-------------- |
| $$∃X. (P(0) ⇒ P(X))$$ | $$P(0) ⇒ P(c)$$ |


### Refutación


### Corrección




