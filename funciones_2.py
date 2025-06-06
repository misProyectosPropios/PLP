import numpy as np

#-----------------------------------------------------------------------------
# FUNCIONES AUXILIARES

def calcularGrado(A, nodo):
    """ 
    Calcula el grado del nodo dado a partir de A

    Parametros
    ----------
        A: [[]] 
            Matriz de adyacencia
        N: int
            Nodo de la matriz de adyacencia
            Debe ser un numero entre 0 y |A| - 1
    """
    grado = 0
    i = 0
    while i < altoMatriz(A):
        if (A[nodo][i] != 0):
            grado += 1
        i +=1
    return grado

def esSimetrica(A):
    """
    Devuelve si es simetrica la matriz

    Parametros
    ----------
        A: [[]]
            Matriz
    """
    if (altoMatriz(A) != anchoMatriz(A)):
        return False
    for i in range(altoMatriz(A)):
        for j in range(anchoMatriz(A)):
            if (A[i][j] != A[j][i]):
                return False
    return True

def simetrizarMatriz(A):
    """
    Simetriza una matriz haciendo: 1/2(A + A^t)
    
    Parametros
    ----------
        A: [[]]
            Matriz
            Debe ser cuadrada 
    """
    res = A.copy()
    return (1/2) * (res + res.transpose())

def multMatrizPorVector(A, v):
    """
    Realiza la multiplicacion entre una matriz y un vector columna

    Parametros
    ----------
        A: matriz de K^(m x n)
        v: vector de K^(n x 1)

    Devuelve el vector de K^(m x 1) producto de la multiplicacion matricial
    """
    res = []
    for i in range(altoMatriz(A)):
        valor = 0
        for j in range(anchoMatriz(A)):
            valor += A[i][j] * v[j]
        res.append(valor)
    return res

def productoInterno(v1, v2):
    # Se reciben 2 vectores v1, v2 de tamaño n x 1
    """
    Realiza el producto interno entre 2 vectores

    Parametros:
        v1, v2: vector de k^(n x 1)

    Calcula el producto interno entre ambos vectores
    """
    res = 0
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    return res

def altoMatriz(A):
    """
        Dada una matriz de k^(m x n), devuelve m
    """
    return len(A)

def anchoMatriz(A):
    """
        Dada una matriz de k^(m x n), devuelve n
    """
    return len(A[0])

#-----------------------------------------------------------------------------

# Matriz A de ejemplo
A_ejemplo = np.array([
   [0, 1, 1, 1, 0, 0, 0, 0],
   [1, 0, 1, 1, 0, 0, 0, 0],
   [1, 1, 0, 1, 0, 1, 0, 0],
   [1, 1, 1, 0, 1, 0, 0, 0],
   [0, 0, 0, 1, 0, 1, 1, 1],
   [0, 0, 1, 0, 1, 0, 1, 1],
   [0, 0, 0, 0, 1, 1, 0, 1],
   [0, 0, 0, 0, 1, 1, 1, 0]
])

def calcula_L(A):
    """
    Calcula la matriz laplaciona del grafo A

    Parametros
    ----------
    A: [[]]
        Matriz de k^(n x n) simetrica

    Devuelve la matriz que la definimos como L = K - A
    Siendo K la matriz diagonal de los grados de cada vertice en la diagonal y 0s en todas las otras celdas
    """
    L = A.copy()
    for i in range(altoMatriz(A)):
        gradoNodoI = calcularGrado(A, i)
        for j in range(altoMatriz(A)):
            L[i][j] *= (-1)
        # Ahora le sumo a la diagonal principal el grado
        L[i][i] += gradoNodoI 
    return L

def calcula_R(A):
    """
    Calcula la matriz R, definida como R = A - P

    Parametros
    ----------
    A: [[]]
        Matriz de k^(n x n) simetrica

    Devuelve R.
    Cada celda de R_(ij) = A_(ij) - ((k_i  * k_j) / 2E)
    Siendo k_i el grado del vertice i
    """
    R = A.copy()
    grados = []
    E = 0
    for i in range(altoMatriz(A)):
        grados.append(calcularGrado(A, i))
        E += grados[i]
    
    #Tecnicamente E := 2E ya que E se suma de toda las filas y eso es su definicion
    #Ahora falta hacer la resta entre A y P (P esta implicito con lo que ya calculamos hasta ahora)
    print(grados)
    print(f"E = {E}")
    for i in range(altoMatriz(A)):
        for j in range(altoMatriz(A)):
            R[i][j] = R[i][j] - ((grados[i] * grados[j]) / (E / 2))
    return R

print(A_ejemplo)
print(calcula_R(A_ejemplo))

def calcula_lambda(L,v):
    # Recibe L y v y retorna el corte asociado
    # Lambda = (1/4) s^t L s
    Ls = multMatrizPorVector(L, v)
    lambdon = productoInterno(v, Ls) * 1/4
    return lambdon
