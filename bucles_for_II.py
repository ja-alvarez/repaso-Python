# 1. Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def biggie_size(lista):
    nueva_lista = []
    for i in range (0, len(lista)):
        if lista[i]>= 0:
            nueva_lista.append('big')
        else:
            nueva_lista.append(lista[i])
    return nueva_lista

print(biggie_size([- 1, 3, 5, -5, 0]))

# 2. Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

def count_positives (lista):
    positivos = 0
    nueva_lista = lista
    for i in range (0, len(lista)):
        if lista[i]> 0:
            positivos += 1
    nueva_lista[len(lista)-1] = positivos
    print('Positivos:', positivos)
    return nueva_lista

print(count_positives ([- 1,1,1,1]))

