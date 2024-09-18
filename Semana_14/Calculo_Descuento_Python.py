# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
# Primer monto total de compra
monto_total1 = 100
# Llamada con valor predeterminado del 10%
descuento1 = calcular_descuento(monto_total1)
print(f"Compra: ${monto_total1}, Descuento: ${descuento1}, Monto final: ${monto_total1 - descuento1}")

# Segundo monto total de compra
monto_total2 = 65
# Llamada con un descuento del 12%
descuento2 = calcular_descuento(monto_total2,porcentaje_descuento=12)
print(f"Compra: ${monto_total2}, Descuento: ${descuento2}, Monto final: ${monto_total2 - descuento2}")