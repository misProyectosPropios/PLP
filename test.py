""" 
    Archivo usado para testear la confiabilidad de las funciones que realizamos para el TP
"""

# Leer https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#unresolved-import-warnings
import unittest
import numpy as np
#import funciones_2

class TestFuncionesAuxiliares(unittest.TestCase):

    def setUp(self):
        #Creo objetos una sola vez, no en cada llamado
        self.matriz1 = np.array([
            [0, 1, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 0]
            ])

    def calcularGrado(self):

        pass

    def multMatrizPorVector(self):
        pass

    def productoInterno(self):
        pass

    def altoMatriz(A):
        pass

    def anchoMatriz(A):
        pass

class TestFuncionesCreadorasMatrices(unittest.TestCase):

    def setUp(self):
        pass

    def calcula_L(self):
        pass

    def calcula_R(self):
        pass

    def calcula_lambda(self):
        pass

    def calculaQ(A):
        pass


class TestMetodoDePotencia(unittest.TestCase):

    def setUp(self):
        pass # Crear unos objetos que usaré despues para no crearlos a cada rato

    def metpot1(self):
        pass

    def deflaciona(self):
        pass

    def metpotI(self):
        pass

    def metpotI2(A):
        pass