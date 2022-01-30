"""
Ejercicios relacionaods con la Practica de la leccion 4

Autor: Israel Duran Alonso
"""

"""
Ejercicio 1 de la practica 4
"""
import math
import pdb

lista = [[2,4,1], [1,2,3,4,5,6,7,8], [100,250,43]]

pdb.set_trace()
numero_mayor = [print('El mayor numero es: ', max(i)) for i in lista]
print(numero_mayor)

"""
Ejercicio 2 de la practica 4
"""

lista2 = [3, 4, 8, 5, 5, 22, 13]

def numero_primo(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n_primo = list(filter(numero_primo, [x for x in lista2]))
print(n_primo)