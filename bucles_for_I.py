# 1. imprime todos los enteros del 0 al 150.
for numero in range(0, 151):
    print (numero)


#2. imprime todos los múltiplos de 5 de 5 a 1,000
for multiplo_cinco in range(5, 1001, 5):
    print(multiplo_cinco)

# 3. imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for entero in range(1, 101):
    if entero % 10 == 0:
        print('Coding Dojo')
    elif entero % 5 == 0:
        print('Coding')
    else:
        print(entero)
