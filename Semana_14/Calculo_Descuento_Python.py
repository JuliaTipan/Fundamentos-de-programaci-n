#definir la función para calcular el descuento
def calcular_descuento (monto_total_compra, descuento = 10):
    #calcular el descuento en base al porcentaje
    monto_descuento = monto_total_compra * (descuento / 100)
    #retornar el monto de descuento
    return monto_descuento

#lista de productos
productos = ["pasta dental","cepillo de dientes", "shampoo","jabon","acondicionador"]
#lista de precios correspondientes
precios = [1.55, 0.8, 3.75, 2.45, 3.5]
#calcular el monto total de la compra sumando los precios
monto_total_compra = sum(precios)
#mostrar el monto total
print (f"el monto total de la compra es: {monto_total_compra}")
#calcular el descuento con el valor predeterminado del 10%
descuento_calculado = calcular_descuento (monto_total_compra)
#mostrar el total del descuento
print (f"el monto del descuento es de el (10%): {descuento_calculado}")
#calcular el monto total con el descuento aplicado
monto_final = monto_total_compra - descuento_calculado
#mostrar el monto final
print (f"el monto final despues de aplicar el descuento es: {monto_final}")
