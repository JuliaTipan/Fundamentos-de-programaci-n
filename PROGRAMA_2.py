# Definir una matriz 3x3 con valores numéricos a partir de 100
matriz = [
    [105, 150, 130],
    [200, 175, 160],
    [180, 190, 145]
]

# Función para ordenar los valores de una fila específica en orden ascendente
def ordenar_fila(matriz, fila_index):
    # Obtener los valores de la fila que se va a ordenar usando el índice proporcionado
    fila = matriz[fila_index]
    # Ordenar los valores usando un enfoque de Bubble Sort
    for i in range(len(fila)):
        for j in range(0, len(fila) - i - 1):
            # Comparar elementos adyacentes y ordenarlos si están en el orden incorrecto
            if fila[j] > fila[j + 1]:
                # Intercambiar los elementos
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    # Asignar la fila ordenada de vuelta a la matriz
    matriz[fila_index] = fila

# Mostrar la matriz original antes de la ordenación
print("Matriz original:")
for fila in matriz:
    print(fila)

# Índice de la fila que se va a ordenar (por ejemplo, la segunda fila)
fila_a_ordenar = 1

# Llamar a la función de ordenación para la fila especificada
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de que la fila especificada ha sido ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)