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

print('############### 4 ################')
