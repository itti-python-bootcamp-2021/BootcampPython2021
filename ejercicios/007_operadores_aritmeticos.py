"""
Solicitar al usuario:
    -Nombre de producto
    -Número de unidades
    -Precio unitario
    -Porcentaje de descuento
    -Porcentaje de impuesto
Calcular el precio final.
Ejemplo: Gaseosa, 10, 2, 2.5% dto., 4% impuesto.=>20,28€
"""
nombre = input("Introduce el nombre del producto:")
numero_unidades = float(input("Introduce el número de unidades:"))
precio_unitario = float(input("Introduce el precio unitario:"))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento:"))
porcentaje_impuesto = float(input("Introduce el porcentaje de impuesto:"))

#precio_final = ((numero_unidades * precio_unitario) * (1-porcentaje_descuento)) * (1+porcentaje_impuesto)
precio_final =  numero_unidades * precio_unitario * (100-porcentaje_descuento) / 100 * (100+porcentaje_impuesto) / 100
    
print(nombre,precio_final)
