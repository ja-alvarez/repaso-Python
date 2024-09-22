# 1. Cuenta regresiva. crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).


def cuenta_regresiva(numero):
    cuenta = []
    for numero in range(numero, 0 - 1, -1):
        cuenta.append(numero)
    return cuenta


print(cuenta_regresiva(5))

# 2. Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo. Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2


def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]


imprimir_y_devolver([1, 2])

# 3. First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista. Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)


def first_plus_length(lista):
    return lista[0] + len(lista)


print(first_plus_length([1, 2, 3, 4, 5]))

# 4. Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False


def values_greater_than_second(lista):
    nueva_lista = []
    if len(lista) < 2:
        return False
    else:
        for i in range(0, len(lista)):
            if lista[i] > lista[1]:
                nueva_lista.append(lista[i])
        print(len(nueva_lista))  # imprime length de la nueva lista
        return nueva_lista


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))

# 5. escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]


def length_and_value(length, value):
    return [value] * length


"""     nueva_lista = []
    for i in range(0,length):
        nueva_lista.append(value)
    return nueva_lista """

print(length_and_value(4, 7))
