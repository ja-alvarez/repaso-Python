# 1. Cuenta regresiva. crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).

def cuenta_regresiva (numero):
    cuenta =[]
    for numero in range (numero, 0-1, -1):
        cuenta.append(numero)
    return cuenta

print(cuenta_regresiva(5))

# 2. Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo. Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def imprimir_y_devolver (lista):
    print(lista[0])
    return lista[1]

imprimir_y_devolver([1,2])

# 3. First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista. Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

def first_plus_length(lista):
    return lista[0]+len(lista)

print(first_plus_length([1,2,3,4,5]))

