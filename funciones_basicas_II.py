# Cuenta regresiva. crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).

def cuenta_regresiva (numero):
    cuenta =[]
    for numero in range (numero, 0-1, -1):
        cuenta.append(numero)
    return cuenta
print(cuenta_regresiva(5))

