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

# 3. Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total (lista):
    sum = 0
    for i in range(0, len(lista)):
        sum += lista[i]
    return sum
print(sum_total([6, 3, -2]))

# 4. Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio (lista):
    avg = 0
    for i in range(0, len(lista)):
        avg += lista[i]
    return avg/len(lista)
print(promedio([1,2,3,4,5]))

# 5. Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def longitud (lista):
    return len(lista)

print('longitud', longitud([1, 2, 3]))

# 6. Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False