def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

numbers = [3, 5, 1, 6, 7, 2, 4, 8]

bubble_sort(numbers)

print("Lista ordenada:", numbers)