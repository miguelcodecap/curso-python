
ticker = input("ticker ")
banco = input("banco ")
monto_de_inversion = float(input("monto de inversión "))
precio_hace_1_año = float(input("precio hace un año "))
precio_de_hoy= float(input("precio de hoy "))
tasa_de_plazo_fijo = float(input("tasa de plazo fijo "))

#cálculos:

acciones_que_pude_comprar = int(monto_de_inversion / precio_hace_1_año)
costo_real = acciones_que_pude_comprar * precio_hace_1_año
valor_hoy = acciones_que_pude_comprar * precio_de_hoy
ganancia_de_la_accion = valor_hoy - costo_real
rendimiento_de_la_accion = round(ganancia_de_la_accion / costo_real *100, 2)
monto_con_plazo_fijo_a_1_año = monto_de_inversion*(1+tasa_de_plazo_fijo)
ganancia_con_plazo = monto_con_plazo_fijo_a_1_año - monto_de_inversion
diferencia_entre_acción_y_plazo_fijo =  ganancia_de_la_accion - ganancia_con_plazo

print("---Acción ", ticker, "---")
print("Acciones compradas: " , acciones_que_pude_comprar)
print("Costo real: " , costo_real)
print("Valor hoy: " , valor_hoy)
print("Ganancia con la accion: " , ganancia_de_la_accion)
print("Rendimiento de la acción: ", rendimiento_de_la_accion,"%")

print("---Plazo fijo de", banco, "---")
print("Monto después de 1 año: " , monto_con_plazo_fijo_a_1_año)
print("Ganancia: ", ganancia_con_plazo)

print("---Comparación---")
print("Diferencia acciones vs plazo fijo: ", diferencia_entre_acción_y_plazo_fijo)

