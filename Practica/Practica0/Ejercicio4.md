Definir las siguientes funciones sobre listas:

1. `limpiar :: String → String → String`, que elimina todas las apariciones de cualquier carácter de la primera cadena en la segunda. Por ejemplo, limpiar ‘‘susto’’ ‘‘puerta’’ evalúa a ‘‘pera’’. Nota: `String` es un renombre de `[Char]`. La notación ‘‘hola’’ es equivalente a `[‘h’,‘o’,‘l’,‘a’]` y a `‘h’:‘o’:‘l’:‘a’:[].`
2. `difPromedio :: [Float] → [Float]` que dada una lista de números devuelve la diferencia de cada uno con el promedio general. Por ejemplo, `difPromedio [2, 3, 4]` evalúa a `[-1, 0, 1]`.
3. `todosIguales :: [Int] → Bool` que indica si una lista de enteros tiene todos sus elementos iguales.