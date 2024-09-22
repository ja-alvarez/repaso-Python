"""
    Esta clase implementa métodos similares a la biblioteca Underscore de JavaScript, 
    permitiendo realizar operaciones funcionales sobre iterables. Los métodos incluyen 
    `map`, `find`, `filter` y `reject`, que utilizan funciones de retorno (callbacks) 
    para manipular listas de acuerdo a condiciones específicas.
    """


class Underscore:
    def map(self, iterable, callback):
        return [callback(item) for item in iterable]

    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None

    def filter(self, iterable, callback):
        return [item for item in iterable if callback(item)]

    def reject(self, iterable, callback):
        return [item for item in iterable if not callback(item)]


# Ejemplos de uso:

_ = Underscore()

# Filtrar los números pares
evens = _.filter([1, 8, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)  # debe retornar [8, 2, 4, 6]

# Mapear para duplicar los valores
print(_.map([1, 2, 3], lambda x: x * 2))  # debe retornar [2, 4, 6]

# Encontrar el primer valor mayor que 4
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))  # debe retornar 5

# Filtrar los números pares
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  # debe retornar [2, 4, 6]

# Rechazar los números pares
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))  # debe retornar [1, 3, 5]
