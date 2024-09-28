#Crear diccionario con información personal
informacion_personal = {"nombre":"Jayden Chiluisa","edad":28,"ciudad":"Latacunga","profesion":"ingeniero"}

# Acceder al valor de la clave "ciudad" y modificarlo
print (informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Ambato"  # Modificando la ciudad

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Desarrollador de Software"  # Modificando la profesión

# Verificar si la clave "telefono" existe en el diccionario
print("telefono" in informacion_personal)
informacion_personal["telefono"] = "0995235519"  # Agregando un teléfono ficticio

# Eliminar la clave "edad"
del informacion_personal["edad"]  # Eliminando la edad

#Imprimir diccionario resultante
print (informacion_personal)