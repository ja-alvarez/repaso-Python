# escribir una sola función, randInt() que tome hasta 2 argumentos.
# Si no se proporcionan argumentos, la función debería devolver un entero aleatorio entre 0 y 100.
# Si solo se proporciona un número máximo, la función debe devolver un número entero aleatorio entre 0 y el número máximo.
# Si solo se proporciona un número mínimo, la función debe devolver un número entero aleatorio entre el número mínimo y 100
# Si se proporcionan un número mínimo y máximo, la función debe devolver un número entero aleatorio entre esos 2 valores.
# Crea esta función sin usar random.randInt ()

import random


def randInt(min=0, max=100):
    num = round(random.random() * (max - min) + min)
    return num


print(randInt(max=5))
print(randInt(min=50, max=500))
