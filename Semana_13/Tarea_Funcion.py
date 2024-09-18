temperaturas = [
    [   # Latacunga
        [18, 20, 22, 19, 15, 18, 13],  # Semana 1
        [16, 19, 23, 21, 17, 19, 23],  # Semana 2
        [17, 21, 15, 22, 18, 21, 15],  # Semana 3
        [17, 21, 15, 22, 18, 21, 15]   # Semana 4
    ],
    [   # Salcedo
        [22, 14, 18, 20, 23, 15, 19],  # Semana 1
        [13, 16, 20, 22, 15, 17, 21],  # Semana 2
        [21, 15, 18, 20, 22, 16, 20],  # Semana 3
        [22, 14, 18, 20, 23, 15, 19]   # Semana 4
    ],
    [   # Ambato
        [20, 22, 14, 21, 18, 15, 22],  # Semana 1
        [19, 21, 23, 20, 17, 14, 21],  # Semana 2
        [21, 23, 15, 22, 19, 16, 23],  # Semana 3
        [18, 17, 18, 20, 21, 20, 19]   # Semana 4
    ]
]
def calcular_promedio_ciudad_semana(temperaturas, ciudad_numero, semana_numero):
    """
    Parámetros:
    temperaturas (list): Lista de listas con los datos de temperatura.
    ciudad_numero (int): Número de la ciudad (0 para la primera ciudad, 1 para la segunda, etc.).
    semana_numero (int): Número de la semana (0 para la primera semana, 1 para la segunda, etc.).

    Retorna:
    float: El promedio de temperaturas para la ciudad y semana especificada.
    """
    # Obtener los datos de la ciudad y semana especificadas
    ciudad = temperaturas[ciudad_numero]
    semana = ciudad[semana_numero]

    # Calcular el promedio
    promedio = sum(semana) / len(semana)
    return promedio

ciudad_numero = 1  # Salcedo
semana_numero = 2  # Semana 3
promedio = calcular_promedio_ciudad_semana(temperaturas, ciudad_numero, semana_numero)
print(f"Promedio de temperaturas en Ciudad {ciudad_numero + 1}, Semana {semana_numero + 1}: {promedio:.2f}°C")


def calcular_promedios(temperaturas):
    """
    Parámetros:
    temperaturas (list): Lista de listas con los datos de temperatura para diferentes ciudades y semanas.

    Retorna:
    tuple: Un tuple con dos elementos:
        - Promedio general de todas las ciudades y semanas.
        - Lista con los promedios de temperaturas para cada semana dentro de cada ciudad.
    """
    # Inicializar listas para almacenar todas las temperaturas y promedios semanales
    total_temperaturas = []
    promedios_semanales = []

    # Recorrer cada ciudad en los datos
    for ciudad in temperaturas:
        promedios_ciudad = []
        # Recorrer cada semana en la ciudad
        for semana in ciudad:
            total_temperaturas.extend(semana)  # Agregar todas las temperaturas de la semana a la lista

            # Calcular el promedio de la semana
            promedio_semana = sum(semana) / len(semana)
            promedios_ciudad.append(promedio_semana)

        promedios_semanales.append(promedios_ciudad)

    # Calcular el promedio general
    promedio_general = sum(total_temperaturas) / len(total_temperaturas)

    return promedio_general, promedios_semanales

promedio_general, promedios_semanales = calcular_promedios(temperaturas)

print(f"Promedio de temperaturas para todas las ciudades y semanas: {promedio_general:.2f}°C")

print("\nPromedio de temperaturas por semana en cada ciudad:")
for i, promedios in enumerate(promedios_semanales):
    print(f"Ciudad {i + 1}:")
    for j, promedio in enumerate(promedios):
        print(f"  Semana {j + 1}: {promedio:.2f}°C")

