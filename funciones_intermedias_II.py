### 1. Actualiza los valores en diccionarios y listas

x = [[5, 2, 3], [10, 8, 9]]

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]

sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}

z = [{"x": 10, "y": 20}]

# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x[1][0] = 15
print(x)

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students[0]["last_name"] = "Bryant"
print(students[0])

# En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

# Camba el valor 20 en z a 30
z[0]["y"] = 30
print(z)


### 2. Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
def iterateDictionary (lista):
    for sts in range (len(lista)):
        print(f"first_name - {lista[sts]["first_name"]}, last_name - {lista[sts]["last_name"]}")

iterateDictionary(students)

### 3. Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

def iterateDictionary2(key_name, some_list):
    for sts in range (len(some_list)):
        print(f"{some_list[sts][key_name]}")

iterateDictionary2("first_name", students)

### 4. Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(f"{len(some_dict['locations'])} LOCATIONS")
    for locations in range (len(some_dict['locations'])):
        print(some_dict['locations'][locations])
    
    print(f"\n{len(some_dict['instructors'])} INSTRUCTORS")
    for instructors in range (len(some_dict['instructors'])):
        print(some_dict['instructors'][instructors])

printInfo(dojo)

""" def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)
        print()  # Salto de línea para separar secciones

printInfo(dojo) """