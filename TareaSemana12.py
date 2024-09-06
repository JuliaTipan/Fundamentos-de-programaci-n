# Definimos la matriz 3D de temperaturas (ciudad, semana, día de la semana)
temperaturas = [
    [  # Ciudad 1
        [22, 24, 23, 25, 21, 22, 23],  # Semana 1
        [24, 26, 25, 24, 23, 22, 24]  # Semana 2
    ],
    [  # Ciudad 2
        [19, 20, 22, 21, 23, 21, 20],  # Semana 1
        [18, 19, 21, 22, 20, 19, 20]  # Semana 2
    ]
]

# Número de ciudades, semanas y días
num_ciudades = len(temperaturas)
num_semanas = len(temperaturas[0])
num_dias = len(temperaturas[0][0])

# Iterar sobre ciudades y semanas para calcular el promedio de temperaturas
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(num_dias):
            suma_temperaturas += temperaturas[ciudad][semana][dia]

        # Calcular el promedio
        promedio = suma_temperaturas / num_dias
        print(f"Ciudad {ciudad + 1}, Semana {semana + 1}: Promedio de temperaturas = {promedio:.2f}°C")