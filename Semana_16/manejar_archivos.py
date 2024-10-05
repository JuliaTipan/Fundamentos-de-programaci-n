# Escribir archivo de texto
# Abrimos el archivo en modo escritura ('w')
file = open('my_notes.txt', 'w')
# Escribimos tres líneas de notas personales y damos saltos con \n
file.write("Mi número favorito 2918\n")
file.write("16 de septiembre fecha pendiente\n")
file.write("componer la figura del hombre es recomponer el mundo\n")
file.write("Aceptar que las cosas no salen como uno quiere\n")
file.close() # Cerramos el archivo

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r' para leer)
file = open('my_notes.txt', 'r')
# Leemos y mostramos el contenido línea por línea
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close() # Cerramos el archivo