# Definir una matriz 3x3 con algunos meses del año
matriz = [
    ["Enero", "Febrero", "Marzo"],
    ["Abril", "Mayo", "Junio"],
    ["Julio", "Agosto", "Septiembre"]
]

# Función para buscar un mes en la matriz
def buscar_mes(matriz, mes_a_buscar):
    # Iterar sobre cada fila de la matriz
    for i in range(len(matriz)):
        # Iterar sobre cada columna de la fila
        for j in range(len(matriz[i])):
            # Verificar si el mes en la posición actual coincide con el mes buscado
            if matriz[i][j].lower() == mes_a_buscar.lower():
                # Si se encuentra el mes, retornar la posición como una tupla (fila, columna)
                return (i, j)
    # Si no se encuentra el mes, retornar no se encuetra el mes
    return None

# Definir el mes a buscar
mes_a_buscar = "Junio"

# Llamar a la función de búsqueda y almacenar el resultado en la variable 'posicion'
posicion = buscar_mes(matriz, mes_a_buscar)