# Definir una matriz 3x3 con valores numéricos
matriz = [
    [105, 150, 130],
    [200, 175, 160],
    [180, 190, 145]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_a_buscar):
    # Iterar sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Iterar sobre cada columna de la fila
        for j in range(len(matriz[i])):
            # Verificar si el valor en la posición actual coincide con el valor buscado
            if matriz[i][j] == valor_a_buscar:
                # Si se encuentra el valor, retornar la posición como una tupla (fila, columna)
                return (i, j)
    # Si no se encuentra el valor, retornar None
    return None

# Definir el valor a buscar
valor_a_buscar = 175

# Llamar a la función de búsqueda y almacenar el resultado en la variable 'posicion'
posicion = buscar_valor(matriz, valor_a_buscar)

# Verificar si se encontró el valor y mostrar un mensaje apropiado
if posicion:
    print(f"Valor {valor_a_buscar} encontrado en la posición: {posicion}")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz.")